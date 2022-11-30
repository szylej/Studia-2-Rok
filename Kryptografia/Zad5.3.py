import hashlib

text = input()
text2 = input()
bin_text = bin(int('1'+hashlib.md5(bytes(text, encoding='utf8')).hexdigest(), 16))[3:]
bin_text2 = bin(int('1'+hashlib.md5(bytes(text2, encoding='utf8')).hexdigest(), 16))[3:]

final = 0
for index in range(0, len(bin_text), 1):
    if bin_text[index] != bin_text2[index]:
        final += 1
print("{:.2%}".format(final/128))
