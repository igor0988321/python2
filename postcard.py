word = input("Enter your word: ")

for y in range(12, -12, -1):
    for x in range(-30, 30):
        formula = (
            (x * 0.05) ** 2 +
            (y * 0.1) ** 2 - 1
        ) ** 3 - (
            (x * 0.05) ** 2
        ) * (
            (y * 0.1) ** 3
        )

        if formula <= 0:
            print(
                word[(x - y) % len(word)],
                end=""
            )
        else:
            print(" ", end="")

    print()
