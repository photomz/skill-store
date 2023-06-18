import tkinter as tk
from tkinter import messagebox

def display_message():
    messagebox.showinfo("Message", "Button clicked!")

app = tk.Tk()
app.title("GUI with Button")

button = tk.Button(app, text="Click me!", command=display_message)
button.pack()

app.mainloop()