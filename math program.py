import tkinter as tk
import random


action = ["+", "-", "*", "/"]
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
act = random.choice(action)

ex = f"{num1} {act} {num2}"
res = eval(ex)

def view():
    global res
    if res == int(result.get()):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        act = random.choice(action)

        ex = f"{num1} {act} {num2}"
        res = eval(ex)
        example["text"] = ex
    else:
        pass


root = tk.Tk()
root.geometry('250x300')
root.resizable(False, False)

example = tk.Label(
    root,
    text=ex,
    font="Calibri 40"
)
example.pack(pady=10)

result = tk.Entry(
    root,
    font="Arial 30",
    justify="center"
)
result.pack()

btn = tk.Button(
    root,
    font="Arial 20",
    text="verify",
    command = view
)
btn.pack()


root.mainloop()