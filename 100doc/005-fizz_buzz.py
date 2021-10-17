for i in range(1, 101):
    if i % 15 == 0:
        m = "FizzBuzz"
    elif i % 3 == 0:
        m = "Fizz"
    elif i % 5 == 0:
        m = "Buzz"
    else:
        m = i
    print(m, end=' ')
print()