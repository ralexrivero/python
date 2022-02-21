#!/usr/bin/env python3
"""
    functions allows to don't DRY
    DRY: 'don't repeat yourself'
"""


def greet(name='Person'):
    """ greet with parameters """
    print('Hello {}!'.format(name))


greet()

""" call the function providing arguments """
greet('Ronald')

greet(name='Alexander')

print('The function \'greet()\' is allocated in: {}\ntype: {}'
      .format(greet, type(greet)))
