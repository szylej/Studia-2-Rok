from itertools import islice

x = [] #input
k = [] #macierz
pom = [] #macierz podzielona na wierzcholki
n = 0
z=2
wierz=0
st_wierz = []


def make_chunks(data, SIZE):
    it = iter(data)
    # use `xragne` if you are in python 2.7:
    for i in range(0, len(data), SIZE):
        yield [k for k in islice(it, SIZE)]


def GraphSet(x):

    global n
    global wierz

    while n<len(x):
        if x[n]!=' ':
            k.append(int(x[n]))
            wierz=wierz+1
        n=n+1


def GraphSet2():

    global z

    while z<=wierz:
        n = 0
        x=input()
        while n < len(x):
            if x[n] != ' ':
                k.append(int(x[n]))
            n = n + 1
        z=z+1


def split():
    for sample in make_chunks(k, wierz):
        pom.append(sample)


def Print():

    global pom
    global wierz

    for i in range(0, len(pom), 1):
        for y in range(0, len(pom[i]), 1):
            if y != (wierz-1):
                print(pom[i][y], end=' ')
            else:
                print(pom[i][y])


def graph_consistency():

    sum = []

    for i in range(0, len(pom), 1):
        a = 0
        for j in range(0, len(pom[i]), 1):
            a += pom[i][j]
        sum.append(a)

    for i in sum:
        if i == 0:
            return 1


def degrees():

    counter = 0

    for i in range(0, len(pom), 1):
        for j in range(0, len(pom[i]), 1):
            if pom[i][j] == 1:
                counter = counter+1
        st_wierz.append(counter)
        counter = 0

    for i in st_wierz:
        if i%2 == 0:
            counter += 1

    return counter



GraphSet(x=input())
GraphSet2()
split()


if graph_consistency() == 1:
    print("Graf jest niespójny")
else:
    if degrees() == wierz:
        print("Graf jest eulerowski")
    elif degrees() >= wierz - 2:
        print("Graf jest półeulerowski")
    else:
        print("Graf nie jest eulerowski")
