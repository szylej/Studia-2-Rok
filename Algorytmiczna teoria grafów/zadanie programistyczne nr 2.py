from itertools import islice
import sys

x = [] #input
k = [] #macierz
pom = [] #macierz podzielona na wierzcholki
con = [] #pomocnicza do liczenia spojnosci
stos = []
dfs_order = []
n = 0
z=2
wierz=0
pom2 = 0
pom3 = 0
counter = 0
val = 0


def make_chunks(data, SIZE):
    it = iter(data)
    # use `xragne` if you are in python 2.7:
    for i in range(0, len(data), SIZE):
        yield [k for k in islice(it, SIZE)]

def GraphSet(x):

    global n
    global wierz
    global k

    while n<len(x):
        if x[n]!=' ':
            k.append(int(x[n]))
            wierz=wierz+1
        n=n+1

def GraphSet2():

    global wierz
    global n
    global z
    global k


    while z<=wierz:
        n = 0
        x=input()
        while n < len(x):
            if x[n] != ' ':
                k.append(int(x[n]))
            n = n + 1
        z=z+1

def Print():

    global pom
    global wierz

    for i in range(0, len(pom), 1):
        for y in range(0, len(pom[i]), 1):
            if y != (wierz-1):
                print(pom[i][y], end=' ')
            else:
                print(pom[i][y])

def wierzcholek():

    global pom2
    global v

    v = input()
    pom2 = int(v)-1

    if pom2 < 0 or pom2 > (wierz-1):
        print("BŁĄD")
        sys.exit(0)


def spojnosc():

        global val
        global counter
        global con

        for i in range(0, len(pom), 1):
            for j in range(0, len(pom[i]), 1):
                if pom[i][j] == 1:
                    counter =+ 1
            con.append(int(counter))
            counter = 0

        for y in range(0, len(con), 1):
            if con[y] == 0:
                print("Graf jest niespójny")
                val = 1
                break

def split():
    for sample in make_chunks(k, wierz):
        pom.append(sample)

def dfsOrder(pom, i):

    global dfs_order
    global stos
    global wierz
    while len(stos) < wierz:
        for j in range(0, len(pom[i]), 1):
            if pom[i][j] == 1 and (j+1) not in dfs_order: #sprawdzam czy jest sasiadem poprzedniego wierzcholka
                i = j
                stos.append(j)
                dfs_order.append((j+1))
                dfsOrder(pom, i)


GraphSet(x=input())
GraphSet2()
split()
wierzcholek()

if (spojnosc()):
    sys.exit(0)
else:

    stos.append(pom2)
    dfs_order.append((pom2 + 1))
    dfsOrder(pom, pom2)

    print("Porządek DFS: ", end='')
    print(" ".join([str(i) for i in dfs_order]))
    print("Graf jest spójny")
