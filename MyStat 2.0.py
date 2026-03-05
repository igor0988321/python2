# import random
#
# names = ["Яромил","Горигляд","Ярополк","Цвітан","Наслав","Іларіон","Йозеф","Худан","Щастибог"]
#
# f = open("st.txt", "w", encoding="utf-8")
#
# f.write("Ім*я       | Оцінки\n")
# f.write("---------------------------------------\n")
#
#
# for name in names:
#     marks = [str(random.randint(6,12)) for _ in range(random.randint(4, 8))]
#     f.write(f"{name:<12}| {' '.join(marks)}\n")
#
# f.close()
#
# students = {}
#
# f = open("students.txt", "r", encoding="utf-8")
# lines =  f.readlines()
# f.close()
#
# for line in lines[2:]:
#     if "|" in lines:
#         name, marks = line.split(" | ")
#         students[name.strip()] =  marks.strip().split()
#
# name = input("Ведіть ім*я студента:")
#
# if name in students:
#     print("Оцінки:", students[name])
#
#     add = input("Додати оцінку?")
#
#     if add.lower() == "так":
#         mark = input("Ведіть оцінку")
#         students[name].append(mark)
#
#     f = open("students.txt", "w", encoding="utf-8")
#
#     f.write("Ім*я:      | Оцінки\n")
#     f.write("------------------------\n")
#
#     for n,m in students.items():
#         f.write(f"{n:<12}| {' '.join(m)}\n")
#
#     f.close()
#     print("Всі оцінки студента:" , students[name])
# else:
#     print("Студента немає")