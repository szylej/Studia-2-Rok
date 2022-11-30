import itertools

letters = [["a", "b", "c"], ["a", "b", "c"]]

l = itertools.product(*letters)

for word in l:
    print(word)
