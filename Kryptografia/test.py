from string import ascii_lowercase, ascii_uppercase, ascii_letters

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

values = []

tekst = "Lccxsr"


for x in alfabet:
    value = []
    value.append(x)
    counter = 0
    for letter in tekst:
        if letter == x:
            counter += 1
        if letter in ascii_uppercase:
            if (ascii_letters.index(letter) % 26) == ascii_lowercase.index(x):
                counter += 1
    value.append(counter)
    values.append(value)

print(values)

for iter_num in range(len(values)-1,0,-1):
    for idx in range(iter_num):
        if values[idx][1]<values[idx+1][1]:
            temp = values[idx][1]
            temp2 = values[idx][0]
            values[idx][1] = values[idx+1][1]
            values[idx][0] = values[idx+1][0]
            values[idx+1][1] = temp
            values[idx+1][0] = temp2

print(values)
