import random


welcome = "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
choice = int(input(welcome))


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]
index = ["Rock", "Paper", "Scissors"]

""" for i in hands:
    print(i)
"""
print("You choose: {:s}".format(index[choice]))
print(hands[choice])

machine = random.randint(0, 2)
print("Machine choose: {:s}".format(index[machine]))
print(hands[machine])

"""Rules:machine
    (0)Rock wins against (2)scissors
    (2)Scissors wins against (1)paper
    (1)Paper wins against (0)rock"""

result = "You "

if choice == machine:
    result = "Draw"
elif choice == 0: #Rock
    if machine == 2:
        result += "win!"
    else:
        result += "lose"
elif choice == 1: #Paper
    if machine == 0:
        result += "win!"
    else:
        result += "lose"
elif choice == 2: #Scissors
    if machine == 0:
        result += "lose"
    else:
        result += "win!"

print("{}".format(result))