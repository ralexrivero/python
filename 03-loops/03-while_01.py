#!/usr/bin/env python3
""" while loop """

""" continue """
j = 0
li = list(range(20))
print(li)
while j < 20:
    j += 1
    if j < 15:
        """ back to the loop """
        continue
    print(li[j - 1])
