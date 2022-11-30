import itertools
from string import ascii_lowercase, ascii_uppercase, ascii_letters

numb = {"2": "0", "3": "0", "4": "0", "5": "0", "6": "0", "7": "0", "8": "0", "9": "0", "10": "0", "11": "0",
        "12": "0", "13": "0", "14": "0", "15": "0", "16": "0"}

content = []
content2 = ""
content_without_space = ""
content_without_space2 = []
key = [0]
len_of_keys = []
len_of_keys2 =[]
factors = []
factors_to_check = []
letters_sequency = []
letters_sequency_package = []
possible_keys = []

def sequency(content):

    alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
               "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    first_letters = ["e", "t", "a", "o", "i", "n"]
    last_letters = ["v", "k", "j", "x", "q", "z"]

    first_letters2 = []
    last_letters2 = []

    values = []

    for x in alfabet:
        value = []
        value.append(x)
        counter = 0
        for letter in content:
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

    #print(first_letters)
    #print(first_letters2)

    for x in range(19, 25, 1):
        if values[x][1] != 0:
            last_letters2.append(values[x][0])

    #print(last_letters)
    #print(last_letters2)
    counter = 0
    for x in first_letters2:
        for y in first_letters:
            if x == y:
                counter += 1

    for x in last_letters2:
        for y in last_letters:
            if x == y:
                counter += 1

    return counter

def viginare_decoding(content,key):

    k1 = []
    k2 = []

    k = key

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

while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

content2 = str(content[0]).split(" ")

for word in content2:
    content_without_space += word

for letter in content_without_space:
    content_without_space2.append(letter)

#print(content)
#print(content2)
#print(content_without_space)
#print(content_without_space2)

key.append(content_without_space2[0])
content_without_space2.pop(0)
key.append(content_without_space2[0])
content_without_space2.pop(0)

#print(content_without_space2)
#print(key)

#-----------------------------------------------------------------Znalezienie Czynników

while len(content_without_space2) > 3 and len(key) >= 3:

    key.pop(0)
    key.append(content_without_space2[0])
    content_without_space2.pop(0)
    #print(content_without_space2)
    #print(key)

    for i in range(0, len(content_without_space2)-3, 1):
        if key[0] == content_without_space2[i]:
            if key[1] == content_without_space2[i+1]:
                if key[2] == content_without_space2[i+2]:
                    len_of_key = i+3
                    len_of_keys.append(len_of_key)


for i in len_of_keys:
    for j in range(2, int(i)+1, 1):
        if i % j == 0:
            len_of_keys2.append(j)

len_of_keys2.sort()
#print(len_of_keys)

#print(" ".join([str(i) for i in len_of_keys2]))

#-----------------------------------------------------------------
#Zliczenie Czynników oraz posortowanie
#-----------------------------------------------------------------
for i in numb.keys():
    for j in len_of_keys2:
        if str(j) == i:
            m = int(numb[i]) + 1
            numb.update({i: str(m)})


for i in numb.items():
    temp = []
    temp.append(i[0])
    temp.append(i[1])
    factors.append(temp)

for i in range(len(factors)):
    for j in range(0, len(factors)-i-1):
        if factors[j][1] < factors[j+1][1]:
            factors[j][0], factors[j+1][0] = factors[j+1][0], factors[j][0]
            factors[j][1], factors[j+1][1] = factors[j+1][1], factors[j][1]

#-----------------------------------------------------------------
#Selekcja czynników do sprawdzenia
#-----------------------------------------------------------------

#print(factors)

for i in range(0, 3, 1):
    factors_to_check.append(factors[i][0])

print(factors_to_check)

for i in factors_to_check:
    temp = []
    for j in range(0, int(i), 1):
        text = ""
        for x in range(j, len(content_without_space), int(i)):
            text += content_without_space[x]
        temp.append(text)

    print(temp)

    decoded_options_package = []
    decoded_options = []
    final = ""

    for option in temp:
        for y in ascii_uppercase:
            temp = []
            for letter in option:
                if letter in ascii_uppercase:
                    final += ascii_uppercase[(ascii_uppercase.index(letter) - ascii_uppercase.index(y)) % 26]

            temp.append(final)
            temp.append(y)
            decoded_options.append(temp)
            final = ""

        decoded_options_package.append(decoded_options)
        decoded_options = []

    for element_of_decoded_package in range(0, len(decoded_options_package), 1):
        for decoded_option_index in range(0, len(decoded_options_package[element_of_decoded_package]), 1):
            temp = []
            seq = sequency(str(decoded_options_package[element_of_decoded_package][decoded_option_index][0]))
            decoded_options_package[element_of_decoded_package][decoded_option_index].append(seq)
            temp.append(decoded_options_package[element_of_decoded_package][decoded_option_index][1])
            temp.append(decoded_options_package[element_of_decoded_package][decoded_option_index][2])
            letters_sequency.append(temp)
        letters_sequency_package.append(letters_sequency)
        letters_sequency = []

    print("-----------------------" + i + "--------------------------------------------")
    #print(decoded_options_package)
    #print("-----------------------" + i + "--------------------------------------------")

    for ele_sequency_package in range(0, len(letters_sequency_package), 1):
        for i in range(len(letters_sequency_package[ele_sequency_package])):
            for j in range(0, len(letters_sequency_package[ele_sequency_package]) - i - 1):
                if letters_sequency_package[ele_sequency_package][j][1] < letters_sequency_package[ele_sequency_package][j+1][1]:
                    letters_sequency_package[ele_sequency_package][j][0], letters_sequency_package[ele_sequency_package][j+1][0] = letters_sequency_package[ele_sequency_package][j+1][0], letters_sequency_package[ele_sequency_package][j][0]
                    letters_sequency_package[ele_sequency_package][j][1], letters_sequency_package[ele_sequency_package][j+1][1] = letters_sequency_package[ele_sequency_package][j+1][1], letters_sequency_package[ele_sequency_package][j][1]

    key_letters = []
    for letter_package in range(0, len(letters_sequency_package),1):
        temp = []
        for letter in range(0, len(letters_sequency_package[letter_package]), 1):
            if letters_sequency_package[letter_package][letter][1] > 0 and letters_sequency_package[letter_package][letter][1] != 1:
                temp.append(letters_sequency_package[letter_package][letter][0])
        key_letters.append(temp)


    letters = itertools.product(*key_letters)

    for word in letters:
        temp = ""
        for key in word:
            temp += str(key)
        possible_keys.append(temp)

    #print(letters_sequency_package)
    print(key_letters)
    print(possible_keys)

    for key in possible_keys:
        viginare_decoding(content, key)

    letters_sequency_package = []
    possible_keys = []
    key_letters = []


