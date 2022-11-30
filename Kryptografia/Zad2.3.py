from string import ascii_lowercase, ascii_uppercase, ascii_letters

alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

first_letters = ["e", "t", "a", "o", "i", "n"]
last_letters = ["v", "k", "j", "x", "q", "z"]

first_letters2 = []
last_letters2 = []

values = []
content = []

while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

for x in alfabet:
    value = []
    value.append(x)
    counter = 0
    for y in content:
        for letter in y:
            if letter == x:
                counter += 1
            if letter in ascii_uppercase:
                if (ascii_letters.index(letter) % 26) == ascii_lowercase.index(x):
                    counter += 1
        value.append(counter)
        values.append(value)



for iter_num in range(len(values)-1,0,-1):
    for idx in range(iter_num):
        if values[idx][1]<values[idx+1][1]:
            temp = values[idx][1]
            temp2 = values[idx][0]
            values[idx][1] = values[idx+1][1]
            values[idx][0] = values[idx+1][0]
            values[idx+1][1] = temp
            values[idx+1][0] = temp2
        if values[idx][1] == values[idx+1][1]:
            if values[idx][0] < values[idx+1][0]:
                temp = values[idx][1]
                temp2 = values[idx][0]
                values[idx][1] = values[idx+1][1]
                values[idx][0] = values[idx+1][0]
                values[idx+1][1] = temp
                values[idx+1][0] = temp2


for x in range(0, 6, 1):
    first_letters2.append(values[x][0])

print(first_letters)
print(first_letters2)

for x in range(19, 25, 1):
    if values[x][1] != 0:
        last_letters2.append(values[x][0])

print(last_letters)
print(last_letters2)
counter = 0
for x in first_letters2:
    for y in first_letters:
        if x == y:
            counter += 1

for x in last_letters2:
    for y in last_letters:
        if x == y:
            counter += 1

print(counter)

