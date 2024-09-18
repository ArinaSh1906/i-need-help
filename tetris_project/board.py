import pygame as pg
from element import Element


class Board:
    def __init__(self, x: int, y: int, square_length: int, width: int, height: int):
        self.width = width
        self.height = height
        self.rect = pg.Rect(x, y, square_length * self.width, square_length * self.height)
        self.square_length = square_length
        self.squares = self.create_squares()
        self.free_squares = self.create_free_squares()
        # debug
        self.element = Element()
        self.old_elements = []

    def create_squares(self):
        squares = []
        for y in range(self.height):
            squares.append([])
            for x in range(self.width):
                square_x = self.rect.x + self.square_length * x
                square_y = self.rect.y + self.square_length * y
                squares[-1].append(pg.Rect(square_x, square_y, self.square_length, self.square_length))
        return squares

    def create_free_squares(self) -> list[list[bool]]:
        free_squares = []
        for y in range(self.height):
            free_squares.append([True])
            for x in range(self.width):
                free_squares[-1].append(True)
        return free_squares

    def draw(self, screen):
        self.element.draw(screen, self.squares)
        # рисовать старые элементы
        for element in self.old_elements:
            element.draw(screen, self.squares)

        for y in range(self.height):  # y - номер ряда (индекс списка в board1)
            for x in range(self.width):  # x - номер клетки в этом ряду
                pg.draw.rect(screen, 'white', self.squares[y][x], 1)

    def update(self):
        self.element.update(self.free_squares)
        if not self.element.active:
            for x, y in self.element.coordinates:
                self.free_squares[y][x] = False
                # print(x, y, self.free_squares[y][x])

            self.old_elements.append(self.element)
            self.element = Element()
