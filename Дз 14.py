# nums = input("Введіть вираз: ")
#
# num1 = ""
# num2 = ""
# o = ""
#
#
# for a in nums:
#     if a == "+" or a == "-" or a == "*" or a == "/":
#         o = a
#     elif o == "":
#         num1 += a
#     else:
#         num2 += a
#
# a = int(num1)
# b = int(num2)
#
# if o == "+":
#     res = a + b
# elif o == "-":
#     res = a - b
# elif o == "*":
#     res = a * b
# elif o == "/":
#     res = a / b
#
# print("Результат:", res)


text = input("Enter a sentence: ")
reserv = ["Step", "IT", "Name" , "Ukraine"]
new_text = ""
words = text.split()
for word in words:
    replaced = False
    for r in reserv:
        if word == r:
            new_text += word.upper() + " "
            replaced = True
        if replaced == False:
            new_text += word + " "
print(new_text)

