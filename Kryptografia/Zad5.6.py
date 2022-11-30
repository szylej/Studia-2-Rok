import hashlib
import secrets
from string import ascii_letters, ascii_uppercase, ascii_lowercase
import time

hex_letters = []


def random_letter():

    letter_index = secrets.randbelow(len(ascii_lowercase))
    letter = ascii_lowercase[letter_index].encode("utf-8")
    return letter

def main_function(alfabet, hash_function, letter):

    values = []
    hash_letter = hash_function(letter)

    for i in range(10):
        start_time = time.time()

        for letter in alfabet:
            if hash_function(letter.encode("utf-8")) == hash_letter:
                break

        end_time = (time.time()-start_time)

        values.append(end_time)

    return sum(values) / len(values)

example = random_letter()

low_md5 = main_function(ascii_lowercase, hashlib.md5, example)
all_md5 = main_function(ascii_letters, hashlib.md5, example)
low_sha1 = main_function(ascii_lowercase, hashlib.sha1, example)
all_sha1 = main_function(ascii_letters, hashlib.sha1, example)

print('Małe litery Md5: ' + str(low_md5))
print('Wszystkie litery Md5: ' + str(all_md5))
print('Małe litery Sha1: ' + str(low_sha1))
print('Wszystkie litery Sha1: ' + str(all_sha1))
