#!/usr/bin/env python3
""" global keyword sets the use of a global variable """

total = 0


def count():
    """ increase the value every time is called """
    global total
    total += 1
    return total


print(count())
print(count())
print(count())

total2 = 0


def count2(total2):
    """ increase the value once """
    total2 += 1
    return total2


print(count2(total2))
print(count2(count2(count2(total2))))
