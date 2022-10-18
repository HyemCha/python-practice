import turtle
import random

def mouseClick(x,y):
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r,g,b)
    tSize = random.randrange(0,10)
    turtle.shapesize(tSize)
    turtle.goto(x,y)
    print(r,g,b)

tSize = 5

turtle.shape('circle')
turtle.pensize(tSize)

turtle.onscreenclick(mouseClick, 1)

turtle.done()