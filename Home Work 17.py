# Напишіть програму, яка запитує в користувача три рядки і записує їх у файл data.txt,
# кожен рядок має бути записаний на новому рядку.

# f = open("data.txt","w")
# for i in range(1, 4):
#     text = input(f"Enter a number {i}: ")
#     f.write(f"{text}\n")
#     s = text
#     print(s)
# f.close()






# Напишіть програму, яка читає файл data.txt, фільтрує рядки, що містять слово "Python",
# і записує їх у новий файл filtered.txt.


# f = open("data.txt", "r")
# d = open("filtered.txt", "w")
# for line in f:
#     if "Python" in line:
#         d.write(line)
# f.close()
# d.close()

#
# Напишіть програму, яка запитує в користувача ім('я файлу, ''відкриває його,
# видаляє всі цифри з вмісту і зберігає результат у новому файлі cleaned.txt.)

# fname = input("Enter file name: ")
# d = open(fname, "r")
# text = d.read()
# d.close()
# clean_text = 0
# for i in text:
#     if not i.isdigit():
#         clean_text += i
#
# ff = open("cleaned.txt", "w")
# ff.write(clean_text)
# ff.close()






# Напишіть програму, яка читає файл data.txt, інвертує порядок рядків і зберігає результат у новому файлі reversed.txt.
# Наприклад, якщо data.txt містить:
# Перший рядок
# Другий рядок
# Третій рядок
# Після виконання програми reversed.txt має містити:
# Третій рядок
# Другий рядок
# Перший рядок



# f = open("data.txt", 'r')
# lines = f.readlines()
# f.close()
#
# f = open("reversed.txt", "w")
# f.writelines(lines[::-1])
# f.close()