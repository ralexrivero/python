print("Welcome to love calculator!")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name1_low = name1.lower()
name2_low = name2.lower()

word1 = "true"
word2 = "love"
dec, uni = 0, 0
message = ""

"""Evaluates first digit: decimal
    word 'true'
"""
for c in word1:
    dec += (name1_low.count(c) + name2_low.count(c))
"""Evaluates second digit: units
    word 'love'
"""
for c in word2:
    uni += (name1_low.count(c) + name2_low.count(c))

score = dec * 10 + uni
if score < 10 or score > 90:
    message = ", you go together like coke and mentos."
elif score >= 40 and score <= 50:
    message = ", you are alright together."
print("Your score is {:d}{:s}".format(score, message))