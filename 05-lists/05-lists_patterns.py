#!/usr/bin/env python3
# lists common patterns

li = list(range(0, 10))
print('Created list: {}'.format(li))

liA = list(range(97, 123))
alpha = []
for c in liA:
    alpha.append(chr(c))
    print("{}".format(chr(c)), end=" ")
print()

print("Alphabet list: {}".format(alpha))

"""
    join combines a list into a string and
    returns a new string
"""

sentence = ['Hello', 'my', 'name', 'is', 'Ronald']
sentenceNew = ' '.join(sentence)
print('Joined sentece is: \'{}\'\nType: {}'
      .format(sentenceNew, type(sentenceNew)))
