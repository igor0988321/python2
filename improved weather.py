import tkinter as tk

import requests

root = tk.Tk()
root.geometry("300x200")
def get_weather():
    city = city_entry.get()
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)
    text= response.content.decode("utf-8")
    title.config(text=text)

title = tk.Label( root, text="Enter your city name:" ,  font=('Arial', 16))

title.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

btn = tk.Button(root, text="get the weather", command=get_weather)

btn.pack(pady=5)

root.mainloop()