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


def repeat_calc():
    """
    Repeat calculation with the previous result
    """
    print("Welcome to the Basic calculator")
    n1 = float(input("Enter a number: "))
    for f in modes:
        print(f)
    option = input("Choose an operation: ")
    n2 = float(input("Enter the second number: "))
    first_calc = modes[option](n1, n2)
    print("{:.1f} {:s} {:.1f} = {:.1f}".format(n1, option, n2, first_calc))
    prev_calc = first_calc
    repeat = input("want to continue? type 'y' or 'n': ")
    while (repeat == "y"):
        for f in modes:
            print(f)
        option = input("Pick another operation with {}: ".format(prev_calc))
        n3 = float(input("Enter the next number: "))
        next_calc = modes[option](prev_calc, n3)
        print("{:.1f} {:s} {:.1f} = {:.1f}".format(prev_calc,
              option, n3, next_calc))
        if input("want to continue? type 'y' or start new \
operation 'n': ") == "y":
            prev_calc = next_calc
            repeat = "y"
        else:
            repeat = "n"
            repeat_calc()


repeat_calc()
