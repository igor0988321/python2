import pygame
import random

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Random Dice Generation")





clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    x = random.randint(0, 450 )
    y = random.randint(0, 450)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


    pygame.draw.rect(
        window,
        (r, g, b),
        (x, y, 50, 50,),

    )
    pygame.display.update()
    clock.tick(40)