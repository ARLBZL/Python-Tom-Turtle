from turtle import *
tom = Turtle()
tom.speed(0)
tom.width(1)

n=3

while True:
    for i in range(n):
        tom.forward(n)
        tom.left(360/n)
    tom.right(n)
    n+=1
