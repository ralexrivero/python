#!/usr/bin/env python3
""" tricks with == """
from re import A

""" checks the equlity in value """
print('==')
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print({} == [])
print([1, 2, 3] == [1, 2, 3])

"""
    is checks if the location in memory where the value is stored is the same
"""
print('\nis')
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([] is [])
""" every list as a new allocation in memory
because of that always be False """
print({} is [])
print([1, 2, 3] is [1, 2, 3])
"""
    data structures are created in a new location every time
    dictionaries, sets, lists, tuples
"""
print(True is True)
print(1 is 1)
print('1' is '1')
""" simply types are in the same space of memory"""
print()


a = 1
b = 1
c = a

print(a == c)
print(a is c)
print(a is b)

d = [1, 2]
e = [1, 2]

print(d == e)
print(d is e)
