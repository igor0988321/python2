print(" WELLCOME TO OUR CAFE : ")

while True:
    print("Select items : ")

    items_name = {
        1 : "Milk Tea",
        2 : "Black Tea",
        3 : "Coffee",
        4 : "Lattee coffee",
        5 : "Green Tea"
    }

    for i ,j in items_name.items():
        print(i, j)

    select_items = input("Select the items : (1 , 5)  : " )
    if select_items == "1":
        print("You select Milk Tea")
    elif select_items == "2":
        print("You select Black Tea")
    elif select_items == "3":
        print("You select Coffee")
    elif select_items == "4":
        print("You select Lattee coffee")
    elif select_items == "5":
        print("You select Green Tea")
    else:
        print("invalid selection : Please try again : ")

    add_more_items = input(" If you want to add more items ! (yes/no) :").lower()
    if add_more_items == "yes":
        print(select_items)
    elif add_more_items == "no":
        print("Thank you")
        break
    else:
        print("invalid option . Please select a valid option :")