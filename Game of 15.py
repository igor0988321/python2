import tkinter as tk
import random

root = tk.Tk()
root.title("Game of 15")

SIZE = 4
TITLE_SIZE = 100
numbers = list(range(1, SIZE*SIZE))
numbers.append(None)
random.shuffle(numbers)

empty_title_pos = numbers.index(None)

def move_title(index):
    global empty_title_pos
    if (abs(empty_title_pos - index) == 1 and empty_title_pos // SIZE == index // SIZE) or abs(empty_title_pos - index) == SIZE:
        numbers[empty_title_pos], numbers[index] = numbers[index], numbers[empty_title_pos]
        empty_title_pos = index
        update_buttons()


def update_buttons():
    for i, num in enumerate(numbers):
        if num is None:
            buttons[i].config(text="", state=tk.DISABLED)
        else:
            buttons[i].config(text=str(num), state=tk.NORMAL)


buttons = []

for i in range(SIZE*SIZE):
    btn = tk.Button(
        root,
        text="",
        height=2,
        width=4,
        font=("Arial", 24),
    )
    btn.grid(row=i//SIZE, column=i%SIZE)
    buttons.append(btn)

update_buttons()

root.mainloop()


