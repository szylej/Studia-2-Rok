file = open('napisy.txt', 'r')


class Node:
    def __init__(self, wyst, znak, left=None, right=None):
        self.wyst = wyst
        self.znak = znak
        self.left = left
        self.right = right
        self.code = ''


keys = []
keys2 = []
nodes = []
znaki = {"A": "0", "a": "0", "Ą": "0", "ą": "0", "B": "0", "b": "0", "C": "0", "c": "0",
         "Ć": "0", "ć": "0", "D": "0", "d": "0", "E": "0", "e": "0", "Ę": "0", "ę": "0",
         "F": "0", "f": "0", "G": "0", "g": "0", "H": "0", "h": "0", "I": "0", "i": "0",
         "J": "0", "j": "0", "K": "0", "k": "0", "L": "0", "l": "0", "Ł": "0", "ł": "0",
         "M": "0", "m": "0", "N": "0", "n": "0", "Ń": "0", "ń": "0", "O": "0", "o": "0",
         "Ó": "0", "ó": "0", "P": "0", "p": "0", "Q": "0", "q": "0", "R": "0", "r": "0",
         "S": "0", "s": "0", "Ś": "0", "ś": "0", "T": "0", "t": "0", "U": "0", "u": "0",
         "V": "0", "v": "0", "W": "0", "w": "0", "X": "0", "x": "0", "Y": "0", "y": "0",
         "Z": "0", "z": "0", "Ź": "0", "ź": "0", "Ż": "0", "ż": "0", " ": "0", ".": "0",
         ",": "0"}


def file_read():
    while file:
        line = file.readline()
        if line == "":
            break
        keys.append(line)


def bubbleSort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j][0], arr[j + 1][0] = arr[j + 1][0], arr[j][0]
                arr[j][1], arr[j + 1][1] = arr[j + 1][1], arr[j][1]


def zliczanie():

    litery = znaki.keys()

    for i in range(0, len(keys), 1):
        for j in range(0, len(keys[i]), 1):
            for x in litery:
                if keys[i][j] == x:
                    m = int(znaki[x]) + 1
                    znaki.update({x: str(m)})

    for litera, wartosc in znaki.items():
        if int(wartosc) != 0:
            temp_list = []
            temp_list.append(litera)
            temp_list.append(wartosc)
            keys2.append(temp_list)


def NodeChange():

    for i in range(0, len(keys2), 1):
        temp = Node(int(keys2[i][1]), keys2[i][0])
        nodes.append(temp)

    while len(nodes) > 1:

        right = nodes[0]
        left = nodes[1]

        right.code = 1
        left.code = 0

        sumNode = Node(left.wyst + right.wyst, left.znak + right.znak, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(sumNode)


def PrintTable():

    for i in range(0, len(keys2), 1):
        print("Symbol: " + str(keys2[i][0]) + " " + "Ilość wystąpień: " + str(keys2[i][1]))


file_read()
zliczanie()
bubbleSort(keys2)
NodeChange()
print(keys2)
PrintTable()
