# kupa0 = str(hex(4)[2:]).zfill(2)
# kupa = str(hex(4)[2:])
# kupa2 = str(hex(4))
# print(kupa0)
# print(kupa)
# print(kupa2)

temp = []
text = input().encode('utf-8').decode('unicode-escape')
text2 = input().encode('utf-8').decode('unicode-escape')

for char in text:
    temp.append(ord(char))

print(temp)
