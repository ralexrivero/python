#!/usr/bin/env python3
"""
builtin functions
"""

# len function

a = 'Hello'
b = ['a', 'hello', a, 15]

print(len(a))
print(len(a[1:3:2]))
print(len(b))
print(b)
print(len(b[2]))

quote = 'to be or not to be'
print(quote.replace('be', 'me'))
print(quote)

"""
./script.py | cat -e
display $ at end of each line
"""

quote2 = '     hello     world                 '
print(quote2)
print(quote2.strip())
