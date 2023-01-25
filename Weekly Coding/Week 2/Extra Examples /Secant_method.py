import numpy as np
import matplotlib.pyplot as plt

# Define constants
R_0 = 100
A = 6.75e-4
B = 1.34e-8
C = 2.77e-13


def R(T):
    return R_0 * (1 + A*T + B*T**2 + C*T**4) - 150


def secant_method(f: callable, x: float, tolerance=10e-5):
    # Initialize variable to store previous
    previous = x * 1.01
    while True:
        # Finite difference
        d = x * 1.01
        # Calculate f_x
        f_x = f(x)
        # Get next value
        x -= f_x * (x - d) / (f_x - f(d))
        # Check for convergence
        if abs(x - previous) / abs(x) < tolerance:
            return x
        else:
            # Update finite difference value
            previous = x


print(secant_method(R, 400))
