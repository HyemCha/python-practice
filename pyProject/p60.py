import turtle
import random

def rightBtnClick(x,y):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.shapesize(random.randrange(0,10))
    turtle.stamp()
    turtle.color(r,g,b)
    turtle.goto(x,y)

turtle.shape('turtle')
turtle.pensize(1)
turtle.onscreenclick(rightBtnClick, 3)

turtle.done()