import random
k = int(input())
n = int(input())
random.seed(k)
print(str(random.randbytes(n))[2:-1])
