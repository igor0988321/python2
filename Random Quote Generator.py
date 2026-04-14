import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def get_qoutes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('b')
        quotes = []
        for title in titles:
            quotes.append(title.get_text().strip())
        cleaned_quotes = [clean_quote(q) for q in quotes]
        return cleaned_quotes
    else:
        messagebox.showerror("Error", "Something went wrong")
        return []

def clean_quote(quote):
    result = ''
    for char in quote:
        if char.isdigit() or char == '.':
            continue
        else:
            result += char
    return result.strip() + '.'

def show_random_quote():
    if quotes:
        random_quote = random.choice(quotes)
        quote_label.config(text=random_quote)
    else:
        quote_label.config(text="No quotes")

def save_to_file():
    if quotes:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                for quote in quotes:
                    file.write(quote + '\n')
            messagebox.showinfo("Success", "Quotes saved successfully")
    else:
        messagebox.showerror("Error", "No quotes")

# enter your URL
url = ""


quotes = get_qoutes(url)
root = tk.Tk()
root.title("Random Quote Generator")

quote_label = tk.Label(root, text="Random Quote Generator",
                       wraplength=400, justify="center")
quote_label.pack(pady=20)

random_button = tk.Button(root,
                          text="Show random quote",
                          command=show_random_quote)
random_button.pack(pady=10)

save_button = tk.Button(root,
                        text="Save to file",
                        command=save_to_file)
save_button.pack(pady=10)

root.mainloop()

