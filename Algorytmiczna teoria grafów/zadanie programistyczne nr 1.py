from itertools import islice

def make_chunks(data, SIZE):
    it = iter(data)
    for i in range(0, len(data), SIZE):
        yield [k for k in islice(it, SIZE)]

k = []
pom = []
st_wierz = []
n = 0
wierz=0
z=2
kraw=0
counter=0
polaczony = 0
drzewo = 0
sciezka = 0
cykl = 0

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

for l in range(len(k)):
    if k[l]>=1:
        kraw=kraw+1
kraw=kraw/2
kraw=int(kraw)

for sample in make_chunks(k, wierz):
        pom.append(sample)

for i in range(0, len(pom), 1):
    for j in range(0, len(pom[i]), 1):
        if pom[i][j] == 1:
            counter = counter+1
    st_wierz.append(counter)
    counter = 0

for i in range(0, len(st_wierz), 1):
    counter = counter + st_wierz[i]

srednia = counter/wierz

if srednia % 1 == 0:
    srednia = int(srednia)

counter = 0
for i in range(0, len(pom), 1):
    for j in range(0, len(pom[i]), 1):
        if pom[i][j] == 1:
            counter = counter+1

print("Ilość wierzchołków: "+str(wierz))
print("Ilość krawędzi: "+str(kraw))
print('Stopnie wierzchołków: ', end='')
print(' '.join([str(i) for i in st_wierz]))
print('Średni stopień: ' + str(srednia))

z = 0

if counter == (len(k)-wierz):
    print("Jest to graf pełny.")
    z =+ 1

for i in st_wierz:
    if (i==0) and (st_wierz[0] == 0):
        drzewo = 0
        break
    else:
        drzewo = 1


if ((st_wierz[0]) == 1 and (st_wierz[len(st_wierz)-1]) == 1):
    for i in range (1,len(st_wierz) - 2,1):
        if (st_wierz[i]) == 2:
            sciezka = 1
        else:
            sciezka = 0
    if ((sciezka == 1)):
        print("Jest to ścieżka.")
        z = + 1

if ((kraw == wierz - 1) and (drzewo == 1)):
    print("Jest to drzewo.")
    z = + 1

for i in st_wierz:
    if(i==2):
        cykl = 1
    else:
        cykl = 0
        break

if ((cykl == 1)):
    print("Jest to cykl.")
    z =+ 1


if z == 0:
    print("Graf nie należy do żadnej z podstawowych klas.")
