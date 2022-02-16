
def fib(n):
    """print fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


"""call the function fib"""

fib(2000)
