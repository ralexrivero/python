#!/usr/bin/env python3
"""
    print the highest even number in a list
"""

li = [10, 2, 3, 20, 15, 29, 0, 1, 2, 35, 3, 4, 49, 5, 50, 51, 7, 6]


def highest_even(li):
    """ return the highest even number """
    li.sort()
    li.reverse()
    for x in li:
        if x % 2 == 0:
            return x


evenNum = highest_even(li)

print(evenNum)
