zmist = {
    "Ведення": 2,
    "Завантаження редактора": 6,
    "Функції, змінні": 12,
    "Типи данних": 13,
    "Перевірки": 16
}

# print(zmist["Завантаження редактора"])

# print(max(zmist, key=len))

max_str = max(zmist, key=len)

for key in zmist:
    print(key,
          "." * (10 + len(max_str) - len(key)),
          zmist[key]
    )

