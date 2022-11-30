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

Z = 26
x = int(keys[0])
results = []

for i in range(1, Z, 1):
    y = (x * i) % Z
    results.append(y)

for i in range(0, len(results), 1):
    if results[i] == 1:
        odw = int(i+1)
        break


if gcd(int(keys[0]), 26) > 1:
    print("BŁĄD")
else:
    final = ""
    for x in content:
        for letter in x:
            if letter in ascii_uppercase:
                final += ascii_uppercase[((ascii_uppercase.index(letter) - int(keys[1])) * int(odw)) % 26]
            elif letter in ascii_lowercase:
                final += ascii_lowercase[((ascii_lowercase.index(letter) - int(keys[1])) * int(odw)) % 26]
            else:
                final += letter

        print(final)
        final = ""

print(str(odw) + " " + keys[1])
