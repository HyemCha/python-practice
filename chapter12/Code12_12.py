import threading
import time

class RacingCar:
    carName = ''

    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(0,3):
            carStr = self.carName + '~~run\n'
            print(carStr, end='')
            time.sleep(0.2)

car1 = RacingCar('@car1')
car2 = RacingCar('#car2')
car3 = RacingCar('$car3')

car1.runCar()
car2.runCar()
car3.runCar()
print('='*20)
th1 = threading.Thread(target=car1.runCar)
th2 = threading.Thread(target=car2.runCar)
th3 = threading.Thread(target=car3.runCar)

th1.start()
th2.start()
th3.start()