import random


rand_num = random.seed(int(input("Enter a random value: ")))

nameAsCSV = input("Give me everybody's names, separated by ', '\n")
name = nameAsCSV.split(", ")
print("{:}".format(name))

banker = random.choice(name)
print("{:s} is going to pay the bill today!".format(banker))
