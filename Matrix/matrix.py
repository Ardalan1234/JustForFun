import pygame
import sys
import string
import random

WIDTH = 1920
HEIGHT = 1080
BLOCK_SIZE = 15

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
# RAINBOW[Block.n % len(RAINBOW)] -> this is how you can use the RAINBOW color as an argument
RAINBOW = [
    (255, 0, 0),  # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (127, 255, 0),  # Greenish Yellow
    (0, 255, 0),  # Green
    (0, 255, 127),  # Spring Green
    (0, 255, 255),  # Cyan
    (0, 127, 255),  # Sky Blue
    (0, 0, 255),  # Blue
    (127, 0, 255),  # Purple
    (255, 0, 255)  # Magenta
]

LETTERS = string.ascii_letters + string.digits + string.punctuation
FONT_SIZE = 20

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
FONT = pygame.font.SysFont('terminal', FONT_SIZE)
clock = pygame.time.Clock()


class Block:
    n = 0

    def __init__(self, x, y, speed, color, last):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.interval = random.randint(5, 30)
        self.char = random.choice(LETTERS)
        self.color = WHITE if last else self.color  # RAINBOW[Block.i % len(RAINBOW)]
        Block.n += 1

    def draw(self, window):
        self.y = self.y + self.speed if self.y < HEIGHT else -BLOCK_SIZE
        frames = pygame.time.get_ticks()
        if not frames % self.interval:
            self.char = random.choice(LETTERS)
        label = FONT.render(self.char, True, self.color)
        window.blit(label, (self.x, self.y))


class Column:
    def __init__(self, x, y):
        self.height = random.randint(10, 30)
        self.speed = random.randint(5, 10)
        self.blocks = [
            Block(x=x, y=i, speed=self.speed, color=GREEN, last=True if i == y else False)
            for i in range(y, y - BLOCK_SIZE * self.height, -BLOCK_SIZE)
        ]

    def draw(self, window):
        for block in self.blocks:
            block.draw(window)


def main(window):
    columns = [Column(x=x, y=random.randint(-HEIGHT, 0)) for x in range(0, WIDTH, BLOCK_SIZE)]
    while True:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
        for col in columns:
            col.draw(window)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main(screen)
