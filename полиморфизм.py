import random

import pygame as pg


WIDTH = 600
HEIGHT = 600


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, image: pg.Surface):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        buttons = pg.key.get_pressed()
        if buttons[pg.K_LEFT]:
            self.rect.x -= 1
        if buttons[pg.K_RIGHT]:
            self.rect.x += 1
        if buttons[pg.K_UP]:
            self.rect.y -= 1
        if buttons[pg.K_DOWN]:
            self.rect.y += 1


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((20, 20))
        self.rect = self.image.get_rect()
        self.image.fill('red')
        self.rect.x = random.randint(0, WIDTH - 20)
        self.rect.y = random.randint(0, WIDTH - 20)

    def move(self):
        direction = random.choice(('left', 'right', 'up', 'down'))
        match direction:
            case 'left':
                self.rect.x -= 1
            case 'right':
                self.rect.x += 1
            case 'up':
                self.rect.y -= 1
            case _:
                self.rect.y += 1


def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    group = pg.sprite.Group()

    bear_image = pg.image.load('images/bear17.png')
    bear_image = pg.transform.scale(bear_image, (140, 120))
    player = Player(230, 240, bear_image)
    group.add(player)

    for _ in range(11):
        group.add(Enemy())

    mainloop(group, screen)


def mainloop(group, screen):
    running = True
    while running:
        # обработка событий
        events = pg.event.get()
        for event in events:
            # если тип события...
            if event.type == pg.QUIT:
                running = False
        screen.fill('black')
        group.draw(screen)
        pg.display.flip()

        for sprite in group:
            sprite.move()


if __name__ == '__main__':
    main()
