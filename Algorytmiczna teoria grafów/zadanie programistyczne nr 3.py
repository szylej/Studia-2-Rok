from itertools import islice
import sys

x = []
k = []
pom = []
pom2 = 0
v = 0
n = 0
wierz=0
counter = 0
z=2

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

def split():
    for sample in make_chunks(k, wierz):
        pom.append(sample)


def wierzcholek():

    global pom2
    global v

    v = input()
    pom2 = int(v)-1

    if pom2 < 0 or pom2 > (wierz-1):
        print("BŁĄD")
        sys.exit(0)


GraphSet()
GraphSet2()
split()
wierzcholek()



