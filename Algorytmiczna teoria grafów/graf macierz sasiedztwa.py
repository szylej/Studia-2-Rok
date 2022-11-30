from itertools import islice

def make_chunks(data, SIZE):
    it = iter(data)
    # use `xragne` if you are in python 2.7:
    for i in range(0, len(data), SIZE):
        yield [k for k in islice(it, SIZE)]
x = []
k = []
pom = []
wyj = []
wyj2 = []
n = 0
a = 0
wierz=0
z=2

x=input()
while n<len(x):
    if x[n]!=' ':
        k.append(int(x[n]))
        wierz=wierz+1
    n=n+1

while z<=wierz:
    n=0
    x=input()
    while n < len(x):
        if x[n] != ' ':
            k.append(int(x[n]))
        n = n + 1
    z=z+1

a = input()
pom2 = int(a) - 1

if int(a) > 0:
    for sample in make_chunks(k, wierz):
        pom.append(sample)

    print(pom)

    for l in range(0, len(pom), 1):
        if l != pom2:
            for y in range(0, len(pom[l]), 1):
                if y != pom2:
                    wyj.append(pom[l][y])

    for sample in make_chunks(wyj, wierz-1):
        wyj2.append(sample)

    for i in range(0, len(wyj2), 1):
        for y in range(0, len(wyj2[i]), 1):
            if y != (wierz-2):
                print(wyj2[i][y], end=' ')
            else:
                print(wyj2[i][y])

else:
    print('BŁĄD')
