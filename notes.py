import tkinter as tk

def on_text_write(x):
    file = open("notes.txt", 'w')
    file.write(notes.get("0.0", "end"))
    file.close()

window = tk.Tk()
window.title("Notes")
window.geometry("500x500")

notes = tk.Text(
    window,
    font="Arial 20",
    background="black",
    foreground="#0f0",
)
notes.place(x = 0 ,
    y = 0,
    width = 500,
    height = 500
)

notes.bind("<Key>", on_text_write)

window.mainloop()