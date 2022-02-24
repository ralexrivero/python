"""Do something while condition is true"""
import turtle
import time


turtle.color("blue")
turtle.bgcolor("white")
turtle.shape("circle")
turtle.pensize(5)

n = int(input("How much long do you want the line?"))
while n >= 0:
    turtle.forward(1)
    n -= 1
time.sleep(5)
