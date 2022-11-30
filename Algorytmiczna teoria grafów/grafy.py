stos = [1, 2, 3]

v = 3

if v == stos[(len(stos)-1)]:
    print("tak")
else:
    print("nie")
i = 1
stos2 = [1,2]

while(len(stos2) != 0):
    stos2.remove(stos2[i])
    print("Usunieto")
    i = i-1

stos.remove(len(stos)-1)
print(stos)
print(stos[len(stos)-1])

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

print(k)
print(wierz)
print(n)
