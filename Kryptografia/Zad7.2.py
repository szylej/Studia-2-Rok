#9 test 2 1 13 2 jest liczba pierwsza
import random

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

data = input().split()

n = int(data[0])
k = int(data[1])
s = int(data[2])
counter = 0

for i in range(0, k):
    if n > 2:
        a = int(losowanie(s, n))
        d = nwd(a, n)
        if d > 1:
            counter += 1
            break
        else:
            last_ans = potegowanie_szybkie(a, (n-1), n)
            if last_ans != 1:
                counter += 1
            else:
                counter += 0
    else:
        counter += 0

if counter > 0:
    print("Liczba złożona")
else:
    print("Liczba prawdopodobnie pierwsza")
