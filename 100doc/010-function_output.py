#!/usr/bin/env python3
"""
Title case transform
"""

f_name = input("First name: ")
l_name = input("Last name: ")


def title_case(f_name, l_name):
    """
    Transform text to cammel case
    """
    f_name = f_name.lower()
    l_name = l_name.lower()
    f_name_T = ("{:s}{:s}".format(f_name[0].upper(), f_name[1:]))
    l_name_T = ("{:s}{:s}".format(l_name[0].upper(), l_name[1:]))
    print("{:s} {:s}".format(f_name_T, l_name_T))


title_case(f_name, l_name)
