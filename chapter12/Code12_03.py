class Car:
    color = ""
    speed = 0

    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    def upSpeed(self, value):
        self.speed += value

    def downSpeed(self, value):
        self.speed -= value

# main
myCar1 = Car("red", 30)
myCar2 = Car("blue", 60)

print("자동차1의 색상:", myCar1.color, "\t/ current speed:", myCar1.speed)
print("자동차2의 색상:", myCar2.color, "\t/ current speed:", myCar2.speed)
