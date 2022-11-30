zbior = []

for i in range(4):
        temp = set()
        temp.add(i+1)
        zbior.append(temp)

print(zbior)
podzb = set()
podzb2 = set()

kraw = [1, 3]

for z in zbior:
    if kraw[0] in z:
        podzb = z
    if kraw[1] in z:
        podzb2 = z
    if podzb.union(podzb2) not in zbior:
        podzb3 = podzb.union(podzb2)
        zbior.append(podzb3)
        zbior.remove(podzb)
        zbior.remove(podzb2)
        podzb = set()
        podzb2 = set()

print(zbior)
kraw = [2, 4]

for z in zbior:
    if kraw[0] in z:
        podzb = z
    if kraw[1] in z:
        podzb2 = z
    if podzb.union(podzb2) not in zbior:
        podzb3 = podzb.union(podzb2)
        zbior.append(podzb3)
        zbior.remove(podzb)
        zbior.remove(podzb2)
        podzb = set()
        podzb2 = set()

print(zbior)
kraw = [2, 3]

for z in zbior:
    if kraw[0] in z:
        podzb = z
    if kraw[1] in z:
        podzb2 = z
    if podzb.union(podzb2) not in zbior:
        podzb3 = podzb.union(podzb2)
        zbior.append(podzb3)
        zbior.remove(podzb)
        zbior.remove(podzb2)
        podzb = set()
        podzb2 = set()

print(zbior)



