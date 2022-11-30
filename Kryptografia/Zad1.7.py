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


content = []
while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

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

            print("A=" + str(a) + " B=" + str(b) + " " + final)
            final = ""
    else:
        continue
