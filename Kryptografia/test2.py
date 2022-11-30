def fun1(x):

    temp = []

    for letter in x:
        temp.append(letter)

    temp2 = []

    for letter in temp:
        temp2.append(ord(letter))

    temp = []

    for numbers in temp2:
        temp.append(bin(numbers))

    return temp2


def fun2(x, y):

    temp = []

    for i in range(0, len(x), 1):
        temp.append(x[i] ^ y[i])

    return temp


t1 = "a"
t2 = ","
k1 = fun1(t1)
k2 = fun1(t2)

print(k1)
print(k2)

answear = fun2(k1, k2)
print(answear)

if chr(answear[0]).isprintable():
    print(chr(answear[0]))
else:
    print("\\x" + str(hex(answear[0])[2:]).zfill(2))


