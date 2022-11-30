#NWD rozszerzonym algorytmem euklidesa

n = input()
n = n.split(" ")

a = int(n[0])
b = int(n[1])
c = 0
y_a = 0
y_b = 1
x_a = 1
x_b = 0

while a * b != 0:
    if a >= b:
        c = (a - a % b) / b
        a = a % b
        x_a = x_a - x_b * c
        y_a = y_a - y_b * c
    else:
        c = (b - b % a) / a
        b = b % a
        x_b = x_b - x_a * c
        y_b = y_b - y_a * c

if a > 0:
    print(int(x_a), int(y_a), int(a))
else:
    print(int(x_b), int(y_b), int(b))




