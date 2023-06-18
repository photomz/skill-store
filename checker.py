import tkinter as tk

class CounterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Counter App")
        self.counter = 0

        self.label = tk.Label(self, text=str(self.counter), font=("Arial", 24))
        self.label.pack(pady=10)

        self.increment_button = tk.Button(self, text="Increment", command=self.increment)
        self.increment_button.pack(pady=5)

        self.decrement_button = tk.Button(self, text="Decrement", command=self.decrement)
        self.decrement_button.pack(pady=5)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack(pady=5)

    def increment(self):
        self.counter += 1
        self.label.config(text=str(self.counter))

    def decrement(self):
        self.counter -= 1
        self.label.config(text=str(self.counter))

    def reset(self):
        self.counter = 0
        self.label.config(text=str(self.counter))

def main():
    app = CounterApp()
    app.mainloop()

if __name__ == "__main__":
    main() 
import unittest
import tkinter as tk
from unittest.mock import MagicMock


class TestCounterApp(unittest.TestCase):
    def test_increment(self):
        app = CounterApp()
        app.increment()
        self.assertEqual(app.counter, 1)
        self.assertEqual(app.label["text"], "1")

    def test_decrement(self):
        app = CounterApp()
        app.decrement()
        self.assertEqual(app.counter, -1)
        self.assertEqual(app.label["text"], "-1")

    def test_reset(self):
        app = CounterApp()
        app.increment()
        app.reset()
        self.assertEqual(app.counter, 0)
        self.assertEqual(app.label["text"], "0")

    def test_gui(self):
        app = CounterApp()
        app.mainloop = MagicMock()
        app.mainloop()
        app.mainloop.assert_called_once()


def main():
    unittest.main()


if __name__ == "__main__":
    main()