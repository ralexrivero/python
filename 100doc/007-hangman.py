import random
import string


# Generates a random word
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
while word_as_list:
    letter = input("Guess a letter: ")
    letter = letter.lower()
    if word_as_list.index(letter) >= 0:
        hang_list[word_as_list.index(letter), letter]
        word_as_list[word_as_list.index(letter)] = '*'
    else:
        print("Bad")
    for h in hang_list:
        print(h, end='')
    print()

# print debugging information
print(word, word_len, letter)