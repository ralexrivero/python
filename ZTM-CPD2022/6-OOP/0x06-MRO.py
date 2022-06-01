#!/usr/bin/env python3
""" MRO Method Resolution Order """


class A:
    """ class A """
    num = 10


class B(A):
    """ class B inherits from class A """
    pass


class C(A):
    """ class C inherits from class A"""
    num = 1


class D(B, C):
    """ class D, multiple inheritance from class B and class C"""
    pass

print(A.num)
print(B.num)
print(C.num)
print(D.num)

# print the MRO of the class
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())