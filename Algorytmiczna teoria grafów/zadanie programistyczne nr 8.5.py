x = []
k = []
zbior1 = []
zbior2 = []
wierz = []
odwiedzone_wierzcholki = []
skojarzenie = []


def myFunc(e):
  return len(e)


def graph_set():

    global wierz

    while True:
        try:
            x = input()
            x = x.split()
            if not x:
                break
            for number in x:
                try:
                    wierz.append(number)
                except ValueError:
                    continue
            k.append(wierz)
            wierz = []
        except EOFError:
            break


def zbiory():

    for i in range(0, len(k), 1):
        if k[i][0] not in zbior2:
            zbior1.append(k[i][0])
            for j in range(1, len(k[i]), 1):
                if k[i][j] not in zbior2:
                    zbior2.append(k[i][j])


def check():

    k.sort(key=myFunc)

    for i in range(0, len(k), 1):
        if len(zbior1) == 0:
            break
        for j in range(1, len(k[i]), 1):
            if k[i][0] in zbior1 and k[i][0] not in odwiedzone_wierzcholki:
                if k[i][j] in zbior2 and k[i][j] not in odwiedzone_wierzcholki:
                    odwiedzone_wierzcholki.append(k[i][0])
                    odwiedzone_wierzcholki.append(k[i][j])
                    zbior1.remove(k[i][0])
                    skojarzenie.append(k[i])
            elif k[i][j] in zbior1 and k[i][j] not in odwiedzone_wierzcholki:
                if k[i][0] in zbior2 and k[i][0] not in odwiedzone_wierzcholki:
                    odwiedzone_wierzcholki.append(k[i][0])
                    odwiedzone_wierzcholki.append(k[i][j])
                    zbior1.remove(k[i][j])
                    skojarzenie.append(k[i])

    if len(zbior1) == 0:
        print("Istnieje skojarzenie doskonałe")
        print(skojarzenie)
    else:
        print("Nie istnieje skojarzenie doskonałe")

graph_set()
zbiory()
check()
