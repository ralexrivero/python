#!/usr/bin/env python3

"""
caesar cipher encode and decode for encrypt messages in ascii code
Displace the character the number of positions given by the user
    lowecase
    uppercase
    numbers
    space
"""


def caesar(direction, text, shift):
    """
    Encrypt and decrypt text and numbers using Caesar Cipher Encrypt.
    Direction stablish the type:
        encode = move to the right
        decode = move to the left
    text: the text to process
    shift: amount of position to move
    """
    if direction == "decode":
        sign = -1
    else:
        sign = 1
    for t in text:
        c = ord(t)
        if c == 32:
            cipher = 32
        elif c >= 48 and c <= 57:
            cipher = c + (sign * shift)
            if cipher > 57:
                cipher -= 10
            elif cipher < 48:
                cipher += 10
        elif c >= 65 and c <= 90:
            cipher = c + (sign * shift)
            if cipher > 90:
                cipher -= 26
            if cipher < 65:
                cipher += 26
        elif c >= 97 and c <= 122:
            cipher = c + (sign * shift)
            if cipher > 122:
                cipher -= 26
            elif cipher < 97:
                cipher += 26
        print("{:c}".format(cipher), end='')
    print()


""" Take input from the user """
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

""" Call the function using the arguments given by the user """
caesar(direction, text, shift)
