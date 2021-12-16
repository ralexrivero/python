#!/usr/bin/env python3

"""
Basic calculator
"""


# add
def add(n1, n2):
    """
    add two numbers
    """
    return n1 + n2


# subtract
def sub(n1, n2):
    """
    subtract n2 to n1
    """
    return n1 - n2


# multyply
def mul(n1, n2):
    """
    multiply two numbers
    """
    return n1 * n2


# divide
def div(n1, n2):
    """
    divide n1 between n2
    """
    return n1 / n2


modes = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

print("Welcome to the Basic calculator")
n1 = float(input("Enter a number: "))
for f in modes:
    print(f)
option = input("Choose an operation: ")
n2 = float(input("Enter the second number: "))

print("{:.1f} {:s} {:.1f} = {:.1f}".format(n1, option, n2, modes[option](n1, n2)))
