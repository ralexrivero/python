#!/usr/bin/env python3

import random
import string
from hangman_ascii import title, hangman
from hangman_list import words, a, b
import os


# Generates (choose) a random word
word = random.choice(words)  # choose random word
word_clean = word.lower()  # original word in lowercase
word_translated = str.maketrans(a, b)  # clean characters
word_clean.translate(word_translated)
word_len = len(word_clean)

# print ascii art for game name
print(title)


# creates a list to fill with the user input letters
# print one underscore by each letter of the random word
hang_list = list("_" * word_len)

# convert word in list
word_as_list = list(word_clean)

"""
Automatically match the spaces when is more than one word
"""
space = ' '
for i in range(word_len):
        w = word_as_list[i]
        eval = space in w
        if eval is True:
            hang_list[i] = space

# print the underscores for the word(s)
for h in hang_list:
    print(h, end=' ')
print()

# prompt to the user to enter a letter

countdown = word_len
life = 6  # number of lives, fixed, 2 arms, 2 legs, body, and head
black_list = []


def display_black_list():
    """
    display the list of wrong letters to avoid by the user
    """
    print("\nBlack list: ", end='')
    for i in black_list:
        print("{:s} ".format(i),end="")
    print()


'''
    print an empty handman
    ask user for a letter, if the letter is in the word, then replace
    the underscore with matching letter
'''
while (countdown > 0):
    display_black_list()
    print( hangman[life])
    letter = input("Guess a letter: ")
    os.system("clear")
    letter = letter.lower()
    if letter in hang_list:
        print("You already has typed the {:s} letter".format(letter))
    for i in range(word_len):
        w = word_as_list[i]
        eval = letter in w
        if eval is True:
            if hang_list[i] != letter:
                hang_list[i] = letter
                countdown -= 1
            else:
                break
            print("You match the letter: {:s}\n".format(letter))
    if letter not in word_as_list:
        print("You guess : {:s}, that's not in the word. You loose a life!\n"
              .format(letter))
        black_list.append(letter)
        life -= 1
        if life == 0:
            print(hangman[0])
            print("You lose!")
            break
    for h in hang_list:
        print(h, end=' ')
    print()

''' if the letter is not in the word, then decrease the life by 1 '''
if countdown == 0 and life > 0:
    print("You win!")

print("The word to guess: {:s}".format(word))

# print("countdown: {:d}, life: {:d}".format(countdown, life))
