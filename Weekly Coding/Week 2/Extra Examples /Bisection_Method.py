import numpy as np
import matplotlib.pyplot as plt

# Define constants
c_d = 0.25
g = 9.81

def f(m):
    return np.sqrt(g * m / c_d) * np.tanh(np.sqrt(g * c_d / m) * 4) - 36


def bisection_method(f: callable, interval: list, tolerance=10e-6):
    # Get initial interval
    a = interval[0]
    b = interval[1]
    # Initialize value to count iterations
    i = 0
    # Initialize value to save previous
    previous = b
    while True:
        # Get values
        f_a = f(a)
        f_b = f(b)
        # Get midpoint
        c = (a + b) / 2
        f_c = f(c)
        # Check if error is within tolerance
        if abs(c - previous) / abs(c) > tolerance:
            # Check for a change in sign
            if f_a * f_c < 0:
                b = c
            if f_b * f_c < 0:
                a = c
            # Update previous value
            previous = c
            # Increment iteration count
            i += 1
        else:
            print(f'Iterations required: {i}')
            return c


print(bisection_method(f, [1, 145]))
