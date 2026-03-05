import random
import os
import time



ones = [{'x': random.randint(0, 11),
         'y': random.randint(0,11)}
        for i in range(12)
]

while True:
    dis = [['0' for _ in range(12)] for _ in range(12)]
    for one in ones:
        dis[one['y']][one['y']] = '1'

        one['y'] += 1
        one['y'] %= 11

        for row in dis:
            print(' '.join(row))

        time.sleep(0.1)
        os.system('cls')