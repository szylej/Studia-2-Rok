import math
import random
n = 8
gora = math.log2(n)
print(gora)
for alfa in range(2, int(gora)):
    print(2**int(alfa))
    if n == 2**int(alfa):
        print("Jest potęgą")

list1 = [0, 1, 2]

print(list1.__contains__(1))

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

print(czy_pierwsza(13))

random.seed(13)
value = random.randint(2, 12)
print(value)
