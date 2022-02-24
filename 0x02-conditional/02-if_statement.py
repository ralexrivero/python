#!/usr/bin/env python3
""" if and elif """


def checks(is_magician, is_expert):
    """
        Defines the player status
    """
    if is_magician and is_expert:
        print('You are a master magician')
    elif is_magician and not is_expert:
        print('At least you\'re getting there')
    else:
        print('You need more magic')


checks(True, True)
checks(True, False)
checks(False, True)
checks(False, False)
