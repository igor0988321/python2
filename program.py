def celsius_in_farenhean(c):
    return c * 9 / 5 + 32

def farenheit_in_celsius(f):
    return (f - 32)* 5 / 9

def km_in_ml(km):
    return km * 0.621371

def ml_in_km(ml):
    return ml * 1.609344

def kg_in_funt(kg):
    return kg * 2.20462

def funt_in_kg(funt):
    return funt * 0.453592

print("unit converter")
print("1 - temperature")
print("2 - length")
print("3 - weight")
print("0 - exit")

while True:
    a = input("Enter: ")

    if a == "0":
        print("Goodbye")
        break
    elif a == "1":
        print("1 - Celsius in Farenheit")
        print("2 - Farenheit in Celsius")
        b = input("Enter: ")

        if b == "1":
            num = float(input("Enter celsius: "))
            res = celsius_in_farenhean(num)
            print(num , "degrees Celsius = ", res, "degrees Farenheit")

        elif b == "2":
            num = float(input("Enter farenheit: "))
            res = farenheit_in_celsius(num)
            print(num, "degrees Farenheit = ", res, "degrees Celsius")

        else:
            print("Invalid input")

    elif a == "2":
        print("1 - km in mil")
        print("2 - mil in km")
        b = input("Enter: ")

        if b == "1":
            num = float(input("Enter km : "))
            res = km_in_ml(num)
            print(num, "km = ", res, "mil")

        elif b == "2":
            num = float(input("Enter ml: "))
            res = ml_in_km(num)
            print(num, "ml= ", res, "km")
        else:
            print("Invalid input")

    elif a == "3":
        print("1 - kg in funt")
        print("2 - funt in kg")
        b = input("Enter: ")

        if b == "1":
            num = float(input("Enter kg: "))
            res = kg_in_funt(num)
            print(num, "kg= ", res, "funt")

        elif b == "2":
            num = float(input("Enter funt: "))
            res = funt_in_kg(num)
            print(num , "funt= ", res, "kg")
        else:
            print("Invalid input")

    else:
        print("Invalid input")
