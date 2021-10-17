
s = "\U000025A1" #unicode square
t = "\U00002217" #unicode triangle

row1 = [s, s, s]
row2 = [s, s, s]
row3 = [s, s, s]

c3r3 = [row1, row2, row3]
print("{}\n{}\n{}".format(c3r3[0], c3r3[1], c3r3[2]))

position = int(input("Where do you want to put the treasure?\n\
    enter two digits: column and row. i.e. 23\n"))

col = int(position / 10)
row = position % 10

c3r3[row -1][col-1] = t

print("{}\n{}\n{}".format(c3r3[0], c3r3[1], c3r3[2]))
