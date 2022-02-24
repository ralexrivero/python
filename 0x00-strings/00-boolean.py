#!/usr/bin/env python3

"""
boolean
"""

a = True
b = False

print(type(a), 'and ', type(b))

print(bool(1))

print(bool(0))

print(bool(2))

c = bool().as_integer_ratio()
print(c)

d = 'True'

print(type(d), bool(d))

e = 'False'
print(type(e), bool(e))

f = 0
print(type(f), bool(f))

g = '0'
print(type(g), bool(g))
