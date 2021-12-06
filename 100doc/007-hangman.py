#!/usr/bin/env python3

import random
import string
from hangman_ascii import title ,hangman
from hangman_list import words
import os

# Generates (choose) a random word
word = random.choice(words)
word = word.lower()
word_len = len(word)

# print ascii art for game name
print(title)


# creates a list to fill with the user input letters
# print one underscore by each letter of the random word
hang_list = list("_" * word_len)
for h in hang_list:
    print(h, end=' ')
print()

# convert word in list
word_as_list = list(word)

# prompt to the user to enter a letter

countdown = word_len
life = 6 # number of lives, fixed, 2 arms, 2 legs, body, and head

'''
    print an empty handman
    ask user for a letter, if the letter is in the word, then replace
    the underscore with matching letter
'''
while (countdown > 0):
    print(hangman[life])
    letter = input("Guess a letter: ")
    os.system("clear")
    letter = letter.lower()
    if letter in hang_list:
        print("You already has typed the {:s} letter".format(letter))
    for i in range(word_len):
        w = word_as_list[i]
        eval = letter in w
        if eval == True:
            if hang_list[i] != letter:
                hang_list[i] = letter
                countdown -= 1
            else:
                break
            print("You match the letter: {:s}".format(letter))
    if letter not in word_as_list:
        print("You guess : {:s}, that's not in the word. You loose a life!".format(letter))
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
