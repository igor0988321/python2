strings = [
    "banana", "python",
    "lviv", "apple",
    "Paris"
]

# print(strings[1])

count = 0

for index in range(5):
    string = len(strings[index - 1])
    if index != 0:
        count += string

    print(" " * count + strings[index])