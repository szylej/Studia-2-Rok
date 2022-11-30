from string import ascii_letters
content = []
while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

final = ""
for key in range(1, 53, 1):
    for x in content:
        for letter in x:
            if letter in ascii_letters:
                final += ascii_letters[(ascii_letters.index(letter) - key) % len(ascii_letters)]
            else:
                final += letter

    print("Klucz: " + str(key) + " | " + "Tekst: " + final)
    final = ""
