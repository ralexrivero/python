import string
import random

printable_chars = list(string.printable)

j = 0
valid_chars = []

for i in printable_chars:
    if i == " ":
        break
    valid_chars.append(i)

for i in range(0, 12):
    print(valid_chars[random.randint(0, len(valid_chars))], end='')
print()
