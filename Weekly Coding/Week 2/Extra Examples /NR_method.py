import numpy as np
import matplotlib.pyplot as plt

# Define constants
R_0 = 100
A = 6.75e-4
B = 1.34e-8
C = 2.77e-13


def R(T):
    return R_0 * (1 + A*T + B*T**2 + C*T**4) - 150


def dR(T):
    return R_0 * (A + 2*B*T + 4*C*T**3)


def NR_method(f: callable, df: callable, x, tolerance=10e-5):
    # Initialize variable to store previous
    previous = x
    while True:
        # Get next value
        x -= f(x) / df(x)
        # Check for convergence
        if abs(x - previous) / abs(x) < tolerance:
            return x
        else:
            # Update check value
            previous = x


print(NR_method(R, dR, 400))

# # Plot
# T = np.linspace(400, 800)
# R_T = R(T)
# plt.plot(T, R_T)
# plt.grid()
# plt.show()
