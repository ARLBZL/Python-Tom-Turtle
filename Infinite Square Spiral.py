from turtle import *
tom = Turtle()
tom.speed(0)
n = 1

while True:
    for square in range(4):
        tom.forward(n)
        tom.left(90)
    tom.right(5)
    n += 1
