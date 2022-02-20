#!/usr/bin/env python3
""" enumerate an iterable object """

""" unpack an enumerated string """
for i, val in enumerate('Ronald'):
    print('{}: {}'.format(i, val))
print()

""" unpack an enumerated list """
li = [1, 2, 3, 4]
for i, val in enumerate(li):
    print('{}: {}'.format(i, val))
