#!/usr/bin/env python3
"""
Title case transform
exist a python str.title() can do this job
"""

f_name = input("First name: ")
l_name = input("Last name: ")


def title_case(f_name, l_name):
    """
    Take a first name and last name and format it
    to return the title case version.
    """
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"

    f_name = f_name.lower()
    l_name = l_name.lower()
    f_name_T = ("{:s}{:s}".format(f_name[0].upper(), f_name[1:]))
    l_name_T = ("{:s}{:s}".format(l_name[0].upper(), l_name[1:]))
    return f_name_T + " " + l_name_T


formatted = title_case(f_name, l_name)
print(formatted)
