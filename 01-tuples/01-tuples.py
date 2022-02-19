#!/usr/bin/env python3
""" tuples are immutable """

tp = (1, 2, 3, 5, 4, 5, 8, 9, 1)

print(tp[1])
print(3 in tp)

x, y, z, *other = tp

print("x: {}\ny: {}\nz: {}\nother: {}".format(x, y, z, other))

print("tp length is: {}".format(len(tp)))

print(tp.count(5))
print(tp.index(3))