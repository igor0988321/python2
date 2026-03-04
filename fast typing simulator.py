import time
import random
import os

words = ['apple', 'banana', 'python', 'keyboard', 'cloud', 'coffee']
input('Press enter to start the game')
start = time.time()
score = 0
while time.time() - start < 10:
    os.system('cls')
    print('Write: ', random.choice(words))
    input()
    score += 1

print("Your score is:", score)