#!/usr/bin/env python3
# list unpacking

a, b, c, *other, d = list(range(20))

print('a: {}\ttype: {}'.format(a, type(a)))
print('b: {}\ttype: {}'.format(b, type(b)))
print('c: {}\ttype: {}'.format(c, type(c)))
print('other: {}\ttype: {}'.format(other, type(other)))
print('d: {}\ttype: {}'.format(d, type(d)))
