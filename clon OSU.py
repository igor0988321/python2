import pygame
import random

pygame.init()


screen = pygame.display.set_mode((600,400))

dots = [[random.randint(50, 550), random.randint(50, 350)] for j in range(6) ]
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()

            for dot in dots:
                if (dot[0] - mx)**2 + (dot[1]- my)**2 < 20**2:
                    dot[0] = random.randint(50, 550)
                    dot[1] = random.randint(50, 350)

    screen.fill((30,30,30))
    for dot in dots:
        pygame.draw.circle(screen, (240,240,240), dot, 20)

    pygame.display.flip()
