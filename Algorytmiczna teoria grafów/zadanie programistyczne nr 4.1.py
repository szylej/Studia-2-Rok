x = []
k = []
wierz = []
col = []
counter = 0

def graphset():

    global x, k, wierz

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


def colwierz():

    global col

    col = input()
    col = col.split()


graphset()
colwierz()

print(k)

for i in range(1, len(k), 1):
    pom = col[i]
    for j in range(1, len(k[i]), 1):
        pom2 = col[int(k[i][j])-1]
        if pom == pom2:
            counter += 1

if counter > 0:
    print("Graf nie jest kolorowalny")
else:
    print("Graf jest kolorowalny")
