import random

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

t1 = input().encode('utf-8').decode('unicode-escape')
n = int(input())
random.seed(n)
key = random.randbytes(len(t1))

k1 = bytes(t1, encoding='utf8')
k2 = key

answear = fun2(k1, k2)

for i in answear:

    if i == 92:
        end_answear.append("\\")
    if i == 10:
        end_answear.append('\\n')
        continue
    if i == 13:
        end_answear.append('\\r')
        continue
    if i == 9:
        end_answear.append('\\t')
        continue
    if chr(i).isprintable():
        if i < 150:
            end_answear.append(chr(i))
        else:
            end_answear.append("\\x" + str(hex(i)[2:]).zfill(2))
    else:
        end_answear.append("\\x" + str(hex(i)[2:]).zfill(2))

print(''.join(end_answear))
