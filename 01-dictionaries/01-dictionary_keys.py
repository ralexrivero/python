#!/usr/bin/env python3
"""
    dictionary keys:
        must be unmutable
        unique, if repeat a key, the previous value is override
"""

d = {
    'a': 1,
    'greet': 'Hello',
    1: 'es',
    200: 'en',
    1.5: [1, 2, 3],
    True: False,
    (1, 2): [4, 5, 6]
}

print(d)

"""
    The value 'True' is an int equls to '1',
    then the value 'es' is override by 'False'
"""
print(d[1])
print(d[(1,2)])
