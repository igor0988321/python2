import string
# st = "Hello python"
# for s in st:
#     print(s)
#
# l = [1, 2, 3]
# print(st[2])
# print(st.upper())
# print(st.lower())
# print(st.find(""))
# # print(st.replace(""))
# print(st.index(""))
# print(" + ".join([str (i) for i in l]))
# print(st.zfill(20))
# print(st.ljust(20))
# print(st.rjust(20))
# print(st.center(20))
# print(st.title())
# print(st.capitalize())
# print(st.islower())
# print(st.endswith())
# print(st.startswith())
# print(st.count(""))
# print(st.replace("python", ""))
# print(st.split())
# print(st.strip())

# print(string.digits)
# print(chr(97))
# print(ord('b'))
# print(st[2:6])


# st = "Ruslan Karnaukh , mmm , s , ss"
# s = st.split()
# s1 = s[1] + " " + s[0]
# print(s1)

# print(" ".join(reversed(st.split())))

# print(len(st.split()))

# words = st.split()
# lenMax = 0
# for s in words:
#     if len(s) > lenMax:
#         lenMax = len(s)
#         w = s
#
# print(w)
# words = st.split()
# for j in range(len(words)- 1):
#     for i in range(len(words) - 1 - j):
#         if len(words[i]) > len(words[i + 1]):
#             words[i], words[i + j] = words[i + 1], words[i]
#
#
#
# print(words)

#
# st = "Повний текст гімну:Щене вмерла Україна, і слава, і воля,Ще нам, браття молодії, усміхнеться доля.Згинуть наші вороженьки, як роса на сонці,Запануєм і ми, браття, у своїй сторонці."
# rech = st.split(".")
# rech = [r.strip().capitalize() + "." for r in rech]
# st1 = " ".join(rech)
# print(st1)
#
# count = 0
# for s in st:
#     if s.isdigit():
#         count += 1
# print(count)
#
# c1 = 0
# for s in string.punctuation:
#     c1 += st.count(s)
# print(c1)