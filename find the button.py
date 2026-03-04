import tkinter as tk
import random


def replace_button():
    button_to_find.place(
        x=random.randint(0, 250),
        y=random.randint(0, 250),
        width=50,
        height=50
    )


root = tk.Tk()
root.geometry('300x300')
root.title('Find the Button')
root.resizable(False, False)
root.config(
    background='green'
)


button_to_find = tk.Button(
    root,
    background='green',
    borderwidth=0,
    command=replace_button,

)


# button_to_find.place(
#     x = random.randint(0,250),
#     y = random.randint(0,250),
#     width = 50,
#     height = 50
# )

replace_button()

root.mainloop()