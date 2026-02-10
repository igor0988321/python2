# Б
# n = 5
# for i in range(n):
#     for j in range(i + 1):
#          print("*", end=" ")
#     print()

# k
# n = 5
# for i in range(n):
#     for j in range(n - 1 - i):
#         print("  ", end='')
#     for j in range(i + 1):
#          print("*", end=" ")
#     print()

#
# u
# n = 5
# for i in range(n):
#     for j in range(n):
#         if j < (n - 1 - i):
#             print("*", end=" ")
#     print()


# n = 5
# for i in range(n):
#     for j in range(n):
#         if j <= i:
#             print("*", end=" ")
#     print()



# Г
# n = 7
# m = n // 2
# for i in range(n):
#     for j in range(n):
#         if i <= m and j >= m - i and j <= m + i:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# В
# n = 7
# m = n // 2
# for i in range(n):
#     for j in range(n):
#         if i >= m and j >= i - m and j <= n - 1 - (i - m):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# e
# n = 7
# m = n // 2
# for i in range(n):
#     for j in range(n):
#         if (i <= m and (j <= i or j >= n - 1 - i)) or  (i > m and (j <= n - 1 - i or j >= i)):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()



# д
# n = 7
# for i in range(n):
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()