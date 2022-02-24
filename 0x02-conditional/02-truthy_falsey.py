#!/usr/bin/env python3
"""
    truthy:
        when running boolean conversion evaluates to True
    falsey:
        when running boolean convesion evaluates to False
"""


""" truthy """
print(bool('Hello'))
print(bool(5))

""" falsey """
print(bool(''))
print(bool(0))
print(bool(None))
print(bool([]))


password = 'abcd1234'
username = 'John'

if password and username:
    print('Both values exist')
else:
    print('Complete the registration')
