for n in range(50, 100):
    for x in range(2, n):
        if n % x == 0:
            print("{:d} * {:d} = {:d}".format(x, int(n / x), n))
            break
    else:
        print("{:d} is prime".format(n))
