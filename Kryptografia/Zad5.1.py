import hashlib

text = input()
print(hashlib.md5(bytes(text, encoding='utf8')).hexdigest())
