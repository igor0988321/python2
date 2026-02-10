# Завдання 4
# # Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри
# def symbol(a = 0, b = 0, c = 0, d = 0, e = 0):
#     if a < b:
#         return a
#     elif b < c:
#         return b
#     elif c < d:
#         return c
#     elif d < e:
#         return d
#     else:
#         return e
#
# print(symbol(10,-9,4,5,6))

#
# Завдання 2
# Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.

# def nums(a, b):
#     for i in range(min(a,b), max(a,b)+1):
#         if i % 2 == 0:
#             print(i)
#
# nums(10,25)

# Завдання 3
# Напишіть функцію, яка відображає порожній або заповнений квадрат з деякого символу. Функція приймає як параметри: довжину сторони квадрата, символ і змінну логічного типу:
# якщо вона дорівнює True, квадрат заповнений;
# якщо False, квадрат порожній.
# def square(size:int , symbol: int, boool: bool):
#     if boool:
#         for i in range(size):
#             print(symbol * size)
#     else:
#         print(symbol * size)
#         for i in range(size - 2):
#             print(symbol + " " * (size - 2) + symbol)
#         print(symbol * size)
#
# square(5, "*", True)
#
# square(5, "*", False)

#
# Завдання 5
# Напишіть функцію, яка рахує кількість цифр у числі. Число передається як параметр. З функції потрібно повернути отриману кількість цифр.
# Наприклад, якщо передали 3456, кількість цифр буде 4.
#
# def number(number):
#     count = 0
#     if number == 0:
#         return 1
#     while number > 0:
#         count += 1
#         number /= 10
#     return count
#
# print(number(123))
