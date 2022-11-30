main_content = []
k1 = []
k2 = []
end_answear = []

def fun1(x):

    temp = []

    for letter in x:
        temp.append(letter)

    temp2 = []

    for letter in temp:
        temp2.append(ord(letter))

    return temp2


def fun2(x, y):

    temp = []

    for i in range(0, len(x), 1):
        temp.append(x[i] ^ y[i])

    return temp

def read():

    content = []

    while True:
        try:
            line = input()
            if line:
                content.append(line)
        except EOFError:
            break

    return content


main_content = read()

t1 = str(main_content[0])
t2 = str(main_content[1])

k1 = fun1(t1)
k2 = fun1(t2)

answear = fun2(k1, k2)

for i in answear:

    if chr(i).isprintable():
        end_answear.append(chr(i))
    else:
        end_answear.append("\\x" + str(hex(i)[2:]).zfill(2))

print(''.join(end_answear))
