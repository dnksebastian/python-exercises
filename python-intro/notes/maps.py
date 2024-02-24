# map(function, data)

from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


words = ['beetroot', 'carrots', 'potatoes']

anagrams = []

# for loop method:

# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# using map:
print(list(map(jumble, words)))

# comprehension method:
print([ jumble(word) for word in words ])
