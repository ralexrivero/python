#!/usr/bin/env python3
"""
Check if a given number is a prime number
"""


def prime_checker(number):
    for i in range (2, number - 1):
        print(i)
        if number % i == 0:  # not reminder, is not a prime
            return False
    return True


n = int(input("Check this number: "))
result = prime_checker(number = n)
print(result)