#fibonacci series
print("Fibonacci series")
max = int(input("Enter a value: "))
a = 0
b = 1

for i in range(0, max):
    print("{:d}".format(b))
    a, b = b, a + b