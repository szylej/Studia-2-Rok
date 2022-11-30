x = []
k = []
k2 = []
wierz = []
temp = []

def graph_set():

    global wierz

    while True:
        try:
            x = input()
            x = x.split()
            if not x:
                break
            for number in x:
                try:
                    wierz.append(number)
                except ValueError:
                    continue
            k.append(wierz)
            wierz = []
        except EOFError:
            break


def sasiedzi(a):

    for x in k[a]:
        if int(x) not in wierz:
            if int(x) not in temp:
                temp.append(int(x))


def sasiedzi2():

    temp.sort()

    for x in temp:
        wierz.append(x)


def graph_print():

    for i in range(0, len(k2), 1):
        print(k2[i][0], end=" ")
        for j in range(1, len(k2[i]), 1):
            if j == len(k2[i])-1:
                print(k2[i][j])
            else:
                print(k2[i][j], end=" ")

graph_set()

for i in range(0, len(k), 1):
    wierz = []
    wierz.append(int(k[i][0]))
    for j in range(1, len(k[i]), 1):
        sasiedzi(int(k[i][j])-1)
    sasiedzi2()
    k2.append(wierz)
    temp = []

graph_print()
