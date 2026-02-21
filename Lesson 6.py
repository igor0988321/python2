# n1 = float(input(" 1 : "))
# n2 = float(input(" 2 : "))
# oper = input(" : ")
# res = 0
# if d == "+":
#     res = n1 + n2
#     print(res)
# elif d == "-":
#     res = n1 - n2
#     print(res)
# elif d == "*":
#     res = n1*n2
#     print(res)
# elif d == "/":
#     res = n1/n2
#     print(res)
# else:
#     print("")


# match oper:
#     case '+': res = n1 + n2
#     case '-': res = n1 - n2
#     case '*': res = n1 * n2
#     case '/': res = n1 / n2
#     case _: print("error")


# Локатор ориентирован на одну из сторон света («С» — север, «З» —
# запад, «Ю» — юг, «В» — восток) и может принимать три цифровые ко-
# манды поворота: 1 — поворот налево, –1 — поворот направо, 2 — поворот
# на 180°. Дан символ C — исходная ориентация локатора и целые числа N1
# и N2 — две посланные команды. Вывести ориентацию локатора после вы-
# полнения этих команд.



# pos = input()
# com1 = int(input())
# com2 = int(input())

# if pos == 'n':
#     dir = 0
# elif pos == 'e':
#     dir = 1
# elif pos == 's':
#     dir = 2
# elif pos == 'w':
#     dir = 3
#
# dir += com1
# dir += com2
#
# dir %= 4
#
# if dir == 0:
#     pos = 'n'
# elif dir == 1:
#     pos = 'e'
# elif dir == 2:
#     pos = 's'
# elif dir == 3:
#     pos = 'w'

# print(pos)


# Даны два целых числа: D (день) и M (месяц), определяющие правиль-
# ную дату невисокосного года. Вывести значения D и M для даты, наступної-
# для указанной.