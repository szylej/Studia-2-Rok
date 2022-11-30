x = []
k = []
count = 1
odp = []
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

a=input()
pom = int(a) - 1

if int(a) >= 0 and int(a) <= int(wierz):
    for l in range(int(pom), len(k), int(wierz)):
        if k[l]>=1:
            odp.append(count)
        count=count+1

    print(' '.join([str(i) for i in odp]))
else:
    print('BŁĄD')






