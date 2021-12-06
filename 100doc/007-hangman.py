#!/usr/bin/env python3

import random
import string

# hangman ascii art
hangman = ['''
      _______
     |/      |
     |      (_)
     |      /|\\
     |       |
     |      / \\
     |
 ____|___
''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
 ____|___
''', '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |
     |
 ____|___
''', '''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |
     |
 ____|___
''', '''
      _______
     |/      |
     |      (_)
     |       |
     |       |
     |
     |
 ____|___
''', '''
      _______
     |/      |
     |      (_)
     |
     |
     |
     |
 ____|___
''', '''
      _______
     |/      |
     |
     |
     |
     |
     |
 ____|___
 ''']


# Generates (choose) a random word
words = ["Uruguay", "Argentina", "Brasil", "Chile", "Colombia", "Venezuela", "Ecuador"]
word = random.choice(words)
word = word.lower()
word_len = len(word)

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
    letter = letter.lower()
    for i in range(word_len):
        w = word_as_list[i]
        eval = letter in w
        if eval == True:
            if hang_list[i] != letter:
                hang_list[i] = letter
                countdown -= 1
            else:
                break
    if letter not in word_as_list:
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
