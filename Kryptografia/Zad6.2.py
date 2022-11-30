#Liczby wzgledznie pierwsze do n

n = int(input())
answear = []
for i in range(n):
    c = 0
    y_a = 0
    y_b = 1
    x_a = 1
    x_b = 0
    a = n
    b = i
    while a * b != 0:
        if a >= b:
            c = (a - a % b)/b
            a = a % b
            x_a = x_a - x_b * c
            y_a = y_a - y_b * c
        else:
            c = (b - b % a)/a
            b = b % a
            x_b = x_b - x_a * c
            y_b = y_b - y_a * c
    if a == 1 or b == 1:
        answear.append(i)

print(len(answear))
print(*answear)
