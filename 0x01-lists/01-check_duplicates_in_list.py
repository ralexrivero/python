#!/usr/bin/env python3
# check duplicated values in list

dup_list = ['a', 'b', 'c', 'b', 'd', 'e', 'a', 'm', 'n', 'a', 'n']

only_dup = set()

for x in dup_list:
    if dup_list.count(x) > 1:
        only_dup.add(x)

only_dup_list = list(only_dup)

only_dup_list.sort()

print(only_dup_list)
