main_content = []
k1 = []
k2 = []
end_answear = []
temp = []

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

def fun3(x):

    odp = ""

    for i in x:
        odp += chr(i)

    return odp

t1 = input().encode('utf-8').decode('unicode-escape')
t2 = input().encode('utf-8').decode('unicode-escape')

for char in t1:
    temp.append(ord(char))

k1 = temp
k2 = fun1(t2)

answear = fun2(k1, k2)

final = fun3(answear)

print(final)


