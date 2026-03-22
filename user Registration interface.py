name = input("Enter Your name:")
email = input("Enter Your email:")
password = input("Enter Your password:")
skill = input("Enter Your skill:")
education = input("Enter Your education:")
no = input("Enter Your no:")

user_input = {
    'Name': name,
    'Email': email,
    'Password': password,
    'Skill': skill,
    'Education': education,
    'Phone No': no,
}

for i, j in user_input.items():
    print(i, j)