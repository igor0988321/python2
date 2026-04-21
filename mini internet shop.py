import tkinter as tk


counter = 0
products = {
    "carrot": 1,
    "Apple": 2,
    "Banana": 3,
    "Milk": 10,
    "Water": 5,
}

def add_to_cart():
    global counter
    value = product.get()
    counter += products[value]
    money.config(
        text=f"Summ: {counter} grn"
    )


window = tk.Tk()

window.geometry("400x400")
window.title("Mini Internet Shop")

money = tk.Label(window, text="Summ:", font=("Arial", 20))
money.pack(
    pady=20
)

product = tk.Entry(
    window,
    font="Arial 20",
    justify="center"
)

product.pack()


buy = tk.Button(
    window,
    text="Add",
    font="Arial 20",
    command=add_to_cart
)

buy.pack(
    pady=50
)



window.mainloop()