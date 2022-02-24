#!/usr/bin/env python3

import os
"""
Secret auction
"""

greeting = "Welcome to the auction program"

auction = {}
loop = True
maxValue = 0


def addAuction(name, bid):
    auction[name] = bid


while (loop):
    name = input("What is your name? ")
    bid = int(input("What is your bid? $ "))
    addAuction(name, bid)
    if (bid > maxValue):
        winner = name
        maxValue = bid
    other = input("Are there any other bidders? Type 'yes' or 'Not' ")
    other = other.lower()
    if (other == 'not'):
        loop = False
    os.system('clear')

print(auction)
print("The winner is: {:s} : with a bid of $ {:d}".format(winner, maxValue))
