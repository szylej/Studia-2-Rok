content = []
content2 = ""
content_without_space = ""
content_without_space2 = []
key = [0]
len_of_keys = []
len_of_keys2 =[]

while True:
    try:
        line = input()
        if line:
            content.append(line)
    except EOFError:
        break

content2 = str(content[0]).split(" ")

for word in content2:
    content_without_space += word.lower()

for letter in content_without_space:
    content_without_space2.append(letter)

#print(content)
#print(content2)
#print(content_without_space)
#print(content_without_space2)

key.append(content_without_space2[0])
content_without_space2.pop(0)
key.append(content_without_space2[0])
content_without_space2.pop(0)

#print(content_without_space2)
#print(key)



while len(content_without_space2) > 3 and len(key) >= 3:

    key.pop(0)
    key.append(content_without_space2[0])
    content_without_space2.pop(0)
    #print(content_without_space2)
    #print(key)

    for i in range(0, len(content_without_space2)-3, 1):
        if key[0] == content_without_space2[i]:
            if key[1] == content_without_space2[i+1]:
                if key[2] == content_without_space2[i+2]:
                    len_of_key = i+3
                    if len_of_key not in len_of_keys:
                        len_of_keys.append(len_of_key)


for i in len_of_keys:
    for j in range(2, int(i)+1, 1):
        if i % j == 0:
            if j not in len_of_keys:
                len_of_keys.append(j)
for i in len_of_keys:
    if i < 17:
        len_of_keys2.append(i)

len_of_keys2.sort()
#print(len_of_keys)

print(" ".join([str(i) for i in len_of_keys2]))
