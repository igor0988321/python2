# Напишіть програму, яка об'єднує вміст кількох текстових
# файлів (file1.txt, file2.txt, file3.txt) в один файл
# merged.txt, додаючи перед вмістом кожного файлу його ім'я у
# вигляді заголовка.
import random

# file_list = ["file1.txt", "file2.txt", "file3.txt"]
#
#
# for file_name in file_list:
#     f = open(file_name, 'r', encoding="utf-8")
#     info = f.read()
#     f.close()
#     merged = open("merged.txt", "a", encoding="utf-8")
#     merged.write(file_name + '\n')
#     merged.write(info + '\n')
#     merged.close()


# week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
# f = open("log.txt", "w")
# for i in range(10000):
#     f.write("192.168.0." + str(random.randint(100, 255)) + " " + week[random.randint(0,6)] + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + " " +
#             str(random.randint(0, 23)).zfill(2) + "." + str(random.randint(0, 59)).zfill(2) + "\n")

# f = open("log.txt", 'r', encoding="utf-8")
# logList = [[l for l in line.replace('\n', '').split()] for line in f.readlines()]
# unique_ip = []
# for line in logList:
#     if line[0] not in unique_ip:
#         unique_ip.append(line[0])
#
# ip_list = [el[0] for el in logList]
# unique_ip = set(ip_list)
#
# maxCount = 0
# for ip in unique_ip:
#     count = ip_list.count(ip)
#     if count > maxCount:
#         maxCount = count
#         maxIP = ip
#
# print(maxIP, maxCount)
# f.close()
# f = open("log.txt", 'r', encoding="utf-8")
# info = f.read()
# week = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
# for d in week:
#     print(d, info.count(d))
#
#
# import datetime
#
# # d = datetime.datetime.now()
# # print(d)
#
# def deltatime(t1, t2):
#     h1, m1 = map(int, t1.split('.'))
#     h2, m2 = map(int, t2.split('.'))
#     dt1 = datetime.timedelta(hours=h1, minutes=m1)
#     dt2 = datetime.timedelta(hours=h2, minutes=m2)
#     if dt1 < dt2:
#         return dt2 - dt1
#     return datetime.timedelta(hours=24) - (dt1 - dt2)
#
#
# time = []
#
# for ip in unique_ip:
#     alltime = datetime.timedelta()
#     for line in logList:
#         if ip == line[0]:
#             alltime += deltatime(line[2], line[3])
#     time.append(alltime)
#
#
# print(list(unique_ip)[time.index(max(time))])
# print(time[time.index(max(time))])

# print(time)