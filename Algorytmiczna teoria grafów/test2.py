test = [[1, 2, 3], [1, 4, 6]]

if 4 not in test[1]:
    print("True")
else:
    print("false")


def graph_power():

    sum = 0

    for i in range(0, len(k2), 1):
        wierz = []
        for o in range(0, len(k2), 1):
            for j in range(0, len(k2[i]), 1):
                if int(k2[i][j]) == 1 and int(k2[o][j]) == 1:
                    pom = int(k2[i][j]) * int(k2[o][j])
                    sum += pom
            wierz.append(sum)
            sum = 0
        k3.append(wierz)


x = 0
while x < len(kraw):

    for i in range(0, len(kraw), 1):
        for j in range(0, len(k[i]), 1):
            if kraw[x][0] == k[i][j]:
                k[i][j] = kraw[x]
    x += 1

for i in range(0, len(kraw), 1):
    k2.append(k[i])

print(k)

