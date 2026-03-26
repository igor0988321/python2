file = open("user.txt", 'r')
text =  file.read()
file.close()
if text == "":

    name = input("Enter your name: ")

    print("Hello", name)


    file = open("user.txt", 'w')
    file.write(name)
    file.close()
else:
    print("Hello", text)