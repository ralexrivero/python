#!/usr/bin/env python3
import utility
import packages.cart

print(utility.mul(3, 5))
print(utility.divide(20, 7))

packages.cart.add_cart("Bag")
packages.cart.add_cart("Ring")

print("in main_fun: "+ __name__)

print(type(utility.st1))

if __name__ == '__main__':
    print("Run this when main")