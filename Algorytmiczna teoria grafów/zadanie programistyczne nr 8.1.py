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


def complement():

    for i in range(0, len(k), 1):
        wierz = []
        wierz.append(k[i][0])
        for j in range(0, len(k), 1):
            if k[j][0] not in k[i]:
                wierz.append(j+1)
        k2.append(wierz)


def print_graph():

    for i in range(0, len(k2), 1):
        for j in range(0, len(k2[i]), 1):
            if j == len(k2[i])-1:
                print(k2[i][j])
            else:
                print(k2[i][j], end=" ")


graph_set()
complement()
print_graph()
