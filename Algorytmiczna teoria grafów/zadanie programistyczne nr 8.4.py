x = []
k = []
k2 = []
wierz = []


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


def edge_set():

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
            k2.append(wierz)
            wierz = []
        except EOFError:
            break


def assosiaction():

    counter = 0

    for i in range(0, len(k2), 1):
        pom = k2[i][0]
        pom2 = k2[i][1]
        for j in range(i+1, len(k2), 1):
            if pom in k2[j] or pom2 in k2[j]:
                counter += 1

    if counter > 0:
        print("Nie jest to skojarzenie")
    else:
        counter = 0
        for i in range(0, len(k2), 1):
            for j in range(0, len(k), 1):
                if k2[i][0] in k[j] and k2[i][1] in k[j]:
                    counter += 1
        if counter >= 2:
            print("Jest to skojarzenie")
        else:
            print("Nie jest to skojarzenie")


graph_set()
edge_set()
assosiaction()


