import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Message", "Button clicked!")

root = tk.Tk()
root.title("Dark Purple Button")

button = tk.Button(root, text="Click me!", command=on_button_click, bg="#800080")
button.pack(padx=50, pady=50)

root.mainloop()