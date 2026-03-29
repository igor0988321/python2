import pygame
import random
import sys

pygame.init()

# Налаштування вікна
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Кольори
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Змінні гри
SIZE = 20
snake = [(100, 100), (80, 100), (60, 100)]  # Початкове тіло змії
clock = pygame.time.Clock()


# Функція для генерації їжі, кратної кроку змії
def get_random_food():
    x = random.randrange(0, WIDTH, SIZE)
    y = random.randrange(0, HEIGHT, SIZE)
    return (x, y)


food = get_random_food()
dx, dy = SIZE, 0  # Початковий рух праворуч

running = True
while running:
    # Контроль швидкості (FPS)
    clock.tick(10)

    # 1. Обробка подій
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Керування (запобігаємо розвороту на 180 градусів)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy == 0:
        dx, dy = 0, -SIZE
    elif keys[pygame.K_DOWN] and dy == 0:
        dx, dy = 0, SIZE
    elif keys[pygame.K_LEFT] and dx == 0:
        dx, dy = -SIZE, 0
    elif keys[pygame.K_RIGHT] and dx == 0:
        dx, dy = SIZE, 0

    # 3. Рух змії
    # Рахуємо нову голову: беремо старі координати x та y і додаємо зміщення
    new_head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, new_head)

    # 4. Перевірка на їжу
    # Використовуємо невеликий діапазон (Rect.colliderect), якщо координати не ідеальні,
    # але тут координати точні, тому просто порівнюємо.
    if snake[0] == food:
        food = get_random_food()
    else:
        snake.pop()  # Видаляємо хвіст, якщо не з'їли їжу

    # 5. Перевірка на програш (стіни або самоперетин)
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake[1:]):
        running = False

    # 6. Малювання
    screen.fill(WHITE)

    # Малюємо їжу
    pygame.draw.rect(screen, RED, (food[0], food[1], SIZE, SIZE))

    # Малюємо змію
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SIZE, SIZE))

    pygame.display.flip()

pygame.quit()
sys.exit()