def derivative(f, x):
    """Computes the derivative of a function at a point x.

    f: function
    x: float

    Returns: float
    """
    h = 1e-4
    return (f(x + h) - f(x)) / h