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

numbers = input().split()

print(potegowanie_szybkie(int(numbers[0]), int(numbers[1]), int(numbers[2])))

#108 = 22
#97 = 15

print(chr(15) + chr(22) + chr(15))
