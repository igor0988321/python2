# Guess the number game

import random
num1 = random.randint(1, 100)


while True:
    num2 = int(input("Enter a number between 1 and 100: "))
    if num2 > num1:
        print("Too much")
    elif num2 < num1:
        print("not enough")
    else:
        print("Congratulations, you guessed the number")
        break

# Even number filter
#
numbers = [1, 5, 8, 10, 13, 15, 20, 24, 27]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
       even_numbers.append(num)

print(even_numbers)

# ATM

balance = 1000

summ = int(input("Enter the amount you want to withdraw : "))
if summ > balance or summ == 0:
    print("Incorrect amount")
elif summ > balance:
    print("Insufficient funds")
elif summ % 10 == 0 and summ <= balance:
    # summ1 = summ - balance
    print(f"Issued: {summ} Remaining: {summ - balance}")
else:
    pass