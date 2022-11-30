def czy_skierowany(tab):
    skier = "N"
    for i in range(len(tab)):
        for j in range(1, len(tab[i])):
            x = int(tab[i][j])
            helper = 0
            for n in range(1, len(tab[x-1])):
                if int(tab[x-1][n]) == i+1:
                    helper = 1
            if helper == 0:
                skier = "Y"
    return skier


def skierowanykraw(tab):
    kraw = []
    for i in tab:
        for j in range(1, len(i)):
            buff = int(i[j])
            wiersz = [[int(i[0]), int(i[j])]]
            for x in range(1, len(tab[buff-1])):
                wiersz.append([buff, int(tab[buff-1][x])])
            kraw.append(wiersz)
    print_graph(kraw)


def print_graph(tab):
    for x in tab:
        for y in x:
            print("(", end='')
            print(y[0], end='')
            print(", ", end='')
            print(y[1], end='')
            print(")", end='')
            if y != x[len(x)-1]:
                print(" ", end='')
        print('') 


def nieskierowany(tab):
    kraw=[]
    for x in tab:
        wiersz=[]
        for y in range(1, len(x)):
            a = int(x[0])
            b = int(x[y])
            buff = 0
            for n in kraw:
                if (n[0][0] == a and n[0][1] == b) or (n[0][0] == b and n[0][1] == a):
                    buff = 1
            if buff == 0:
                wiersz = [[a, b]]
                for i in range(1, len(tab[a-1])):
                    bufff = 0
                    pom = [a, int(tab[a-1][i])]
                    n = []
                    for n in wiersz:
                        if n == pom or (n[0] == int(tab[a-1][i]) and n[1] == a):
                            bufff = 1
                    if bufff == 0:
                        wiersz.append(pom)
                for i in range(1, len(tab[b-1])):
                        bufff = 0
                        pom = [b, int(tab[b-1][i])]
                        for n in wiersz:
                            if (n == pom) or (n[0] == int(tab[b-1][i]) and n[1] == b):
                                bufff = 1
                        if bufff == 0:
                            wiersz.append(pom)
                kraw.append(wiersz)
    Sort(kraw)


def Sort(tab):
    tab2 = []
    x = []
    y = []
    for x in tab:
        wiersz = [[x[0][0], x[0][1]]]
        for y in range(1, len(x)):
            
            if x[y][0]<x[y][1]:
                wiersz.append([x[y][0], x[y][1]])
            else:
                wiersz.append([x[y][1], x[y][0]])
            
        tab2.append(wiersz)
    tab3 = []
    p = 1
    while p != 0:
        p = 0
        for x in tab2:
            wiersz=x[0]
            for y in range(2, len(x)):
                if x[y-1][0] > x[y][0]:
                    x[y-1], x[y] = x[y], x[y-1]
                    p = 2
                elif x[y-1][0] == x[y][0] and x[y-1][1] > x[y][1]:
                    x[y-1], x[y] = [y], x[y-1]
                    p = 2
            tab3.append(x)
    
    print_graph(tab2)
                

tab = []
macierz = input("")
macierz = macierz.split()
tab.append(macierz)
while macierz != " ":
    try:
        macierz = input("")
    except EOFError:
        break
    else:
        macierz = macierz.split()
        tab.append(macierz)
skierowany = czy_skierowany(tab)
if skierowany == "N":
    nieskierowany(tab)
else:
    skierowanykraw(tab)
