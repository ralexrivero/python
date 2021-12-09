#!/usr/bin/env python3

"""
caesar cipher encode and decode for encrypt messages in ascii code
Displace the character the number of positions given by the user
lowecase
uppercase
numbers
space
"""


def encrypt(text, shift):
    """
    encrypt text desplacing every character the position given in shift
    """
    for t in text:
        c = ord(t)
        if c == 32:
            cipher = 32
        elif c >= 48 and c <= 57:
            cipher = c + shift
            if cipher > 57:
                cipher -= 10
        elif c >= 65 and c <= 90:
            cipher = c + shift
            if cipher > 90:
                cipher -= 26
        elif c >= 97 and c <= 122:
            cipher = c + shift
            if cipher > 122:
                cipher -= 26
        print("{:c}".format(cipher), end='')
    print()


def decrypt(text, shift):
    """
    de-encrypt the text, previously encrypted given the right shift number
    """
    for t in text:
        c = ord(t)
        if c == 32:
            decipher = 32
        elif c >= 48 and c <= 57:
            decipher = c - shift
            if decipher < 48:
                decipher += 10
        elif c >= 65 and c <= 90:
            decipher = c - shift
            if decipher < 65:
                decipher += 26
        elif c >= 97 and c <= 122:
            decipher = c - shift
            if decipher < 97:
                decipher += 26
        print("{:c}".format(decipher), end='')
    print()

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
