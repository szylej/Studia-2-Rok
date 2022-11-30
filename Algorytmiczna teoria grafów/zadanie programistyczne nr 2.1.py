from itertools import islice
import sys

x = []
k = []
pom = []
pom2 = []
con = []
n = 0
wierz=0
counter = 0
z=2
val = 0
suma = 0
kraw = []
kraw2 = []
wag = []
zbior = []
podzb = set()
podzb2 = set()

def make_chunks(data, SIZE):
    it = iter(data)
    # use `xragne` if you are in python 2.7:
    for i in range(0, len(data), SIZE):
        yield [y for y in islice(it, SIZE)]

def GraphSet():

    global n
    global wierz
    global k

    x=input()

    while n<len(x):
        if x[n] == x[len(x)-1]:
            if x[n]!=' ':
                k.append(int(x[n]))
                wierz=wierz+1
        else:
            if x[n]!=' ' and x[n + 1]!=' ':
                k.append(int(str(x[n]) + str(x[n+1])))
                wierz=wierz+1
                n=n+2
            elif x[n]!=' ':
                k.append(int(x[n]))
                wierz=wierz+1
        n=n+1

def GraphSet2():

    global wierz
    global n
    global z
    global k


    while z<=wierz:
        n=0
        x=input()
        while n < len(x):
            if x[n] == x[len(x)-1]:
                if x[n]!=' ':
                    k.append(int(x[n]))
            else:
                if x[n]!=' ' and x[n + 1]!=' ':
                    k.append(int(str(x[n]) + str(x[n+1])))
                    n=n+2
                elif x[n]!=' ':
                    k.append(int(x[n]))
            n=n+1
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

def split():
    for sample in make_chunks(k, wierz):
        pom.append(sample)

def split2(kraw2):

    for sample in make_chunks(kraw2, 2):
        pom2.append(sample)

def spojnosc():

        global val
        global counter
        global con

        for i in range(0, len(pom), 1):
            for j in range(0, len(pom[i]), 1):
                if pom[i][j] == 0:
                    counter += 1
            con.append(int(counter))
            counter = 0

        for y in range(0, len(con), 1):
            if con[y] == wierz:
                print("Graf jest niespójny")
                sys.exit(0)


def bubblesort(list, list2):

    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp

                temp = list2[idx]
                list2[idx] = list2[idx+1]
                list2[idx+1] = temp

def pobierz(wierz):

    for z in zbior:
        if wierz in z:
            return z


def krawRead():

    for i in range(0, len(pom), 1):
        for y in range(0, len(pom[i]), 1):
            if pom[i][y] > 0:
                if (str(i+1) + ":" + str(y+1)) not in kraw and (str(y+1) + ":" + str(i+1)) not in kraw:
                    kraw.append(str(i+1) + ":" + str(y+1))
                    kraw2.append(i+1)
                    kraw2.append(y+1)
                    wag.append(pom[i][y])


def createZbior():

    for i in range(wierz):
        temp = set()
        temp.add(i+1)
        zbior.append(temp)


def shortPath():

    global suma
    global podzb
    global podzb2

    for k2, k in enumerate(pom2):
        podzb = pobierz(k[0])
        podzb2 = pobierz(k[1])
        if podzb != podzb2:
            podzb3 = podzb.union(podzb2)
            zbior.append(podzb3)
            zbior.remove(podzb)
            zbior.remove(podzb2)
            podzb = set()
            podzb2 = set()
            suma += wag[k2]

    print(suma)


GraphSet()
GraphSet2()
split()
krawRead()
split2(kraw2)
bubblesort(wag, pom2)
createZbior()

if(spojnosc()):
    sys.exit(0)
else:
    shortPath()




