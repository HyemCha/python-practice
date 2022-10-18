import turtle
import random

turtle.shape('turtle')

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r,g,b)
    turtle.right(143)
    turtle.forward(500)

turtle.done()