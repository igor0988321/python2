import pygame
import random

pygame.init()

window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

x = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    x += 1

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


    pygame.draw.rect(
        window,
        (r, g, b),
        (x, 0, 10, 500)
    )

    pygame.display.update()
    clock.tick(60)