import random

letters = 'qwertyuiopasdfghjklzxcvbnm123456789!@#$%^&*?'

while True:

    input()
    print('You password:', ''.join([random.choice(letters) for _ in range(10)]))
