from string import ascii_lowercase, ascii_uppercase, ascii_letters
content = []
while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

key = int(content.pop())
final = ""
for x in content:
    for letter in x:
        if letter in ascii_letters:
            final += ascii_letters[(ascii_letters.index(letter) + key) % len(ascii_letters)]
        else:
            final += letter

    print(final)
    final = ""



