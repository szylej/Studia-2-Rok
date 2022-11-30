import requests
import hashlib
r = requests.get("https://stepik.org/media/attachments/lesson/668860/dictionary.txt")

text = input()
for x in r.iter_lines():
    if hashlib.md5(x.lower()).hexdigest() == text:
        print(x.decode('utf8').lower())
