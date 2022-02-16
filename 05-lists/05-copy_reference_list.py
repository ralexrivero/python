#!/usr/bin/env python3
# Copy a list

original = ['a', 'b', 'c']

copy01 = original
copy02 = original[:]

print("before modify 'original':")
print("original: {}\ncopy01: {}\ncopy02: {}".format(original, copy01, copy02))

original.append('d')

print("after modify 'original':")
print("original: {}\ncopy01: {}\ncopy02: {}".format(original, copy01, copy02))
