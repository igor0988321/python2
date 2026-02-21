import random

#
# def show(a, *args):
#     print(type(args))
#     print(a)
#     s = 0
#     for el in args:
#         s += el
#
# def boo(a, b=5):
#     return a + b
#
# # show(12,324,2345,345,67890)
# # print(boo(4, b=3))
#
# def foo(*args, **kwargs):
#     print(type(kwargs))
#     for key in kwargs:
#         print(f"Key - {key}, Value- {kwargs[key]}")


# foo(2, 4, c="mama", age=20, isDay=True)


# print(213,345,234,123,2134, "12e2")


# b = boo
# print(b(3,5))

#
# def printLine(symbol='*', count=10):
#     for i in range(count):
#         print(symbol, end='')
#     print()
#
# def func(method):
#     method()
#
# # func(printLine)
#
# def hello():
#     print("Hello")
#
# def goodbye():
#     print("Goodbye")


# message = hello
# message()
# message = goodbye
# message()
#
# message_list = [hello, goodbye]
# for f in message_list:
#     f()

# def asc(a, b):
#     return a > b
#
# def desc(a, b):
#     return a < b
#
# def evenFirst(a, b):
#     if a % 2 == 1 and b % 2 == 0:
#         return True
#     if a % 2 == 0 and b % 2 == 1:
#         return False
#     return asc(a, b)
#
#
# def lastDigit(a, b):
#     if a % 10 > b % 10:
#         return True
#     if a % 10 < b % 10:
#         return False
#     return asc(a, b)
#
#
# def bubble_sort(_list: list, method = asc):
#     for j in range(len(_list) - 1):
#         for i in range(len(_list) - 1 - j):
#             if method(_list[i], _list[i + 1]):
#                 _list[i], _list[i + 1] = _list[i + 1], _list[i]

# l = [random.randint(1, 100) for i in range(20)]
# print(l)
# bubble_sort(l, lastDigit)
# print(l)

#
# marks = [["Яромил"],["Горигляд"],["Ярополк"],["Цвітан"],["Наслав"],["Іларіон"],["Йозеф"],["Худан"],["Щастибог"]]
# for l in marks:
#     l.extend([random.randint(6, 12) for i in range(random.randint(4, 10))])
#
# # print(marks)
#
# def printStudent(marks):
#     for st in marks:
#         print(st[0].ljust(15), end='')
#         for i in range(1, len(st)):
#             print(str(st[i]).rjust(3), end=' ')
#         print()
#
# printStudent(marks)
#
#
# def indBestStudent(marks):
#     iBest = 0
#     avg = 0
#     for i in range(len(marks)):
#         s1 = sum(marks[i][1:]) / (len(marks[i]) - 1)
#         if s1 > avg:
#             iBest = i
#             avg = s1
#     return iBest
#
# print()
# print(marks[indBestStudent(marks)])