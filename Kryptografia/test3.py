tekst = "\\x0e\\x19\\x09"

k1 = []
k = tekst.split("\\")

for x

print(tekst


while(int(flag) <= int((len(content_without_space)-1))):
    print(content_without_space[flag])
    flag += 1

for x in range(0, len(start_from_0), 1):
    counter = str(start_from_0[x]) + ""
    for y in range((x+1), len(start_from_0), 1):
        if start_from_0[x] == start_from_0[y]:
            len_of_keys.append(len(start_from_0[x]))
            len_of_keys.append(len(counter))
        counter += str(start_from_0[y])

    counter = ""
    flag += 3


content = []
content2 = ""
content_without_space = ""
len_of_keys = []


def elemenets(x, y):

    temp_list = []
    temp_element = ""

    for i in range(y, len(x), 1):
        temp_element += x[i]
        if len(temp_element) == 3:
            temp_list.append(temp_element.lower())
            temp_element = ""

    return temp_list


def key_len_finder(table):

    flag = 0

    for x in range(0, len(table), 1):
        counter = str(table[x]) + ""
        for y in range((x+1), len(table), 1):
            if table[x] == table[y]:
                len_of_keys.append(len(table[x]))
                len_of_keys.append(len(counter))
            counter += str(table[y])

        counter = ""
        flag += 3


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

start_from_0 = elemenets(content_without_space, 0)
start_from_1 = elemenets(content_without_space, 1)
start_from_2 = elemenets(content_without_space, 2)

print(content)
print(content2)
print(content_without_space)

print(start_from_0)
print(start_from_1)
print(start_from_2)

key_len_finder(start_from_0)
key_len_finder(start_from_1)
key_len_finder(start_from_2)


print(" ".join([str(i) for i in len_of_keys]))

Ogolnie GITT TYLKO elementy mogą być wieksze niż 3!!!!

for i in len_of_keys:
    for j in range(2, 17, 1):
        if i % j == 0:
            if j not in len_of_keys:
                len_of_keys.append(j)

for i in len_of_keys:
    if i < 17:
        len_of_keys2.append(i)


print(content)
print(content2)
print(content_without_space)

print(start_from_0)
print(start_from_1)
print(start_from_2)
