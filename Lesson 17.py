# f = open("test.txt", "w")
# f.write("Hello Python!")
# f.write("Hello Python!\n")
# f = open("test.txt", "w", encoding='utf-8' )
# f.write("Слава Україні!")
# f.close()







#
# f = open("test.txt", "r")
# s = f.read(5)
# print(s)
# s = f.read()
# print(s)
#
# s = f.readlines()
# print(s)
# s = f.readline()
# print(s)
# f.close()
import random



#
# arr = [random.randint(1, 20) for i in range(10)]
# print(arr)
# f = open("arr.txt", "w")
# f.write(" ".join([str(i) for i in arr]))
# f.close()
#
#
# f = open("arr.txt", "r")
# s = f.read().split()
# # arr = [int(i) for i in s]
# arr = list(map(int,s))
#
# f.close()
#
# arr2 = [i for i in arr if i % 2 == 0]
# f = open("arr2.txt", "w")
# f.write(" ".join([str(i) for i in arr2]))
# print(arr2)
# f.close()
# print(arr[1])


# s.strip('[').rstrip(']').split(', ')
#
# f = open("test1.txt", "r")
# lines = f.readlines()
# print(len(lines))
# words = 0
# symbol = 0
# for l in lines:
#     words += len(l.split())
#     symbol += sum(map(len, l.split()))
# print(symbol)
# print(words)
#
# f.close()
#
# def square(a):
#     return a * a
#
# arr = [random.randint(1, 5) for i in range(5)]
# print(arr)
# arr3 = list(map(square, arr))
# print(arr3)

# Шифр Цезаря
s = "mama"
m = ""
n = 3
for i in s:
    m += chr(ord(i) + n)

print(m)



