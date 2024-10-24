import pygame as pg
from element import Element
import random


class Board:
    def __init__(self, x: int, y: int, square_length: int, width: int, height: int):
        self.width = width
        self.height = height
        self.rect = pg.Rect(x, y, square_length * self.width, square_length * self.height)
        self.square_length = square_length
        self.squares = self.create_squares()
        self.occupied_squares = self.create_occupied_squares()
        # debug
        self.element = Element()
        # self.old_elements = []
        self.rows_to_delete = []
        self.score_counter = 0
        self.frame_counter = 0
        self.game_over = False

    def create_squares(self):
        squares = []
        for y in range(self.height):
            squares.append([])
            for x in range(self.width):
                square_x = self.rect.x + self.square_length * x
                square_y = self.rect.y + self.square_length * y
                squares[-1].append(pg.Rect(square_x, square_y, self.square_length, self.square_length))
        return squares

    def create_occupied_squares(self) -> list[list[bool]]:
        occupied_squares = []
        for y in range(self.height):
            occupied_squares.append([])
            for x in range(self.width):
                occupied_squares[-1].append(False)
        return occupied_squares

    def draw(self, screen):
        self.element.draw(screen, self.squares)
        # рисовать старые элементы
        # for element in self.old_elements:
        #     element.draw(screen, self.squares)

        for y in range(self.height):  # y - номер ряда (индекс списка в board1)
            color = random.randint(100, 255)
            for x in range(self.width):  # x - номер клетки в этом ряду
                if self.occupied_squares[y][x]:
                    pg.draw.rect(screen, self.occupied_squares[y][x], self.squares[y][x])
                if y in self.rows_to_delete:
                    # color = random.randint(100, 255)
                    pg.draw.rect(screen, (color, color, color), self.squares[y][x])
                pg.draw.rect(screen, 'white', self.squares[y][x], 1)

    def __element_move__(self):
        # обновление движения элемента
        self.element.update(self.occupied_squares)
        # если занял позицию
        if not self.element.active:
            for x, y in self.element.coordinates:
                if y == 0:
                    self.game_over = True
                    return
                self.occupied_squares[y][x] = self.element.color

            # self.old_elements.append(self.element)
            # проверить все ряды
            # формирование, какие рады удалять
            for index, row in enumerate(self.occupied_squares):
                if False not in row:
                    self.rows_to_delete.append(index)

            if not self.rows_to_delete:
                self.element = Element()

    def __delete_rows__(self):
        self.score_counter += len(self.rows_to_delete)

        # перед удалением - анимация
        while len(self.rows_to_delete) > 0:
            current_index = self.rows_to_delete.pop()

            # найти ближайший целый ряд
            for i in range(current_index - 1, -1, -1):
                if i not in self.rows_to_delete:
                    self.occupied_squares[current_index] = self.occupied_squares[i].copy()

                    self.rows_to_delete.append(i)
                    self.rows_to_delete.sort()

                    for x in range(len(self.occupied_squares[i])):
                        self.occupied_squares[i][x] = False
                    # print(i)

                    break

        # по current index определить, какие ряды пустые, и заполнить их (обновить)
        self.rows_to_delete = []

    def update(self):

        if not self.rows_to_delete:
            self.__element_move__()

        else:
            if self.frame_counter == 60:
                self.__delete_rows__()
                self.frame_counter = 0
                self.element = Element()

            else:
                self.frame_counter += 1
