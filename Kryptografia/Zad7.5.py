import sys


def pascal_triangle(x):
    line = [1]
    for i in range(int(x)):
        next_line = [1]
        for j in range(len(line) - 1):
            next_line.append(line[j] + line[j + 1])
        next_line.append(1)
        line = next_line
    return next_line

n = input()
list = pascal_triangle(n)

for i in range(1, len(list)-1):
    if list[i] % int(n) != 0:
        print("Liczba złożona")
        sys.exit(0)

print("Liczba pierwsza")
