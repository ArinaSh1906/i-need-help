# import qrcode
#
#
# data = 'Hello, world!'
#
# qr = qrcode.QRCode(version=5, box_size=15, border=10)  # ???
#
# qr.add_data(data)
#
# img = qr.make_image(fill_color='red', back_color='black')
#
# img.save('test.png')


# for i in range(1, 11):
#     print(i)

# print([i for i in range(1, int(input()) + 1)])


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f'Book: {self.title} by {self.author}, published in {self.year}.')


class Car:
    def __init__(self, model: str, year: str, engine_running=False) -> None:
        self.model = model
        self.year = year
        self.engine_running = engine_running

    def start_car(self):
        self.engine_running = True
        print('Engine started')
        return self.engine_running

    def stop_car(self):
        self.engine_running = False
        print('Engine stopped')
        return self.engine_running

    def display_info(self):
        print(f'Model: {self.model}, Year: {self.year}, Engine Running: {"yes" if self.engine_running else "no"}')


class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(f'Его зовут {self.name}!')


class Cat(Animal):
    def __init__(self, name):
        # Animal.__init__(self, name)
        super().__init__(name)
        self.get_name()


class Lion(Cat):
    def __init__(self, name):
        super().__init__(name)

    # self.get_name()

    def play_game(self):
        print(f'{self.name} играет с едой.')


class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color


class Airplane(Transport):
    def __init__(self, speed, color):
        super().__init__(speed, color)

    def fly(self):
        print(f'{self.color} самолёт летит со скоростью {self.speed} км/ч')


# Вместо ... нужно дописать код

# Это класс работы с инвентарём.
# Его задача - хранить предметы и предоставлять методы для взаимодействия с ними.
# А именно, добавление и удаление предмета, сортировка всех предметов по алфавиту и демонстрация всех предметов рюкзака.
class Inventory:
    def __init__(self, *items: str) -> None:
        self.__items = list(items)

    # Сортирует инвентарь по алфавиту
    def sort_inventory(self) -> None:
        self.__items = sorted(self.__items)

    # Добавляет предмет в инвентарь
    def add_item(self, item: str) -> None:
        self.__items.append(item)
        print(f"Добавил {item} в инвентарь")

    # Удаляет предмет из инвентаря
    def remove_item(self, item: str) -> None:
        self.__items.remove(item)
        print(f"Вынул {item} из инвентаря")

    # Показывает весь инвентарь
    def show_items(self) -> None:
        print(f'В инвентаре такие предметы: ')
        for i in range(len(self.__items)):
            print(f"{i}. {self.__items[i]}")

    def get_item(self, item_index: int) -> str:
        return self.__items[item_index]


class Student:
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade

    def increase_grade(self):
        self._grade += 1
        print(f'{self.name} теперь в {self._grade} классе.')


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def set_balance(self, value):
        self.__balance = value

    # Продолжи писать решение тут
    def get_balance(self):
        return self.__balance

    def add(self, value):
        self.__balance += value

    def remove(self, value):
        if value > self.__balance:
            print("Ошибка: на счете недостаточно средств")
        else:
            self.__balance -= value
            return self.__balance


class Animal:
    def voice(self):
        print('Звуки молчания')


class Cat(Animal):
    def voice(self):
        print('Мяу, человек')


class Dog(Animal):
    def voice(self):
        print('Гав, дружище')


class Bull(Animal):
    def voice(self):
        print('Му, ты кто вообще')


cat1, cat2 = Cat(), Cat()
dog1, dog2 = Dog(), Dog()
bull1, bull2 = Bull(), Bull()

farm_band = [cat1, cat2, dog1, dog2, bull1, bull2]

# Исправь код ниже тоже
for pet in farm_band:
    pet.voice()
