# chinskie twierdzenie o resztach
import sys


def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

def big_m(list):

    multi = list[0]

    for i in range(1, len(list)):
        multi = multi * list[i]

    return multi

A = []
M = []

first_input = input()
second_input = input()


first_input = first_input.split(" ")
second_input = second_input.split(" ")

for i in range(0, len(first_input)):
    A.append(int(first_input[i]))
    M.append(int(second_input[i]))

#First Step

for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if nwd(M[i], M[j]) != 1:
            print("Brak rozwiązania!!!")
            sys.exit(0)

#Second Step

big_M = big_m(M)
Mi = []
for i in M:
    Mi.append(int(big_M/i))

#Thrid Step

Ni = []
for i in range(0, len(M)):
    for N in range(0, 30):
        temp = N * Mi[i]
        if temp % M[i] == 1:
            Ni.append(N)
            break
#Fourth step

a = 0
for i in range(0, len(M)):
    a = a + (A[i] * Mi[i] * Ni[i])
a = a % big_M

print(str(a))
