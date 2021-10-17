"""Use a for loop instead of max()"""

score = input("Type the scores: ").split()
high = 0

for s in score:
    if int(s) > int(high):
        high = int(s)
print("The maximum score is: {:d}".format(high))

""" high_max = max(score)
print(high_max) """