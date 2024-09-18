import pygame as pg
from constants import ELEMENT_COORDS, ELEMENT_COLORS, ELEMENTS
import random


class Element:
    def __init__(self, fall_speed=60, move_speed=5):
        self.figure = random.choice(ELEMENTS)
        original_coords: list[list[int]] = ELEMENT_COORDS[self.figure]
        self.coordinates = []
        for coord in original_coords:
            self.coordinates.append(coord.copy())
        self.fall_speed = fall_speed
        self.move_speed = move_speed
        self.active = True
        self.frame_counter = 1
        self.color = ELEMENT_COLORS[self.figure]
        # self.board = Board()

    def update(self, free_squares):
        if self.active:
            if self.frame_counter % self.move_speed == 0:
                self.move(free_squares)
            if self.frame_counter % self.fall_speed == 0 and self.active:
                self.fall(free_squares)
            self.frame_counter += 1

    def fall(self, free_squares):
        # сюда проверку на свободную клетку
        for x, y in self.coordinates:
            if y == 19 or not free_squares[y + 1][x]:
                self.active = False
                return
        for element in self.coordinates:
            element[1] += 1

    def move(self, free_squares):
        # сюда проверку на свободную клетку

        can_move_left = True
        can_move_right = True
        can_move_down = True
        buttons = pg.key.get_pressed()

        # проверить, можем ли двигаться в выбранном направлении
        for x, y in self.coordinates:
            if x == 0 or not free_squares[y][x - 1]:
                can_move_left = False

            if x == 9 or not free_squares[y][x + 1]:
                can_move_right = False

            if y == 19 or not free_squares[y + 1][x]:
                can_move_down = False
                self.active = False

        for element in self.coordinates:
            if buttons[pg.K_LEFT] and can_move_left:
                element[0] -= 1
            if buttons[pg.K_RIGHT] and can_move_right:
                element[0] += 1
            if buttons[pg.K_DOWN] and can_move_down:
                element[1] += 1

    def draw(self, screen, squares):
        # рисовать элемент
        for x, y in self.coordinates:
            pg.draw.rect(screen, self.color, squares[y][x])
