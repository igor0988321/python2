password = input("Chek PW: ")

is_long = len(password) >= 8
has_upper = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

if is_long and has_upper and has_number and has_special:
    print("Strong PW")

elif is_long and (has_upper or has_number or has_special):
    missing = []
    if not has_upper:
        missing.append('uppercase')
    if not has_number:
        missing.append('number')
    if not has_special:
        missing.append('special char')
    print(f"PW Missing: {', '.join(missing)}")
else:
    print("Weak PW")