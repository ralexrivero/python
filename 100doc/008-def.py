#!/usr/bin/env python3
"""
Define and call a function to greet
"""


def line_separator():
    print("\n", "*"*80, "\n")  # separator line


def greet(name):
    """
    display greetings
    """
    print("Hello " + name + " !")
    print(f"Hello everybody and specially to {name} !")
    print("{:s} {:s}!".format("Hello again", name))


"""
name acts like parameter and value setted is the argument
"""
greet("Betty")


def greet_two_param(name, location):
    """
    function recives two parameters
    """
    print("Hello {:s}".format(name))
    print("What is it like in {:s}?".format(location))


line_separator()

greet_two_param("Ronald", "Montevideo")
"""
assign positional argument, order matters here
"""

line_separator()

greet_two_param(location="World Trade Center", name="Jagger")
"""
use keyworded arguments to call the function, here doesen't matter the order
"""

line_separator()
