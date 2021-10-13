# odd or even number

for x in range(1, 10):
    if (x % 2 == 0):
        print("{:d} is even".format(x))
        continue
    print("{:d} is odd".format(x))