#!/usr/bin/env python3
# password checker

def passCheck(name, password):
    """ print password and user information """
    print("{} your password {} is {} characters longs".
          format(
                 name,
                 '*' * len(password),
                 len(password)
                 ))


name = input("Enter your name: ")
password = input("Enter your password: ")

passCheck(name=name, password=password)
