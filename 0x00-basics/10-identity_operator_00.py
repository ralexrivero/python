#!/usr/bin/python3
a = ["one", 2, None]
b = ["one", 2, None]

print(a is b)

c = a

print(a is c)

x = "Some"
y = None

print(x is not None, y is None)