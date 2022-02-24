#!/usr/bin/env python3
"""
    range object
"""

a = range(0, 10)
print(a)
print(type(a))

for x in a:
    print(x, end=' ')
print()

for a in range(0, 20):
    print(a, end=' ')
print()

for _ in range(0, 100, 10):
    print(_, end=' ')
print()

for _ in range(10, -10, -1):
    print(_, end=' ')
print()

li = list(range(10))
print(li)
