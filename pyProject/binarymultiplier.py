import turtle

def turtleStampByBinary(n,b):
    global curX, curY
    for i in range(len(b)-2):
        turtle.goto(curX, curY)
        if n & 1:
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50
        n >>= 1

swidth, sheight = 1500, 400
curX, curY = swidth/2, sheight/2

turtle.shape('turtle')
turtle.setup(width=swidth+30, height=sheight+30)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.left(90)

b1 = input('2진수:')
b2 = input('2진수:')

n1 = int(b1, 2)
n2 = int(b2, 2)
multiplyn = n1 | n2
multiplyb = bin(multiplyn)


for i in [n1,n2,multiplyn]:
    curX = swidth/2
    turtle.goto(curX, curY)
    turtleStampByBinary(i,bin(i))
    curY -= 50

turtle.done()