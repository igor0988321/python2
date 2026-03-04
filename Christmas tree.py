import tkinter as tk

def off_on_star():
    if star["foreground"] == 'green':
        star["foreground"] = 'yellow'
    else:
        star["foreground"] = 'green'


window = tk.Tk()
window.geometry("500x500")
window.title("Christmas Tree")
window.config(
    background = 'black'
)


star = tk.Label(
    window,
    text='*',
    font=('Consolas', 40),
    background='black',
    foreground='green'
)
star.pack()

tk.Label(
    window,
    text='***',
    font=('Consolas', 40),
    background='black',
    foreground='green'
).pack()

tk.Label(
    window,
    text='*****',
    font=('Consolas', 40),
    background='black',
    foreground='green'
).pack()


tk.Label(
    window,
    text='*******',
    font=('Consolas', 40),
    background='black',
    foreground='green'
).pack()

tk.Label(
    window,
    text='*********',
    font=('Consolas', 40),
    background='black',
    foreground='green'
).pack()

tk.Label(
    window,
    text=' ',
    font=('Consolas', 40),
    background='brown',
    foreground='green'
).pack()

tk.Button(
    window,
    text="Switch light",
    font=("Calibri", 35),
    background='white',
    foreground='lightgray',
    command=off_on_star
).pack()

window.mainloop()