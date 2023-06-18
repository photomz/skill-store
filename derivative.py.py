def derivative(f, x):
    """Computes the derivative of a function at a point x."""
    h = 1e-4
    return (f(x + h) - f(x)) / h 
def f(x):
    return x**2

def test_derivative():
    assert derivative(f, 1) == 2
    assert derivative(f, 2) == 4