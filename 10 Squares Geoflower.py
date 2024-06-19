from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.speed(0)

for i in range(10):
    for i in range(4):
        tom.forward(100)
        tom.left(90)
    tom.left(360/10)
