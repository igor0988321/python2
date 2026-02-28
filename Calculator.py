def decor():
    print("**************************")

print("Welcome to the calculator")
decor()
while True:
        a = input(
        "Сhoose the action you want to perform: + - to add \n - - minus \n * - to multiply \n / - to divide \n ** - raise to a power ")
        decor()
        b = int(input("Enter the first number"))
        decor()
        c = int(input("Enter the second number"))
        decor()

        if a == "+":
            print(f"Your number: {b + c} ")
            decor()
        elif a == "-":
            print(f"Your number: {b - c} ")
            decor()
        elif a == "*":
            print(f"Your number: {b * c} ")
            decor()
        elif a == "/":
            if c != 0:
                print(f"Your number: {b / c} ")
                decor()
            else:
                print("Error: Division by zero!")
                decor()
        elif a == "**":
            print(f"Your number: {b ** c} ")
            decor()

        d = input("Do you want to stay on the calculator?  Yes or No ")
        decor()
        if d == "Yes" or d == 'yes':
           pass
        else:
            print("Thank you for using calculator \n Goodbye")
            decor()
            break

