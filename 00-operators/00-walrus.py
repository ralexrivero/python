#!/usr/bin/env python3
"""
    walrus operator :=
    assign values to variables as part of larger expressions
"""

text = 'Hello! Is a beautiful day'

if len(text) > 5:
    print('Long text, is {} chars long'.format(len(text)))


""" Now, with walrus """
if (l := len(text)) > 5:
    print('Long text, is {} chars long'.format(l))

while ((n := len(text)) > 1):
    print(n)
    text = text[:-1]  # slice the string from position 0 to len-1

print(text)
