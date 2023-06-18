import math

def f(x):
    return math.exp(-x**2)

def integral(a, b, N):
    h = (b-a)/N
    s = 0.5*(f(a) + f(b))
    for i in range(1, N):
        s += f(a + i*h)
    return s*h

a, b = 0, 1