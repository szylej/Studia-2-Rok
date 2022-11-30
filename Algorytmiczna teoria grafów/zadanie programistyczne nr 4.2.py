x = []
k = []
wierz = []
st_wierz = []
queue = []
sorted_queue = []
col = []
chrom = 0

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


def stopnie():

    for i in range(0, len(k), 1):
        z = len(k[i])-1
        st_wierz.append(z)


def kolejka():

    for i in range(0, len(k), 1):
        queue.append(i+1)


def kolejkasort():

    while len(queue) != len(sorted_queue):

        max_st = 0
        max_label = 0

        for i in range(0, len(queue), 1):
            if max_st < st_wierz[i] and i+1 not in sorted_queue:
                max_st = st_wierz[i]
                max_label = i+1
            elif max_st == st_wierz[i] and i+1 not in sorted_queue:
                if max_label < i+1:
                    max_label = i+1

        sorted_queue.append(max_label)


def kolorowanie():

    for o in range(0, len(sorted_queue), 1):
        col.append(0)

    col[int(sorted_queue[0]-1)] = 1

    for i in range(1, len(sorted_queue), 1):
        col[int(sorted_queue[i]-1)] = 1
        temp_col = []
        for j in range(1, len(k[sorted_queue[i]-1]), 1):
            color = col[int(k[sorted_queue[i]-1][j])-1]
            if color != 0:
                temp_col.append(color)
        temp_col.sort()
        m = 1
        col[int(sorted_queue[i]-1)] = m
        for z in range(0, len(temp_col), 1):
            if col[int(sorted_queue[i]-1)] == temp_col[z]:
                m += 1
            col[int(sorted_queue[i]-1)] = m


def liczba_ch():

    max_col = 0

    for i in col:
        if i > max_col:
            max_col = i

    return max_col

graphset()
stopnie()
kolejka()
kolejkasort()
kolorowanie()
chrom = liczba_ch()

print("Pokolorowanie wierzchołków: ", end='')
print(" ".join([str(i) for i in col]))
print("Liczba chromatyczna" + " == " + str(chrom))
