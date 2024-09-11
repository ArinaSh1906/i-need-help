import pygame as pg
from board import Board
from element import Element


WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
SQUARE_LENGTH = 25

SQUARES_X = 10
SQUARES_Y = 20

FPS = 60


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode(SIZE)
        self.board = Board(
            (WIDTH - SQUARE_LENGTH * SQUARES_X) // 2,
            (HEIGHT - SQUARE_LENGTH * SQUARES_Y) // 2,
            SQUARE_LENGTH,
            SQUARES_X,
            SQUARES_Y
        )
        self.clock = pg.time.Clock()

    def mainloop(self):
        while True:
            # обработка событий
            events = pg.event.get()
            for event in events:
                # если тип события...
                if event.type == pg.QUIT:
                    return
            # основные действия
            self.main_actions()

            # draw
            self.draw()

            # time tick
            self.clock.tick(FPS)

    def main_actions(self):
        self.board.update()

    def draw(self):
        self.screen.fill('black')
        self.board.draw(self.screen)
        pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.mainloop()
