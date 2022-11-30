def nwd(a, b):
    if b > 0:
        return nwd(b, a%b)
    return a

x1 = input()
x2 = input()

print(nwd(int(x1), int(x2)))
