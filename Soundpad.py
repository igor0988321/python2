from playsound import playsound
import os

while True:
    choice = input('1/2:')

    if choice == '1':
        playsound('1.mp')
    elif choice == '2':
        playsound('2.mp3')
    else:
        pass

    os.system('cls')


