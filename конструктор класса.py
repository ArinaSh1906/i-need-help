import random


# class
class Car:
    # attributes (fields, properties) - переменные внутри объекта/класса
    def __init__(self, model: str, number: str, color: str = 'blue') -> None:
        # конструктор класса вызывается в момент создания объекта
        self.model = model
        self.number = number
        self.color = color
        self.speed = 0

    # method - функции внутри объекта/класса
    def info(self) -> None:
        # self - ссылка на объект, из которого вызывали метод
        print(f'{self.color} {self.model}, № {self.number}')

    @staticmethod
    def i_am_car() -> None:
        print('i am a car')


class Ship:
    def __init__(self, name: str, people: int) -> None:
        self.name = name
        self.people = people

    def go_swimming(self) -> None:
        print(f'{self.name} отправился в плаванье.')

    def how_many_people(self) -> None:
        print(f'На борту корабля {self.name} находится {self.people} человек.')

    def stop_ship(self, time: int) -> None:
        print(f"Корабль '{self.name}' кинул якорь на {time} часов")


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def greeting(self):
        print(f"Привет, меня зовут {self.name}. Я в {self.grade} классе.")


class School:
    def __init__(self, name):
        self.name = name

    def school_greeting(self):
        print(f"Добро пожаловать в {self.name}!")


school = School("Школа №15")
school.school_greeting()
student = Student('Иван', 12, 6)
student.greeting()


class BadTeacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    @staticmethod
    def get_homework_assessment():
        print(f'Оценка за домашку: {random.randint(2, 5)}')


teacher = BadTeacher("Николай Иванович", 35, "Математика")
teacher.get_homework_assessment()
teacher.get_homework_assessment()
teacher.get_homework_assessment()


if __name__ == '__main__':
    # objects (instances)
    car1 = Car('toyota', 'ABC 123', 'black')
    car2 = Car('BMW', 'ARE 455')

    ship1 = Ship('Варяг', 200)

    car1.info()
    car2.info()

