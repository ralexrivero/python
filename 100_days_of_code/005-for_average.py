values = input("Type some values: ").split()
x, total = 0, 0
"""Replace the sum(values) and len(values) by a for loop
"""
for v in values:
    v = float(v)
    x += 1
    total += v
average = total / x
print("The average of values is: {:.2f}".format(average))
