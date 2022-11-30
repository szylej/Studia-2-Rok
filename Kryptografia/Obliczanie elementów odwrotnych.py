Z = 64
x = 11
results = []

for i in range(1, Z, 1):
    y = (x * i) % Z
    results.append(y)

print(results)

for i in range(0, len(results), 1):
    if results[i] == 1:
        print(i+1)
