#!/usr/bin/env python3

from caesar_cipher_ascii import title

"""
caesar cipher encode and decode for encrypt messages in ascii code
Displace the character the number of positions given by the user
    lowecase
    uppercase
    numbers
    space
"""


def secure_shift_n(shift):
    shift_n = shift
    while (shift_n > 10):
        shift_n = shift % 10
    return shift_n


def secure_shift_c(shift):
    shift_c = shift
    while (shift_c > 26):
        shift_c = shift % 26
    return shift_c


def caesar(direction, text, shift):
    """
    Encrypt and decrypt text and numbers using Caesar Cipher Encrypt.
    Direction stablish the type:
        encode = move to the right
        decode = move to the left
    text: the text to process
    shift: amount of position to move
    """
    shift_n = secure_shift_n(shift)
    shift_c = secure_shift_c(shift)

    if direction == "decode":
        sign = -1
    else:
        sign = 1
    for t in text:
        c = ord(t)
        if c == 32:
            cipher = 32
        elif c >= 48 and c <= 57:
            cipher = c + (sign * shift_n)
            if cipher > 57:
                cipher -= 10
            elif cipher < 48:
                cipher += 10
        elif c >= 65 and c <= 90:
            cipher = c + (sign * shift_c)
            if cipher > 90:
                cipher -= 26
            if cipher < 65:
                cipher += 26
        elif c >= 97 and c <= 122:
            cipher = c + (sign * shift_c)
            if cipher > 122:
                cipher -= 26
            elif cipher < 97:
                cipher += 26
        else:
            cipher = c
        print("{:c}".format(cipher), end='')
    print()

print(title)



run_again = True
while (run_again):
    """ Take input from the user """
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    """ Execute the encode or decode algorithm """
    caesar(direction, text, shift)

    """ Ask the user if want to cotinue """
    ask_continue = input("Type 'yes' to continue. Otherwise type 'no'\n")
    if ask_continue == "no":
        run_again = False
        print("Thanks! Take care, see you soon!\n")
