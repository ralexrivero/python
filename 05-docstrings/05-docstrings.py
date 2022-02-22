#!/usr/bin/env python3
"""
    use docstrings
"""


def test(a):
    """prints the paramater 'a' """
    print(a)


help(test)

print(test.__doc__)
