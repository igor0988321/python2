classroom = [
    {'desk number': 1,
     'sitting': "Maxim"},
    {'desk number': 2,
     'sitting': "Ivan"},
    {'desk number': 3,
     'sitting': "Artem"},
    {'desk number': 4,
     'sitting': "Stas"},
    {'desk number': 5,
    'sitting': "Sasha"},
]

name = input("Enter your name: ")
for desk in classroom:
    if name == desk['sitting']:
        print(name, 'sits at', desk['desk number'], 'desk')