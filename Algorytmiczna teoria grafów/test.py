queue = [1, 2, 3, 4, 5, 6]
col = []

for i in range(0, len(queue), 1):
    col.append(0)

print(col)

col[queue[0]-1] = 1

print(col)

for i in range(1, len(sorted_queue), 1):
        col[int(sorted_queue[i]-1)] = 1
        for j in range(1, len(k[sorted_queue[i]-1]), 1):
            if col[int(sorted_queue[i]-1)] == col[int(k[sorted_queue[i]-1][j])-1]:
                col[int(sorted_queue[i]-1)] += 1


    for i in range(1, len(sorted_queue), 1):
        #col[int(sorted_queue[i]-1)] = 1
        max_col = 0
        for j in range(1, len(k[sorted_queue[i]-1]), 1):
            if col[int(k[sorted_queue[i]-1][j])-1] > max_col:
                max_col = col[int(k[sorted_queue[i]-1][j])-1]

        col[int(sorted_queue[i]-1)] = max_col+1
