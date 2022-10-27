class Car:
    name = ""
    speed = 0

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

# main
myCar1 = Car("고양이 전용 차", 30)
myCar2 = Car("volvo", 60)

print(f"{myCar1.name}의 현재 속도는 {myCar1.getSpeed()}")
print(f"{myCar2.name}의 현재 속도는 {myCar2.getSpeed()}")