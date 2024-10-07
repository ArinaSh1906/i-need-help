import pygame as pg
from constants import ELEMENT_COORDS, ELEMENT_COLORS, ELEMENTS
import random


class Element:
    def __init__(self, fall_speed=60, move_speed=5):
        self.figure = random.choice(ELEMENTS)
        original_coords: list[list[int]] = ELEMENT_COORDS[self.figure]
        self.points = []
        self.center = [5, 1]
        for coord in original_coords:
            self.points.append(coord.copy())
        self.fall_speed = fall_speed
        self.move_speed = move_speed
        self.active = True
        self.frame_counter = 1
        self.color = ELEMENT_COLORS[self.figure]
        self.coordinates = self.update_coords()
        # self.board = Board()

    def update(self, occupied_squares):
        buttons = pg.key.get_pressed()
        if self.active:
            if self.frame_counter % self.move_speed == 0:
                self.move(occupied_squares)
                self.coordinates = self.update_coords()
            if self.frame_counter % self.fall_speed == 0 and self.active:
                self.fall(occupied_squares)
                self.coordinates = self.update_coords()
            if buttons[pg.K_UP] and self.frame_counter % 15 == 0:
                self.rotate(occupied_squares)
                self.coordinates = self.update_coords()
            self.frame_counter += 1

    def update_coords(self) -> list[list[int]]:
        # по центральной точке и координатам построить все точки
        new_coords = [self.center]
        for x, y in self.points:
            new_point = [self.center[0] + x, self.center[1] + y]
            new_coords.append(new_point)
        return new_coords

    def fall(self, occupied_squares):
        # сюда проверку на свободную клетку
        for x, y in self.coordinates:
            if y == 19 or occupied_squares[y + 1][x]:
                self.active = False
                return
        # for element in self.coordinates:
        #     element[1] += 1
        self.center[1] += 1

    def move(self, occupied_squares):
        # сюда проверку на свободную клетку

        can_move_left = True
        can_move_right = True
        can_move_down = True
        buttons = pg.key.get_pressed()

        # проверить, можем ли двигаться в выбранном направлении
        for x, y in self.coordinates:
            if x == 0 or occupied_squares[y][x - 1]:
                can_move_left = False

            if x == 9 or occupied_squares[y][x + 1]:
                can_move_right = False

            if y == 19 or occupied_squares[y + 1][x]:
                can_move_down = False

        if buttons[pg.K_LEFT] and can_move_left:
            self.center[0] -= 1
        if buttons[pg.K_RIGHT] and can_move_right:
            self.center[0] += 1
        if buttons[pg.K_DOWN] and can_move_down:
            self.center[1] += 1

    def rotate(self, occupied_squares):
        if self.can_rotate(occupied_squares):
            for index in range(len(self.points)):
                point = self.points[index]
                point[0], point[1] = -point[1], point[0]

    def can_rotate(self, occupied_squares):
        for index in range(len(self.points)):
            point = self.points[index]
            new_x = self.center[0] - point[1]
            new_y = self.center[1] + point[0]
            if new_x > 9 or new_x < 0 or new_y > 19 or occupied_squares[new_y][new_x]:
                return False
        return True

    def draw(self, screen, squares):
        # рисовать элемент
        for x, y in self.coordinates:
            pg.draw.rect(screen, self.color, squares[y][x])
