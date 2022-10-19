import turtle

i, k, tX, tY = [0]*4
swith, sheight = 800, 450

turtle.title('거북 구구단')
turtle.shape('turtle')
turtle.setup(width=swith+50, height=sheight+50)
turtle.screensize(swith, sheight)
turtle.penup()
tX, tY = -500, 250

for i in range(1,10):
    for k in range(2, 10):
        turtle.goto(tX + 80 * k, tY - 40 * i)
        gugu = str(k) + ' x ' + str(i) + ' = ' + str(k*i)
        turtle.write(gugu, font=('Arial', 12, 'bold'))
turtle.done()