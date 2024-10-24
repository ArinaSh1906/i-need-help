import pygame as pg
from board import Board

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)
SQUARE_LENGTH = 25

SQUARES_X = 10
SQUARES_Y = 20

FPS = 60


class Game:
    def __init__(self):
        # pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode(SIZE)
        self.board = Board(
            (WIDTH - SQUARE_LENGTH * SQUARES_X) // 2,
            (HEIGHT - SQUARE_LENGTH * SQUARES_Y) // 2,
            SQUARE_LENGTH,
            SQUARES_X,
            SQUARES_Y
        )
        self.clock = pg.time.Clock()
        self.state = 'pause'
        self.frame_counter = 0
        self.time_counter = 0
        self.pause_font = pg.font.SysFont('bahnschrift', 80)
        self.pause_text = self.pause_font.render('PAUSE', True, 'white', 'black')
        self.game_font = pg.font.SysFont('bahnschrift', 24)
        self.time_text = self.game_font.render(f'time: {self.board.score_counter}', True, 'white')
        self.score_font = pg.font.SysFont('bahnschrift', 24)
        self.score_text = self.game_font.render(f'score: {self.board.score_counter}', True, 'white')

    def mainloop(self):
        while True:
            # обработка событий
            events = pg.event.get()
            for event in events:
                # если тип события...
                if event.type == pg.QUIT:
                    return
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        if self.state == 'pause':
                            self.state = 'play'
                        else:
                            self.state = 'pause'

            if self.state == 'pause':
                self.screen.blit(self.pause_text,
                                 (WIDTH // 2 - self.pause_text.get_width() // 2,
                                  HEIGHT // 2 - self.pause_text.get_height() // 2))
                pg.display.flip()

            elif self.state == 'play':
                self.play()

            elif self.state == 'game over':
                break

    def play(self):

        # основные действия
        self.main_actions()

        # draw
        self.draw()

        # time tick
        self.clock.tick(FPS)
        self.frame_counter += 1
        # print(self.frame_counter)
        if self.frame_counter == FPS:
            self.frame_counter = 0
            self.time_counter += 1
            self.time_text = self.game_font.render(f'time: {self.time_counter}', True, 'white')

        # score
        self.score_text = self.game_font.render(f'score: {self.board.score_counter}', True, 'white')

    def main_actions(self):
        self.board.update()
        if self.board.game_over:
            self.state = 'game over'

    def draw(self):
        self.screen.fill('black')
        self.board.draw(self.screen)
        time_text_x = self.board.rect.right + (WIDTH - self.board.rect.right) // 2 - self.time_text.get_width() // 2
        self.screen.blit(self.time_text, (time_text_x, HEIGHT - 80))
        score_text_x = self.board.rect.right + (WIDTH - self.board.rect.right) // 2 - self.time_text.get_width() // 2
        self.screen.blit(self.score_text, (score_text_x, HEIGHT - 110))
        pg.display.flip()


if __name__ == '__main__':
    game = Game()
    game.mainloop()
