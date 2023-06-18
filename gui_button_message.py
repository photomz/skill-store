import tkinter as tk
from tkinter import messagebox

def display_message():
    messagebox.showinfo("Message", "Button clicked!")

app = tk.Tk()
app.title("Button Click Message")

button = tk.Button(app, text="Hello", command=display_message)
button.pack()

app.mainloop()