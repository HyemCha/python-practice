import turtle

swidth, sheight = 1000, 300
currentX, currentY = 0, 0

turtle.title('거북이로 이진수 표현하기')
turtle.shape('turtle')
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.left(90)

n = int(input('숫자 : '))
b = bin(n)
currentX = swidth / 2
currentY = 0
print('b', len(b))
print('b', b)
for i in range(len(b) - 2):
    turtle.goto(currentX, currentY)
    if n & 1:
        turtle.color('red')
        turtle.turtlesize(2)
    else:
        turtle.color('blue')
        turtle.turtlesize(1)
    turtle.stamp()
    currentX -= 50
    n >>= 1

turtle.done()