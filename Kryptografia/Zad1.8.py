from string import ascii_lowercase, ascii_uppercase


def eleodw(k):

    Z = 26
    x = k
    results = []

    for i in range(1, Z, 1):
        y = (x * i) % Z
        results.append(y)

    for i in range(0, len(results), 1):
        if results[i] == 1:
            return i + 1

def length(text):

    x = text
    leng = 0

    for i in x:
        if i in ascii_uppercase or i in ascii_lowercase:
            leng += 1

    return leng

content = []
k1 = []
k2 = []
counter = 0
while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

word = content.pop()
dlugosc = length(word)

for x in range(0, len(word), 1):
    for y in range(0, len(word[x]), 1):
        k2.append(word[x][y])

final = ""
for a in range(1, 26, 2):
    odw = eleodw(a)
    if odw:
        for b in range(0, 26, 1):
            for x in content:
                for letter in x:
                    if letter in ascii_uppercase:
                        final += ascii_uppercase[((ascii_uppercase.index(letter) - int(b)) * int(odw)) % 26]
                    elif letter in ascii_lowercase:
                        final += ascii_lowercase[((ascii_lowercase.index(letter) - int(b)) * int(odw)) % 26]
                    else:
                        final += letter

            for x in range(0, len(final), 1):
                for y in range(0, len(final[x]), 1):
                    k1.append(final[x][y])

            for x in range(0, len(word), 1):
                if k2[x] in ascii_lowercase or ascii_uppercase:
                    if k1[x] == k2[x]:
                        counter += 1
                else:
                    counter += 1

            if counter == dlugosc or counter == len(word):
                print(final)
                print(str(a) + " " + str(b))
                exit()
            else:
                k1 = []
                counter = 0
                final = ''



