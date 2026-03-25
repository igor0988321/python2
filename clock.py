import tkinter as tk
import time

root = tk.Tk()

root.geometry("300x100")
text = tk.Label(root,
    font=("Arial", 40)
)
text.pack()
def a():
    s = time.strftime("%H:%M:%S")
    text.config(text=s)
    root.after(1, a)

a()

root.mainloop()