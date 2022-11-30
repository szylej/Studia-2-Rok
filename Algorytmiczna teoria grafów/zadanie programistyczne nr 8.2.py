x = []
k = []
k2 = []
k3 = []
k4 = []
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


def graph_change():

    for i in range(0, len(k), 1):
        wierz = []
        for j in range(0, len(k), 1):
            if str(j+1) in k[i]:
                if j == i:
                    wierz.append(0)
                else:
                    wierz.append(1)
            else:
                wierz.append(0)
        k2.append(wierz)


def graph_power():

    sum = 0

    for i in range(0, len(k2), 1):
        wierz = []
        for o in range(0, len(k2), 1):
            for j in range(0, len(k2[o]), 1):
                pom = int(k2[i][j]) * int(k2[j][o])
                sum += pom
            wierz.append(sum)
            sum = 0
        k3.append(wierz)


def graph_sum():

    for i in range(0, len(k3), 1):
        wierz = []
        for j in range(0, len(k3[i]), 1):
            pom = k3[i][j] + k2[i][j]
            wierz.append(pom)
        k4.append(wierz)


def graph_print():

    for i in range(0, len(k4), 1):
        print(i+1, end="")
        for j in range(0, len(k4[i]), 1):
            if k4[i][j] == 1:
                if i != j:
                    print(" " + str(j+1), end="")
        print("")


graph_set()
graph_change()
graph_power()
graph_sum()
graph_print()
print(k)
