import random
import sys


def losowanie(seed, n):
    random.seed(seed)
    value = random.randint(2, n-1)
    return value

def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

def potegowanie_szybkie(a, k, n):

    b = bin(k)[2:]
    m = len(b)
    r = 1
    x = a % n

    for i in range(m - 1, -1, -1):
        if b[i] == '1':
            r = r * x % n

        x **= 2
        x %= n

    return r


def m(n):

    for k in range(1, 31, 1):
        pot = 2 ** int(k)
        m = (int(n)-1) / pot
        if m % 2 != 0:
            return m


def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True

def funkcja(n):

    for div in range(3, n):
        if czy_pierwsza(div):
            second_div = n/div
            if czy_pierwsza(int(second_div)):
                if div * second_div == n:
                    print("Liczba złożona: " + str(div) + " * " + str(int(second_div)))
                    sys.exit(0)


data = input().split()

n = int(data[0])
k = int(data[1])
s = int(data[2])
m = m(n)
a = losowanie(s, n)
counter = 0


if nwd(a, n) != 1:
    funkcja(n)
else:
    first_try = potegowanie_szybkie(a, int(m), n)
    if first_try != 1:
        another_tries = []
        for j in range(0, k):
            another_try = potegowanie_szybkie(a, (int(m*(2**int(j)))), n)
            another_tries.append(another_try)
        if another_tries.__contains__(1):
            for x in range(0, len(another_tries)):
                if another_tries[x] == 1:
                    value_to_check = another_tries[x-1] - n
                    if value_to_check == -1:
                        print("Liczba jest prawdopodobnie pierwsza")
                        sys.exit(0)
                    funkcja(n)
        else:
            funkcja(n)
    else:
        funkcja(n)
