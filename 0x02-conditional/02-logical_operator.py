#!/usr/bin/env python3
""" logical operators """

"""
    < > <= >= == !=
"""
print(4 > 5)
print(5 < 6)
print(1 == 1)
print(1 >= 0)
print(1 <= 0)
print(1 < 2 < 3 < 4)
print(1 != 2)

""" and or not """

a = True
b = False

print(not a)

print(not (a == b))

print(a is True or b is True)

print(a is True and b is True)
