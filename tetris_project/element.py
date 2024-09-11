import pygame as pg


class Element:
    def __init__(self, coordinates, color='yellow', fall_speed=60, move_speed=5):
        self.coordinates = coordinates
        self.fall_speed = fall_speed
        self.move_speed = move_speed
        self.active = True
        self.frame_counter = 1
        self.color = color
        # self.board = Board()

    def update(self):
        if self.active:
            if self.frame_counter % self.move_speed == 0:
                self.move()
            if self.frame_counter % self.fall_speed == 0 and self.active:
                self.fall()
            self.frame_counter += 1

    def fall(self):
        # сюда проверку на свободную клетку
        # for element in self.coordinates:
        #     if element
        for element in self.coordinates:
            element[1] += 1
            if element[1] == 19:
                self.active = False

    def move(self):
        # сюда проверку на свободную клетку

        can_move_left = True
        can_move_right = True
        can_move_down = True
        buttons = pg.key.get_pressed()
        # проверить, можем ли двигаться в выбранном направлении
        for element in self.coordinates:
            if element[0] == 0:
                can_move_left = False
            if element[0] == 9:
                can_move_right = False
            if element[1] == 19:
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
