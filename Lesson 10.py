# c = 0
# for n in range(50000):
#     n1 = n % 10
#     n2 = n // 10 % 10
#     n3 = n // 100 % 10
#     n4 = n // 1000 % 10
#     n5 = n // 10000 % 10
#     if (n1 == 4 or n2 == 4 or n3 == 4 or n4 == 4 or n5 == 4 or
#             n5 == 1 and n4 == 3 or n4 == 1 and n3 == 3 or n3 == 1 and n2 == 3 or n2 == 1 and n1 == 3):
#         c += 1
# print(c)
import math

# n = 5
# for k in range(3):
#     for i in range(k+3):
#         for j in range(n - 1 - i - k + 2):
#             print(" ", end='')
#         for j in range(2*k + 2*i + 1):
#             if (j == 0 or j == 2*k + 2*i) and i == k + 2 or k == 0 and i == 0:
#                 print("#", end='')
#             else:
#                 print("*", end='')
#         print()

#
# R = 3
# r = 1
# h = 1
# c = 0
# for i in range(-R, R, h):
#     for j in range(-R, R, h):
#        l = math.sqrt(i*i + j*j)
#        if l > r and l < R:
#            c += 1
# print(c)