class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150

    def downSpeed(self, value):
        self.speed -= value

## main
myCar1 = Car()
myCar1.color = "red"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "blue"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "yellow"
myCar3.speed = 0

myCar1.upSpeed(30)
print("자동차1의 색상:", myCar1.color, "\t/ current speed:", myCar1.speed)

myCar2.upSpeed(60)
print("자동차2의 색상:", myCar2.color, "\t/ current speed:", myCar2.speed)

myCar3.upSpeed(155)
print("자동차3의 색상:", myCar3.color, "\t/ current speed:", myCar3.speed)
