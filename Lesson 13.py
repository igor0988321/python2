import string

# st = "hello python"
# for s in st:
#     print(s)
#
# print(st[2])

# l = [1, 2, 3]

# print(st.upper())
# print(st.lower())
# print(st.find("o34"))
# print(st.rfind("o"))
# print(st.index("o"))
# print(" + ".join([str(i) for i in l]))
# print(st.zfill(20))
# print(st.ljust(20, '+'), end='')
# print(st.rjust(20, '+'))
# print(st.center(20, '+'))
# print(st.title())
# print(st.capitalize())
# print("3".islower())
# print("30000".endswith("01"))
# print("30000".startswith("30"))
# print("30000".count("0"))
# print("30000".replace("0", "A"))
# print("mama myla ramu".split('a'))
# print("   mama myla ramu  ".strip())

# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.printable)

# print(chr(97))
# print(ord('b'))

# print(st[2:6])

# st = "Bingle bongle dingle dangle, yickedy doo, yickedy da, lippy-tappy-too-ta!"
# s = st.split()
# s1 = s[1] + " " + s[0]
# print(s1)

# print(" ".join(reversed(st.split())))

# print(len(st.split()))

# words = st.split()
# maxLen = 0
# for s in words:
#     if len(s) > maxLen:
#         maxLen = len(s)
#         w = s
# print(w)


# words = st.split()
# for j in range(len(words) - 1):
#     for i in range(len(words) - 1 - j):
#         if len(words[i]) > len(words[i+1]):
#             words[i], words[i + 1] = words[i + 1],  words[i]
#
# print(words)


# Є деякий текст. Реалізуйте таку функціональність
# Змінити текст таким чином, щоб кожне речення починалося з великої літери;
# Порахуйте скільки разів цифри зустрічаються в тексті;
# Порахуйте скільки разів розділові знаки зустрічаються в тексті;  (,.!?:;)
# Порахуйте кількість знаків оклику в тексті.

# print(string.punctuation)
#
#
# st = "Користувач вводить333 з клавіатури рядок. перевірте чи є введений рядок паліндромом. Паліндром — слово або текст, що читається однаково зліва направо і справа наліво."
# rech = st.split(".")
# rech = [r.strip().capitalize()+"." for r in rech]
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