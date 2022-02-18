#!/usr/bin/env python3
# more lists methods

li = ['Joe', 'Clark', 'Madison', 'John', 'Gillian', 'David']

print("Original list: {}".format(li))

"""
    Sort modifies in place
    Sorted doesn't modify the original list and creates a new one
"""

li.sort()
print('Sorted list: {}'.format(li))

li2 = li.copy()
print('Copied list: {}'.format(li2))

"""
    reverse method switch indexes in place
"""

li2.reverse()
print('Reversed : {}'.format(li2))
