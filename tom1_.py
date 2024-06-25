from turtle import *
tom = Turtle()
tom.shape('turtle')
tom.color('green')
tom.speed(0)
tom.penup()
tom.goto(-200,-200)
tom.pendown()
def I():
    tom.setheading(0)
    tom.fd(100)
    tom.bk(50)
    tom.lt(90)
    tom.fd(200)
    tom.lt(90)
    tom.fd(50)
    tom.bk(100)

def L():
    tom.setheading(0)
    tom.fd(100)
    tom.bk(100)
    tom.lt(90)
    tom.fd(200)

#Test 25/6/2024