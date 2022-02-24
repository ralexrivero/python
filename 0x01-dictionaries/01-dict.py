#!/usr/bin/env python3
""" using dictionaries """

d = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 27,
    'x': "hello",
    'y': [1, 2, 3, 4, 5, 6],
    'z': True,
    'm': 5.7,
    'role': 'Admin'
}

print(d)
print(d['c'])
print(d['role'])

li = [
    {
        'a': [1, 2, 3],
        'b': 'Hi!',
        'c': True,
        'D': None
    },
    {
        'a': [4, 5, 6],
        'b': 'Hi!',
        'c': True,
        'D': None
    }
]

print(li)
print(li[0])
print(li[0]['a'][1])
print(li[1]['a'][1])
