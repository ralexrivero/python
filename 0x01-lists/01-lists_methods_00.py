#!/usr/bin/env python3
# list methods and return value

li = [1, 2, 3, 4, 5]

liCopy = li
""" .append make changes in place
and don't generate return value (see 3th printed value"""
liReturn = li.append(100)

print("Original: {}\nCopy: {}\nReturn Copy: {}".format(li, liCopy, liReturn))

""" other methods"""

li.insert(3, 0)
print("After insert at index: {}".format(li))

auxiliar = [6, 7, 8, 9]
li.extend(auxiliar)
print("Extend: {}".format(li))

li.sort()
print("Sorted: {}".format(li))

li.pop()
print("Pop remove: {}".format(li))

liPop = li.pop(3)
print("Pop at given index: {}".format(li))
print("Poped value : {}".format(liPop))

li.remove(8)
print("Remove a given value: {}:".format(li))

li.clear()
print("Clear the list: {}".format(li))
