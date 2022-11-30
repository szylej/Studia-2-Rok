if (spojnosc()):
    sys.exit(0)
else:
    for i in range(wierz):
        temp = set()
        temp.add(i+1)
        zbior.append(temp)

    for i in range(0, len(pom2), 1):
        for z in zbior:
            if pom2[i][0] in z:
                podzb = pobierz(i)
            if pom2[i][1] in z:
                podzb2 = z
            if podzb.union(podzb2) != set() and podzb != set() and podzb2 != set():
                if podzb.union(podzb2) not in zbior:
                    print(zbior)
                    podzb3 = podzb.union(podzb2)
                    zbior.append(podzb3)
                    print(zbior)
                    zbior.remove(podzb)
                    zbior.remove(podzb2)
                    podzb = set()
                    podzb2 = set()
                    suma += wag[i]
