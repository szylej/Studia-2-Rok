ciag1 = "propsoo"
ciag2 = "pssppos"
A = []


def table_create():

    temp = []

    for i in range(0, len(ciag1)+1, 1):
        temp.append(0)

    A.append(temp)

    for i in range(0, len(ciag2), 1):
        temp = []
        temp.append(0)
        for j in range(0, len(ciag1), 1):
            temp.append(0)

        A.append(temp)


def table_filling():

    for i in range(0, len(ciag2), 1):
        s2 = ciag2[i]
        for j in range(0, len(ciag1), 1):
            s1 = ciag1[j]
            if s2 == s1:
                A[i+1][j+1] = A[i][j] + 1
            else:
                A[i+1][j+1] = max(A[i][j+1], A[i+1][j])


def answear():

    ans = ""
    i = len(ciag2)
    j = len(ciag1)

    while i > 0 and j > 0:
        if A[i][j] == A[i-1][j]:
            i = i - 1
        if A[i][j] == A[i][j-1]:
            j = j - 1
        if A[i][j] != A[i-1][j] and A[i][j] != A[i][j-1]:
            ans = ciag2[i - 1] + ans
            i = i - 1
            j = j - 1

    print("Najdłuższy wspólny podciąg to: " + ans)


def table_print():

    for i in range(0, len(A), 1):
        for j in range(0, len(A[i]), 1):
            if j != len(ciag1):
                print(A[i][j], end=' ')
            else:
                print(A[i][j])
    print("\n", end='')


table_create()
table_filling()
table_print()
answear()










