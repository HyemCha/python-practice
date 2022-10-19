import random
import turtle

swidth, sheight = 500, 500
turtle.shape('turtle')
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight)
turtle.speed(10)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r,g,b)
    x = random.randrange(-(swidth/2), swidth)
    y = random.randrange(-(sheight/2), sheight)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    dist = random.randrange(10,200)
    for i in range(5):
        turtle.forward(dist)
        turtle.right(144)

turtle.done()