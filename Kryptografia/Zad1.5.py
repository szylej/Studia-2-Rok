from string import ascii_lowercase, ascii_uppercase
from math import gcd
content = []
while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

keys = content.pop()

k = keys.split()
keys = []
for i in k:
    keys.append(i)

if gcd(int(keys[0]), 26) > 1:
    print("BŁĄD")
else:
    final = ""
    for x in content:
        for letter in x:
            if letter in ascii_uppercase:
                final += ascii_uppercase[((ascii_uppercase.index(letter) * int(keys[0])) + int(keys[1])) % 26]
            elif letter in ascii_lowercase:
                final += ascii_lowercase[((ascii_lowercase.index(letter) * int(keys[0])) + int(keys[1])) % 26]
            else:
                final += letter

        print(final)
        final = ""
