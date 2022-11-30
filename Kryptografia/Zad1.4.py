from string import ascii_lowercase, ascii_uppercase, ascii_letters
content = []
while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

word = content.pop()
final = ""

k1 = []
k2 = []

for x in range(0, len(content), 1):
    for y in range(0, len(content[x]), 1):
        k1.append(content[x][y])

for x in range(0, len(word), 1):
    for y in range(0, len(word[x]), 1):
        k2.append(word[x][y])

for x in range(0, len(word), 1):
    if k2[x] in ascii_letters:
        key = (ascii_letters.index(k1[x]) - ascii_letters.index(k2[x])) % len(ascii_letters)

for x in content:
    for letter in x:
        if letter in ascii_letters:
            final += ascii_letters[(ascii_letters.index(letter) - key) % len(ascii_letters)]
        else:
            final += letter

    print(final)
    final = ""

print(key)


