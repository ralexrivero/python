#!/usr/bin/env python3
"""
    data structure: set
    unorder collections of unique objects
    there is no duplicate
"""

st01 = {1, 2, 3}
print(st01)

st02 = {1, 1, 2, 3, 3}
print(st02)

""" remove all duplicated values """
li = [1, 1, 2, 2, 4, 3, 5, 1]
li2 = set(li)

print(li2)


li3 = ['a', 'c', 'x', 'y', 'x', 'a', 'b', 'z']
li4 = set(li3)
print(li4)

li5 = {'a', 'c', 'x', 'y', 'x', 'a', 'b', 'z'}

print('x' in li4)

""" only prints the unique values """
print(len(li5))

""" convert in list """
li6 = list(li5)
li6.sort()
print(li6)
