import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Message", "Button clicked!")

root = tk.Tk()
root.title("Dark Blue Button")

button = tk.Button(root, text="Click me!", command=on_button_click, bg="#00008B")
button.pack(padx=20, pady=20)

root.mainloop()