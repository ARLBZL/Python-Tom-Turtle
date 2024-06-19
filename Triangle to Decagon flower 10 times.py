from turtle import *
tom = Turtle()
tom.speed(0)
n = 3

for increasenbyone in range(10):
    for flower in range(10):
        for draw in range(n):
            tom.forward(100)
            tom.right(360/n)
        tom.right(360/10)
    n += 1
    
