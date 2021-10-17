user_range = input("Type a range: (space separated values: start, end, [step]):\n").split()
numbers = []

for u in range(0, len(user_range)):
    user_range[u] = int(user_range[u])
if len(user_range) == 2:
    user_range.append(1)

for n in range(user_range[0], user_range[1], user_range[2]):
    numbers.append(n)

print("\nvalues: {:d}\nminimum value: {:d}\nmaximum value: {:d}\nacumulated value:{:d}".format(len(numbers),min(numbers), max(numbers), sum(numbers)))