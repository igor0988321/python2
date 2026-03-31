import random
import os
import time

field = [['_' for _ in range(3)] for _ in range(3)]


good = [(random.randint(0,2), random.randint(0,2)) for i in range(3)]

for i in range(3):
    os.system('cls')
    for row in field:
        print(row)

    y,x = map(int, input().split())
    if (y,x) in good:
        print("Find")
        field[y][x] = 'X'
    else:
        print("Not Find")
        field[y][x] = '#'
        time.sleep(1.5)