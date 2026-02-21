# def factorial(n):
#     f = 1
#     for i in range(1, n+1):
#         f *= i
#     return f
#
# # print(factorial(5))
#
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n * fact(n-1)
#
# # print(fact(5))
#
# def num(n):
#     print(n, end=' ')
#     if n > 1:
#         num(n-1)

# num(5)
# print()

# def num1(n):
#     if n > 1:
#         num1(n-1)
#     print(n, end=' ')
#
# # num1(5)
#
# def pow(a, n):
#     if n == 0:
#         return 1
#     return a * pow(a, n-1)
#
# # print(pow(2,  2))
#
#
# def sum(a, b):
#     if a == b:
#         return b
#     return a + sum(a+1, b)
#
# print(sum(1, 10))
#
#
# def count(n):
#     if n == 0:
#         return 0
#     return n%10 + count(n//10)
#
# print(count(3751))