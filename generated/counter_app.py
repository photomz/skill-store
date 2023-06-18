
class CounterApp:
    def __init__(self):
        self.counter = 0

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1

    def reset(self):
        self.counter = 0

app = CounterApp()

app.increment()
app.increment()
app.increment()
app.decrement()
app.reset()
