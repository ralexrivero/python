#!/usr/bin/env python3
"""
    iterables
        strings
        tuples
        lists
        dictionaries
        sets
    can be iterated one by one in the collection
"""

""" Dictionaries """

user = {
    'Name': 'Ronald',
    'Age': 41,
    'Language': 'Python3',
    'Editor': 'VS Code'
}

""" iterate over keys """
for item in user:
    print(item)

"""
    iterate over items
    key:value pair in a tuple
"""
print('\nitems')
for item in user.items():
    print(item)

print('\nvalues')
""" iterate over values """
for items in user.values():
    print(items)

print('\nkeys')
""" specific method for the keys"""
for item in user.keys():
    print(item)

print('\nkey:value unpacked')
""" unpack the key/value pair """
for item in user.items():
    key, value = item
    print('{}: {}'.format(key, value))

""" a shorthand for key value unpack """

print('\nkey:value')
for key, value in user.items():
    print('{}: {}'.format(key, value))
