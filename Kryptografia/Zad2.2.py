from string import ascii_lowercase, ascii_uppercase
content = []
k1 = []
k2 = []
while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

k = content.pop()

for x in range(0, len(k), 1):
    k1.append(k[x])
    if k[x] in ascii_uppercase:
        k2.append(int(ascii_uppercase.index(k[x])))
    elif k[x] in ascii_lowercase:
        k2.append(int(ascii_lowercase.index(k[x])))


i = 0
final = ""
for x in content:
    for letter in x:
        key = k2[i]
        if i == (len(k2)-1):
            i = -1
            if letter in ascii_uppercase:
                final += ascii_uppercase[(ascii_uppercase.index(letter) - int(key)) % 26]
                i += 1
            elif letter in ascii_lowercase:
                final += ascii_lowercase[(ascii_lowercase.index(letter) - int(key)) % 26]
                i += 1
            else:
                final += letter
        else:
            if letter in ascii_uppercase:
                final += ascii_uppercase[(ascii_uppercase.index(letter) - int(key)) % 26]
                i += 1
            elif letter in ascii_lowercase:
                final += ascii_lowercase[(ascii_lowercase.index(letter) - int(key)) % 26]
                i += 1
            else:
                final += letter


    print(final)
    final = ""
