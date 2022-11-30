import random

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

def losowanie(seed, n):
    value = random.randrange(2**(n-1), 2**n)
    return value

data = input()
data = data.split()

n = int(data[0])
s = int(data[1])
random.seed(s)
generated_key = losowanie(s, n)

print(str(generated_key))
print(str(generated_key))

