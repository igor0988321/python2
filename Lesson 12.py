# Користувач з клавіатури вводить список чисел. Необхідно знайти суму всіх додатних чисел у списку. Результат вивести на екран.
import random
# l = 10
# nums = [random.randint(-5, 5) for i in range(l)]
# print(nums)
# # s = sum([el for el in nums if el > 0])
# s = [i for i in range(len(nums)) if nums[i] % 2 == 0]
# print(s)
# un = set(nums)
# print(un)
# # sum, max, min, len


# l = 10
# nums = [random.randint(-5, 5) for i in range(l)]
# print(nums)
# for i in range(len(nums) // 2):
#     nums[i], nums[l-1-i] = nums[l-1-i], nums[i]
# print(nums)

h = 10
temp = [random.randint(1, 2000) for i in range(h)]
# print(temp)
# for i in range(25):
#     for t in range(24):
#         if 25-i > temp[t]:
#             print("  ", end='')
#         else:
#             print("* ", end='')
#     print()

# maxDelta = 0
# for i in range(h-1):
#     delta = abs(temp[i+1] - temp[i])
#     if delta > maxDelta:
#         maxDelta = delta
#         h1 = i
# print(h1, maxDelta)

# maxDelta = 0
# for i in range(h-1):
#     delta = temp[i+1] - temp[i]
#     if delta < maxDelta:
#         maxDelta = delta
#         h1 = i
# print(h1, maxDelta)

# step = 0
# for j in range(len(temp)-1):
#     for i in range(len(temp)-1-j):
#         if temp[i] < temp[i+1]:
#             temp[i], temp[i+1] = temp[i+1], temp[i]
#             step += 1
#
#
# print(step)

# l = [[2,3,5], [2,1,4], [6,8,6]]
#
# for i in range(len(l)):
#     s = 0
#     for j in range(len(l[i])):
#         print(l[i][j], end=' ')
#         s += l[i][j]
#     print(" | ", s)
#     # print()