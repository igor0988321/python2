balance = 3000

while True:
    print("-----ATM MENU-----")
    print("1. Check balance : ")
    print("2. Deposite : ")
    print("3. Withdraw :")
    print("4. Exit :")

    user_choice = input("Enter your choice (1,4):")
    if user_choice == '1':
        print(balance)
    elif user_choice == '2':
        amount = int(input("Enter your amount:"))
        if amount > 0:
            balance += amount
            print("Amount deposit successfully!")
        else:
            print("Invalid amount : ")
    elif user_choice == '3':
        amount = int(input("Enter amount to Withdraw:"))
        if amount > balance:
            print('insufficient balance :')
        elif amount <= 0:
            print("Invalid amount : ")
        else:
            balance -= amount
            print("Amount withdraw successfully!")
    elif user_choice == '4':
        print('Thank You : ')
        break
    else:
        print("Invalid choice. please try again. ")
