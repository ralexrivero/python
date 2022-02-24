#!/usr/bin/python3
import fibo

fibo.fib(1000)

fibo.fib2(100)

print("{}".format(fibo.__name__))

fib = fibo.fib

fib(500000)