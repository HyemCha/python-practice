import multiprocessing
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

if __name__ == '__main__':
    car1 = RacingCar('@car1')
    car2 = RacingCar('#car2')
    car3 = RacingCar('$car3')

    car1.runCar()
    car2.runCar()
    car3.runCar()
    print('='*20)
    mp1 = multiprocessing.Process(target=car1.runCar)
    mp2 = multiprocessing.Process(target=car2.runCar)
    mp3 = multiprocessing.Process(target=car3.runCar)

    mp1.start()
    mp2.start()
    mp3.start()

    mp1.join()
    mp2.join()
    mp3.join()