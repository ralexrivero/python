#!/usr/bin/env python3
"""
    dictionary methods
"""

user = {
    'name': 'Ronald',
    'age': 41,
    'level': 50,
    'title': 'Full Stack SE',
    'City': None
}

print(user.get('name'))
print(user.get('Country'))
""" set default value if key value doesn't exist """
print(user.get('Country', 'Uruguay'))

""" a less common way to create a dictionary """

user2 = dict(name='Alexander', age=41, country='Uruguay')
print(user2)
