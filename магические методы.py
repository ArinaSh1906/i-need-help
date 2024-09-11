from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if type(numerator) is not int or type(denominator) is not int:
            raise ValueError('числитель и знаменатель должны быть int')
        elif denominator == 0:
            raise ZeroDivisionError('в знаменателе не может стоять 0')
        self.__num = numerator
        self.__den = denominator
        if self.__den < 0:
            self.__den = abs(self.__den)  # модуль
            self.__num *= -1

        self.__reduce_fraction__()

    @staticmethod
    def __get_result__(result):
        if result.__den == 1:
            return result.__num
        return result

    def get_num(self):
        return self.__num

    def get_den(self):
        return self.__den

    # magic methods
    def __str__(self):
        return f'{self.__num}/{self.__den}'

    def __int__(self):
        return self.__num // self.__den

    def __float__(self):
        return self.__num / self.__den

    def __mul__(self, other):
        if type(other) is Fraction:
            return Fraction.__get_result__(Fraction(self.__num * other.__num, self.__den * other.__den))
        elif type(other) is int:
            return Fraction.__get_result__(Fraction(self.__num * other, self.__den))
        else:
            raise TypeError('Дробь можно умножить только на другую дробь или целое число.')

    def __rmul__(self, other):  # 7 * 1/4
        if type(other) is int:
            return self.__mul__(other)
        else:
            raise TypeError('Дробь можно умножить только на другую дробь или целое число.')

    # add, sub, truediv
    def __add__(self, other):  # сложение
        if type(other) is Fraction:
            return Fraction(self.__num * other.__den + other.__num * self.__den, self.__den * other.__den)
        elif type(other) is int:
            return Fraction.__get_result__(Fraction(self.__num + other * self.__den, self.__den))
        else:
            raise TypeError('К дроби можно прибавить только другую дробь или целое число.')

    def __radd__(self, other):
        if type(other) is int:
            return self.__add__(other)
        else:
            raise TypeError('К дроби можно прибавить только другую дробь или целое число.')

    def __sub__(self, other):  # subtraction вычитание
        if type(other) is Fraction:
            return Fraction(self.__num * other.__den - other.__num * self.__den, self.__den * other.__den)
        elif type(other) is int:
            return Fraction.__get_result__(Fraction(self.__num - other * self.__den, self.__den))
        else:
            raise TypeError('Из дроби можно вычесть только другую дробь или целое число.')

    def __rsub__(self, other):
        if type(other) is int:
            return self.__sub__(other)
        else:
            raise TypeError('Из дроби можно вычесть только другую дробь или целое число.')

    def __truediv__(self, other):
        if type(other) is Fraction:
            return Fraction(self.__num * other.__den, self.__den * other.__num)
        elif type(other) is int:
            return Fraction.__get_result__(Fraction(self.__num, self.__den * other))
        else:
            raise TypeError('Дробь можно разделить только на другую дробь или целое число.')

    def __rtruediv__(self, other):
        if type(other) is int:
            return self.__truediv__(other)
        else:
            raise TypeError('Дробь можно разделить только на другую дробь или целое число.')

    def __eq__(self, other):
        if type(other) is Fraction:
            return self.__num * other.__den == other.__num * self.__den
        elif type(other) is int:
            return Fraction.__get_result__(self.__num == other * self.__den)
        else:
            raise TypeError('Дробь можно сравнить только с другой дробью или целым числом')

    # ne, gt, lt, ge, le
    def __ne__(self, other):
        if type(other) is Fraction:
            return self.__num * other.__den != other.__num * self.__den
        elif type(other) is int:
            return Fraction.__get_result__(self.__num != other * self.__den)
        else:
            raise TypeError('Дробь можно сравнить только с другой дробью или целым числом')

    def __gt__(self, other):
        if type(other) is Fraction:
            return self.__num * other.__den > other.__num * self.__den
        elif type(other) is int:
            return Fraction.__get_result__(self.__num > other * self.__den)
        else:
            raise TypeError('Дробь можно сравнить только с другой дробью или целым числом')

    def __lt__(self, other):
        if type(other) is Fraction:
            return self.__num * other.__den < other.__num * self.__den
        elif type(other) is int:
            return Fraction.__get_result__(self.__num < other * self.__den)
        else:
            raise TypeError('Дробь можно сравнить только с другой дробью или целым числом')

    def __ge__(self, other):
        if type(other) is Fraction:
            return self.__num * other.__den >= other.__num * self.__den
        elif type(other) is int:
            return Fraction.__get_result__(self.__num >= other * self.__den)
        else:
            raise TypeError('Дробь можно сравнить только с другой дробью или целым числом')

    def __le__(self, other):
        if type(other) is Fraction:
            return self.__num * other.__den <= other.__num * self.__den
        elif type(other) is int:
            return Fraction.__get_result__(self.__num <= other * self.__den)
        else:
            raise TypeError('Дробь можно сравнить только с другой дробью или целым числом')

    # reduction
    def __reduce_fraction__(self):
        gcd_ = gcd(self.__num, self.__den)
        self.__num = self.__num // gcd_
        self.__den = self.__den // gcd_

    # def __pow__(self, power):

    # Hе подходят для дробей, но очень полезные
    # __len__, __new__, __del__, __contains__


if __name__ == '__main__':
    f1 = Fraction(1, 6)
    f2 = Fraction(5, 7)
    # f1 *= f2
    print(f2 * f1)
    a = 5
    a *= f1
    print(a)
