from itertools import islice

def make_chunks(data, SIZE):
    it = iter(data)
    # use `xragne` if you are in python 2.7:
    for i in range(0, len(data), SIZE):
        yield [k for k in islice(it, SIZE)]

x = []
k = []
l = []
pom = []
n = 0
wierz = 0
n_wierz = 0
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

n = 0
x=input()
while n<len(x):
    if x[n]!=' ':
        l.append(int(x[n]))
        n_wierz=n_wierz+1
    n=n+1

for sample in make_chunks(k, wierz):
        pom.append(sample)

print(pom)

for i in range((len(l)-1)):
    pom[i].append(l[i])

pom.append(l)

for i in range(0, len(pom), 1):
        for y in range(0, len(pom[i]), 1):
            if y != (n_wierz-1):
                print(pom[i][y], end=' ')
            else:
                print(pom[i][y])
