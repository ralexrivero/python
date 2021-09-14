#!/usr/bin/python3
values = ["a", "b", "c"]

for value in values:
    print(value)

print()

index = 0

for value in values:
    print(index, value)
    index += 1

print()

for index in range(len(values)):
    value = values[index]
    print(index, value)

print()

for count, value in enumerate(values):
    print(count, value)

for count, value in enumerate(values, start=1):
    print(count, value)