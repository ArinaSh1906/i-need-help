import os
import random
import time

import keyboard


class Car:
    def __init__(self, max_speed=180):
        # self.speed = 0  # public attribute
        # self._speed = 0  # protected attribute доступ только у этого класса и наследующих его классов
        self.__speed = 0  # private attribute доступ только внутри этого класса
        self.__max_speed = max_speed

    # getter
    def get_speed(self):
        return self.__speed

    def __accelerate__(self):
        if keyboard.is_pressed('up') and self.__speed < self.__max_speed:
            self.__speed += 1
        elif self.__speed > 0 and not keyboard.is_pressed('up'):
            self.__speed -= 1

    def __decelerate__(self):
        if keyboard.is_pressed('down') and self.__speed > 0:
            self.__speed -= 1

    def update(self):
        self.__accelerate__()
        self.__decelerate__()
        print(f'Текущая скорость: {self.__speed}')
        time.sleep(0.1)
        os.system('cls')

    def simulate(self):
        while True:
            self.update()
            if keyboard.is_pressed('escape'):
                return


if __name__ == '__main__':
    car1 = Car()
    # car1.simulate()
    while True:
        car1.update()
        car1.__speed = random.randint(1, 1000)
        # car1._Car__speed = random.randint(1, 1000)
        if keyboard.is_pressed('escape'):
            break
