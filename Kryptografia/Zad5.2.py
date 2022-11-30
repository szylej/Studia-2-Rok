import hashlib

text = input()
print(bin(int('1'+hashlib.md5(bytes(text, encoding='utf8')).hexdigest(), 16))[3:])
