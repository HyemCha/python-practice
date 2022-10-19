import math
import turtle
import random

curX, curY = 0,0
swidth, sheight = 1000, 1000
dist = 0

turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth, sheight)

turtles = []
for i in range(5):
    t = turtle.Turtle('turtle')
    r = random.random()
    g = random.random()
    b = random.random()
    size = random.randrange(1,100)/10
    angle = random.randrange(0,361)
    tX = random.randrange(-swidth/2, swidth/2)
    tY = random.randrange(-swidth/2, swidth/2)
    turtles.append([size, angle, tX, tY, r,g,b, t])
turtles.sort()
print(turtles)
curX = turtles[0][2]
curY = turtles[0][3]
for i in turtles:
    t = i[-1]
    t.turtlesize(i[0])
    t.pencolor(i[4], i[5], i[6])
    t.color(i[4], i[5], i[6])
    t.right(i[1])
    t.goto(i[2], i[3])
    t.pendown()
    t.stamp()
    # dist = math.pow((curX-turtle.xcor())**2 + (curY-turtle.ycor())**2)
    curX = t.xcor()
    curY = t.ycor()
turtle.done()