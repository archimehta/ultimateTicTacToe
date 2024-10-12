import tkinter as tk
from tkinter import ttk
import random

def toggle(value = None):
    curr_text = hello_label["text"]
    print(curr_text, value)
    if curr_text == "Hello World!":
        hello_label["text"] = "Goodbye World :("
    else:
        hello_label["text"] = "Hello World!"

# Create window object
window = tk.Tk()
window.title("Hello World")
window.geometry("300x200")

#Create the label
hello_label = ttk.Label(window, text ="Hello World!", padding=(10,20))
hello_label.pack()

#Toggle button
x = "Goodbye World"
toggle_button = ttk.Button(window, text="Toggle!", command = lambda: toggle(random.randint(1,100)))
toggle_button.pack()

window.mainloop()