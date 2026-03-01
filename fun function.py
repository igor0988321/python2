# create a function that accepts a string and
# returns letters in the following format:

# print(letters("Hello"))
# print(letters("Banana"))
# print(letters("ahahahahaha"))
#
# Result:
# HeLlO
# BaNaNa
# AhAhAhAhAhA

def letters(text):
    result = ""
    for index, letter in enumerate(text):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()

    return result

print(letters("Hello"))
print(letters("Banana"))
print(letters("ahahahahaha"))



