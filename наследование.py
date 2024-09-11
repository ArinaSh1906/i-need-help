import pygame as pg
import random


clock = pg.time.Clock()
FPS = 60


class Sprite:
    def __init__(self, image: pg.Surface, x: int, y: int, speed: int):
        self.image = image
        self.speed = speed
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen: pg.Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Player(Sprite):
    def __init__(self, image: pg.Surface, x: int, y: int, speed: int, hp: int):
        # Sprite.__init__(self, image, x, y, speed)
        super().__init__(image, x, y, speed)
        self.hp = hp

    def move(self):
        buttons = pg.key.get_pressed()
        if buttons[pg.K_LEFT]:
            self.rect.x -= self.speed
        if buttons[pg.K_RIGHT]:
            self.rect.x += self.speed
        if buttons[pg.K_UP]:
            self.rect.y -= self.speed
        if buttons[pg.K_DOWN]:
            self.rect.y += self.speed


class Enemy(Sprite):
    def move(self):
        direction_list = ['left', 'right', 'up', 'down']
        direction = random.choice(direction_list)
        if direction == 'left':
            self.rect.x -= self.speed
        if direction == 'right':
            self.rect.x += self.speed
        if direction == 'up':
            self.rect.y -= self.speed
        if direction == 'down':
            self.rect.y += self.speed


class Projectile(Sprite):
    pass


if __name__ == '__main__':
    tree_image = pg.image.load('images/tree.png')
    tree_image = pg.transform.scale(tree_image, (200, 250))

    bear_image = pg.image.load('images/bear17.png')
    bear_image = pg.transform.scale(bear_image, (280, 240))

    bee_image = pg.image.load('images/bee.png')
    bee_image = pg.transform.scale(bee_image, (80, 80))

    tree1 = Sprite(tree_image, 0, 80, 0)
    tree2 = Sprite(tree_image, 450, 90, 0)

    bear = Player(bear_image, 250, 300, 1, 100)

    bee1 = Enemy(bee_image, random.randint(0, 570), random.randint(0, 570), 2)
    bee2 = Enemy(bee_image, random.randint(0, 570), random.randint(0, 570), 2)
    bee3 = Enemy(bee_image, random.randint(0, 570), random.randint(0, 570), 2)

    screen = pg.display.set_mode((650, 650))
    running = True
    while running:
        # обработка событий
        events = pg.event.get()
        for event in events:
            # если тип события...
            if event.type == pg.QUIT:
                running = False

        # движение
        bear.move()
        bee1.move()
        bee2.move()
        bee3.move()

        # отрисовка
        screen.fill('dark green')

        tree1.draw(screen)
        tree2.draw(screen)

        bear.draw(screen)

        bee1.draw(screen)
        bee2.draw(screen)
        bee3.draw(screen)

        pg.display.flip()
