import random

def losowanie(seed, n):
    random.seed(seed)
    value = random.randint(2, n-1)
    return value

for i in range(0, 5):
    print(losowanie(1, 13))
