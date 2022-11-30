#Zadanie 4.2 to samo
key = "10101010"
Sbox1 = ["101", "010", "001", "110", "011", "100", "111", "000", "001", "100", "110", "010", "000", "111", "101", "011"]
Sbox2 = ["100", "000", "110", "101", "111", "001", "011", "010", "101", "011", "000", "111", "110", "010", "001", "100"]
Rounds_value = 8
text = input()
L0 = ""
R0 = ""
first_half = ""
second_half = ""

def split_in_half():

    global L0
    global R0

    for b in range(0, 6, 1):
        L0 += text[b]
    for b in range(6, 12, 1):
        R0 += text[b]

def split_in_half_2(text):

    global first_half
    global second_half

    first_half = ""
    second_half = ""

    for b in range(0, 4):
        first_half += text[b]
    for b in range(4, 8):
        second_half += text[b]

def E(R):

    temp = ""
    perm = "01323245"
    for val in range(0, len(perm), 1):
        temp += R[int(perm[val])]

    return temp

def key_maker(round):

    global key
    new_key = ""

    for b in range(round, len(key)):
        new_key += key[b]

    for b in range(0, round):
        new_key += key[b]

    return new_key

def xor(first_bit_string, second_bit_string):

    xor_of_two_strings = ""
    for i in range(0, len(first_bit_string), 1):
        temp = int(first_bit_string[i]) ^ int(second_bit_string[i])
        xor_of_two_strings += str(temp)

    return xor_of_two_strings

def change(string_of_bytes):

    counter = 0

    for i in range(0, len(string_of_bytes)):
        if i == 0 and int(string_of_bytes[i]) == 1:
            counter += 8
        if i == 1 and int(string_of_bytes[i]) == 1:
            counter += 4
        if i == 2 and int(string_of_bytes[i]) == 1:
            counter += 2
        if i == 3 and int(string_of_bytes[i]) == 1:
            counter += 1

    return counter


split_in_half()
R = R0

for i in range(1, Rounds_value):
    e_r = E(R)
    nkey = key_maker(i)
    first_xor = xor(e_r, nkey)
    split_in_half_2(first_xor)
    sum_of_sbox = str(Sbox1[change(first_half)]) + str(Sbox2[change(second_half)])
    second_xor = xor(L0, sum_of_sbox)
    L0 = R
    R = second_xor

print(R + L0)


