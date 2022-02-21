#!/usr/bin/env python3
"""
    functions allows to don't DRY
    DRY: 'don't repeat yourself'
    Positional parameters and arguments mean that the position matters
"""


def greet(treatment='Mr', name='Person'):
    """
    greet with positional parameters
    and default parameters
    """
    print('Hello {} {}!'.format(treatment, name))


greet()

""" call the function providing arguments """
greet('FSE', 'Ronald')

"""
    keyword arguments
    Is a good practice to follow the flow of the program
    Should use the same order
"""
greet(treatment='Sr', name='Alexander')

print('The function \'greet()\' is allocated in: {}\ntype: {}'
      .format(greet, type(greet)))
