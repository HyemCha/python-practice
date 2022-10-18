import turtle

myT = None

myT = turtle.Turtle()
myT.shape('classic')

for i in range(4):
    myT.forward(200)
    myT.right(90)

myT.done()