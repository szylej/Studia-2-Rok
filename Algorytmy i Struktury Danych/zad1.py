file = open('3700.txt', 'r')

m = [1381, 2137, 3001, 1400, 2200, 3000]
T = []
keys = []
converted_keys = []


def file_read():
    while file:
        line = file.readline()
        keys.append(line)
        if line == "":
            break


def h(k):

    return k % 13


def convert():

    global keys
    global converted_keys
    suma = 0
    hf = 0

    for i in range(0, len(keys), 1):
        for j in range(0, len(keys[i]), 1):
            if keys[i][j] != "\n":
                hf = ord(keys[i][j])
                suma += hf
            else:
                converted_keys.append(suma)
                suma = 0


def tab_t(m):

    global T
    global converted_keys

    T = []

    for i in range(0, m, 1):
        T.append(0)

    for i in range(0, len(converted_keys), 1):
        T[h(converted_keys[i])] += 1


def ans1(m):

    global T
    counter = 0

    for i in range(0, len(T), 1):
        if T[i] == 0:
            counter += 1

    print("Liczba zerowych pozycji w tablicy T" + "[" + str(m) + "]: " + str(counter))


def ans2(m):

    global T
    max_value = 0

    for i in range(0, len(T), 1):
        if max_value < T[i]:
            max_value = T[i]

    print("Maksymalna wartość w T" + "[" + str(m) + "]: " + str(max_value))


def ans3(m):

    global T
    middle_value = 0
    counter2 = 0

    for i in range(0, len(T), 1):
        if T[i] > 0:
            middle_value += T[i]
            counter2 += 1

    print("Średnia wartość pozycji niezerowych dla " + "T[" + str(m) + "]: " + str(middle_value/counter2) + "\n")


file_read()
convert()

for i in range(0, len(m), 1):
    tab_t(m[i])
    ans1(m[i])
    ans2(m[i])
    ans3(m[i])

file.close()
