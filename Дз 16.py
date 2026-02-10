# Напишіть функцію, що обчислює добуток елементів списку цілих. Список передається як параметр.
# Отриманий результат повертається з функції.

lists = [2,3,4]

def dobytok(lists):
    count = 1
    for i in lists:
        count *= i
    return count


d = dobytok(lists)
print(d)

# Напишіть функцію для знаходження мінімуму в списку цілих.
# Список передається як параметр. Отриманий результат повертається з функції.

my_list = [10,2,3,4,5]


def minn(my_list):
    min_value = min(my_list)
    print(min_value)

# minn(my_list)

# Напишіть функцію, що визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається з функції.

def neturalne(my_list):
    count = 0
    for i in my_list:
        if i >= 1 and i % 2 == 0:
            count += 1
        print(count)


# neturalne(my_list)


# Напишіть функцію, що видаляє зі списку цілих деяке задане число.
# З функції потрібно повернути кількість видалених елементів.

# a = int(input(" Число яке хочемо видалити:"))
def delete(my_list, a):
    count = 0
    while a in my_list:
        my_list.remove(a)
        count += 1
    return count

# print(my_list)
# delete(my_list, 3)
# print(my_list)

# Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]


def summ(list1, list2):
    print(list1 + list2)



# summ(list1, list2)


