#!/usr/bin/env python3
""" object oriented programming """

from socket import J1939_EE_INFO_NONE


a = None
b = True
c = 2
d = 1.1
e = 'hello'
f = []
g = {1, }
h = {}
i = ()
j = complex(5, 7)

types = [a, b, c, d, e, f, g, h, i, j]

for x in types:
    print('{}'.format(type(x)))
