file = open('nazwiskaASCII.txt', 'r')
keys = [x.split(" ")[1] for x in open("nazwiskaASCII.txt", "r").read().split("\n") if x != ""]
m = [20101] #30103, 40609, 22000, 30000, 40000]
T = []
data = []
converted_keys = []


def file_read():
    while file:
        line = file.readline()
        data.append(line)
        if line == "":
            break


def convert():

    global keys
    global converted_keys
    suma = 0
    hf = 0

    for i in range(0, len(keys), 1):
        for j in range(0, len(keys[i]), 1):
                hf = ord(keys[i][j])
                suma += hf

        converted_keys.append(suma)
        suma = 0


def h(k):

    return k % 13


def tab_t(m):

    global T
    global converted_keys
    global data

    j = 0
    T = []
    for i in range(0, m, 1):
        T.append(0)

    for i in range(0, len(converted_keys), 1):
        temp = h(converted_keys[i])
        if temp + j > m-1:
            break
        else:
            while T[int(temp) + j] != 0:
                if T[int(temp) + j] != 0:
                    j += 1
                elif j == m-1:
                    j = 0
            T[int(temp) + j] = data[i]

    print(j)
    print(len(T))


#def szukaj():

file_read()
convert()

for i in range(0, len(m), 1):
    tab_t(m[i])
    print(T)


file.close()
