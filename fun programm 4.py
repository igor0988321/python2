import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(500, 500)
screen.tracer(0)

# Черепашка для сетки
t = turtle.Turtle()
t.hideturtle()
t.color('green')


def draw_static_radar():
    t.clear()
    for r in [50, 100, 150, 200]:
        t.penup()
        t.goto(0, -r)
        t.pendown()
        t.circle(r)
    t.penup()
    t.goto(-200, 0)
    t.pendown()
    t.goto(200, 0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.goto(0, 200)


# Черепашка для луча и точек
beam = turtle.Turtle()
beam.hideturtle()

targets = [(random.randint(-150, 150), random.randint(-150, 150)) for _ in range(3)]
angle = 0

while True:
    draw_static_radar()  # Рисуем сетку
    beam.clear()

    # Рисуем луч
    rad = math.radians(angle)
    x = 200 * math.cos(rad)
    y = 200 * math.sin(rad)

    beam.color('lime')
    beam.width(3)
    beam.penup()
    beam.goto(0, 0)
    beam.pendown()
    beam.goto(x, y)

    # Проверяем цели
    for tx, ty in targets:
        # Исправленный atan2(y, x)
        target_angle = math.degrees(math.atan2(ty, tx))

        # Нормализуем текущий угол луча в диапазон -180...180
        current_beam_angle = ((angle + 180) % 360) - 180

        diff = abs(target_angle - current_beam_angle)
        if diff > 180: diff = 360 - diff

        if diff < 5:
            beam.penup()
            beam.goto(tx, ty)
            beam.dot(12, 'red')

    angle = (angle + 2) % 360
    screen.update()