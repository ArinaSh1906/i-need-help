# class
class Car:
    # attributes (fields, properties) - переменные внутри объекта/класса
    model = 'toyota'
    color = 'black'
    number = 'ABC 123'
    engine_type = 'electric'

    # method - функции внутри объекта/класса
    def info(self):
        # self - ссылка на объект, из которого вызывали метод
        print(f'{self.color} {self.model}, № {self.number}')

    @staticmethod
    def i_am_car():
        print('i am a car')


if __name__ == '__main__':
    # objects (instances)
    car1 = Car()
    car2 = Car()
    print(car1)
    print(car2)

    car1.model = 'volvo'
    print(car1.model)
    print(car2.model)
    print(Car.model)

    car1.info()
    car2.info()
    Car.info(car1)
    Car.i_am_car()





