"""Use a for loop instead of max()"""

score = input("Type the scores: ").split()
high = 0

for s in score:
    if int(s) > int(high):
        high = s
print(high)

""" high_max = max(score)
print(high_max) """