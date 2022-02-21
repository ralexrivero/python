#!/usr/bin/env python3
# check duplicated values in list without using set

dup_list = ['a', 'b', 'c', 'b', 'd', 'e', 'a', 'm', 'n', 'a', 'n']

duplicates = []

for x in dup_list:
    if dup_list.count(x) > 1:
        if x not in duplicates:
            duplicates.append(x)

print(duplicates)
