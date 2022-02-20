#!/usr/bin/env python3
""" for loop """

for item in 'Ronald':
    print('{}: {}'.format(item, ord(item)))

""" nested loop """
print()

for item in [1, 2, 3]:
    for color in ['blue', 'red', 'yellow']:
        print('{} => {}'.format(item, color))
