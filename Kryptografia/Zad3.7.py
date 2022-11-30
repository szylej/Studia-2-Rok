import secrets

k1 = []
k2 = []
end_answear = []

def fun_xor(x, y):

    temp = []

    for i in range(0, len(x), 1):
        temp.append(x[i] ^ y[i])

    return temp


t1 = "Uniwersytet Gdanski".encode('utf-8').decode('unicode-escape')
key = secrets.token_bytes(len(t1))

k1 = bytes(t1, encoding='utf8')
k2 = key

answear = fun_xor(k1, k2)

for i in answear:

    if i == 92:
        end_answear.append("\\")
    if i == 10:
        end_answear.append('\\n')
        continue
    if i == 13:
        end_answear.append('\\r')
        continue
    if i == 9:
        end_answear.append('\\t')
        continue
    if chr(i).isprintable():
        if i < 150:
            end_answear.append(chr(i))
        else:
            end_answear.append("\\x" + str(hex(i)[2:]).zfill(2))
    else:
        end_answear.append("\\x" + str(hex(i)[2:]).zfill(2))

print(''.join(end_answear))
