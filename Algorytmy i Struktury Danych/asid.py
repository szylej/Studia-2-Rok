for i in range(0, len(converted_keys), 1):
        while T[h(converted_keys[i]) + j] != 0:
            if T[h(converted_keys[i]) + j] != 0:
                j += 1
            elif j == m-1:
                j = 0
            elif T[h(converted_keys[i]) + j] == 0:
                T[h(converted_keys[i]) + j] = data[i]
            break
        T[h(converted_keys[i]) + j] = data[i]
