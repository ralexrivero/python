#!/usr/bin/env python3
"""
string indexes
"""

name = 'Ronald'

print(name[0])

# start point [start:stop]

print(name[1:])

numbers = '0123456789'

subNumbers = numbers[1:5]

print(subNumbers)

print(numbers[5:])

# step over [start:stop:step]

print(numbers[0::2])

print(numbers[::1])  # default behavior

print(numbers[::2])

# negative index starts at the end of the string

print(numbers[-1])
print(numbers[-2:])

# print reverse of the string

print(numbers[::-1])
print(numbers[8:2:-1])