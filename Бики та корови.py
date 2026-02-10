import random
random_number_to_guess = str(random.randint(1000,9999))
def entering_number():
    while True:
        number = 'abcd'
        try:
            number = input('Ведіть значення з 4 цифір: ')
            if number.isdigit() and len(number) == 4:
                return number
        except ValueError:
            print("Хибне ведення даних:")



while True:
    right_place_and_number = 0
    right_number_and_wrong_place = 0
    number = entering_number()
    if number == random_number_to_guess:
        print("Ви вгадали /n Вітаю з перемогою!!!" )
        break
    else:
        for j in range(4):
            if number[j] == random_number_to_guess[j]:
                right_place_and_number += 1
            if number[j] in random_number_to_guess:
                right_number_and_wrong_place += 1
        print(f"Ви вгадали {right_number_and_wrong_place} цифр і {right_place_and_number} із них на правильній позиціЇ ")






