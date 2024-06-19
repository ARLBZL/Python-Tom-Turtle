from turtle import *
tom = Turtle()
tom.color('black')
tom.speed(0)
tom.width(5)
n = 3

while n <= 10:
    for flower in range(n):
        for draw in range(n):
            tom.forward(100)
            tom.right(360/n)
        tom.right(360/n)
    n += 1
    
