import random
import string


# Generates (choose) a random word
words = ["advark", "baboon", "apple"]
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
print(word_as_list)

# prompt to the user to enter a letter

countdown = word_len
life = 6

while (countdown > 0):
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
    life -= 1
    if life == 0:
        print("You lose")
        break
    for h in hang_list:
        print(h, end=' ')
    print()
    if countdown <= 0:
        print("You win!")

print("countdown: {:d}, life: {:d}".format(countdown, life))
