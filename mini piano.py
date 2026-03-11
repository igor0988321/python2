import tkinter as tk
import winsound


def btn1_key():
    winsound.Beep(100, 500)

def btn2_key():
    winsound.Beep(500, 500)

def btn3_key():
    winsound.Beep(1000, 500)


window = tk.Tk()
window.geometry('300x200')
window.title('Mini piano')

btn1 = tk.Button(
    window,
    text='1',
    font="Calibri 20",
    background="white",
    command=btn1_key
)
btn1.pack(
    fill='x',
)

btn2 = tk.Button(
    window,
    text='2',
    font="Calibri 20",
    background="white",
    command = btn2_key
)
btn2.pack(
    fill='x',
)

btn3 = tk.Button(
    window,
    text='3',
    font="Calibri 20",
    background="white",
    command = btn3_key
)
btn3.pack(
    fill='x',
)


window.mainloop()