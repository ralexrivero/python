
s = "\U000025A1"  # unicode square
t = "\U00002217"  # unicode triangle

row1 = [s, s, s]
row2 = [s, s, s]
row3 = [s, s, s]

map = [row1, row2, row3]
print("{}\n{}\n{}".format(map[0], map[1], map[2]))

position = int(input("Where do you want to put the treasure?\n\
    enter two digits: column and row. i.e. 23\n"))

col = int(position / 10)
row = position % 10

map[row - 1][col - 1] = t

print("{}\n{}\n{}".format(map[0], map[1], map[2]))
