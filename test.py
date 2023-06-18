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