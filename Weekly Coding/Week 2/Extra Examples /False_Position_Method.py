import numpy as np
import matplotlib.pyplot as plt

# Define constants
R = 3


def V(h):
    return 30 - np.pi * h**2 * (3 * R - h) / 3


def false_position_method(f: callable, interval: list, tolerance=10e-5):
    # Get endpoints and f(a), f(b)
    a = interval[0]
    b = interval[1]
    # Initialize value to track iterations
    i = 0
    # Initialize value to store previous
    previous = b
    while True:
        # Get values
        f_a = f(a)
        f_b = f(b)
        # Get c and f(c)
        c = b - f_b * (b - a) / (f_b - f_a)
        f_c = f(c)
        # Check if within tolerance
        if abs(c - previous) / abs(c) > tolerance:
            # Check values
            if f_c * f_a < 0:
                b = c
            if f_c * f_b < 0:
                a = c
            # Update previous
            previous = c
        else:
            return c


print(false_position_method(V, [0, R]))

# h = np.linspace(0, R)
# V_h = V(h)
# plt.plot(h, V_h)
# plt.grid()
# plt.show()




