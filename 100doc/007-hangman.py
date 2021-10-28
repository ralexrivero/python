import random
import string


# Generates (choose) a random word
words = ["advark", "baboon", "apple"]
word = random.choice(words)
word = word.lower()
word_len = len(word)

# creates a list to fill with the user input letters
# print one underscore by each letter of the random word
hang_list = list("_ " * word_len)
for h in hang_list:
    print(h, end='')
print()

# convert word in list
word_as_list = list(word)
print(word_as_list)

# prompt to the user to enter a letter


letter = input("Guess a letter: ")
letter = letter.lower()
print(word_len)
for w in word_as_list:
    eval = letter in w
    if eval == True:
        print(w, end=' ')
        word_len -= 1
    else:
        print("_ ", end='')
        word_len -= 1


# print debugging information
print('\n', word, word_len, letter)