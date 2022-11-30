n = input()

for k in range(1, 31, 1):
    pot = 2 ** int(k)
    m = (int(n)-1) / pot
    if m % 2 != 0:
        print("2^" + str(k) + " * " + str(int(m)))
        break

