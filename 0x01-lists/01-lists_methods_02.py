#!/usr/bin/env python3
# lists methods second part

li = ['a', 'b', 'c', 'g', 'x', 'm', 'd', 'e', 'y', 'w', 'a', 'n', 'a']

print('Original list: {}'.format(li))
ind = []
ind.append(li.index('x'))
print("Index of 'x' value is: {}".format(ind))

c = 'g'
print("Append value of char: '{}' if exists".format(c))

if c in li:
    ind.append(li.index(c))
    print(ind)

c2 = 'a'
print('Value: \'{}\' ocurrs {} times'.format(c2, li.count(c2)))
