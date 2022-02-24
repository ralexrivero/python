#!/usr/bin/env python3
""" set methods """

st01 = {1, 2, 3, 4, 5}
st02 = {4, 5, 6, 7, 8, 9}

print(st01.intersection(st02))

print(st01.difference(st02))

st01.discard(5)
print(st01)

st01.difference_update(st02)
print(st01)
print(st02)

""" return True if two sets have nothing in common """
print(st01.isdisjoint(st02))

""" united two sets and remove any duplicates """

print(st01.union(st02))

print(st01)
print(st02)

st03 = {4, 5}

print(st03.issubset(st02))

print(st03.issuperset(st02))
print(st02.issuperset(st03))
