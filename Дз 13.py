import random
from unittest import result

# Завдання 1
# Користувач з клавіатури вводить список цілих чисел.
# Необхідно визначити кількість елементів у списку, які більші за попередній елемент.
# Результат вивести на екран.
# l = 10
# s = 0
# nums = [random.randint(1,10) for i in range(l)]
# print(nums)
# for i in range(1, len(nums)):
#     if nums[i] > nums[i-1]:
#         s += 1
# print(s)


# Завдання 2
# Користувач вводить список цілих чисел. ]
# Необхідно вивести тільки ті елементи, які зустрічаються у списку рівно один раз,
# зберігаючи порядок їхньої появи.

# l = 10
# res = []
# s = 0
# nums = [random.randint(1,10) for i in range(l)]
# print(nums)
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if nums[i] == nums[j]:
#             s += 1
#         if s == 1:
#             res.append(nums[i])
# print(res)


# Завдання 3
# Користувач з клавіатури вводить список чисел. Необхідно знайти у списку найдовшу
# послідовність елементів, що зростають, і вивести її довжину та самі елементи.


# l = 10
# maxValue = 1
# minValue = 1
# ind = 0
# nums = [random.randint(1,10) for i in range(l)]
# print(nums)
# for i in range(len(nums)):
#     if nums[i] > nums[i - 1]:
#         minValue += 1
#     else:
#         maxValue = 1
#
#
#     if minValue > maxValue:
#         maxValue = minValue
#         ind = i
# start_ind = ind - maxValue + 1
# res = []
# for i in range(start_ind, start_ind + maxValue + 1):
#     res.append(nums[i])
# print(maxValue)
# print(res)

#
# Завдання 4
# Користувач із клавіатури вводить список цілих чисел.
# Необхідно реалізувати циклічний зсув списку вправо на N позицій. Результат вивести на екран.
#
# l = 10
# n = int(input(" n = "))
# res = []
# nums = [random.randint(1,10) for i in range(l)]
# print(nums)
# leng = len(nums)
# if leng != 0:
#     n = n % leng
# for i in range(leng):
#     index = i - n
#     if index < 0:
#         index = index + leng
#     res.append(nums[index])
# print(res)

# Завдання 6
# Користувач вводить список цілих чисел. Необхідно відсортувати список так, щоб числа чергувалися:
# спочатку найменше, потім найбільше, потім друге за величиною, друге за мінімальністю тощо.


# l = 10
# nums = [random.randint(1,10) for i in range(l)]
# print(nums)
# res = []
# nums = sorted(nums)
# left = 0
# right = len(nums)-1
# for i in range(len(nums)):
#     if i % 2 == 0:
#         res.append(nums[left])
#         left += 1
#     else:
#         res.append(nums[right])
#         right -= 1
# print(res)

