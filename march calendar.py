import calendar

march = calendar.month(2026, 3)
print(march.replace(" 8", "\33[31m8\33[0m"))


# print("\33[31m8\33[0m")