import numpy as np


def function(x: float, tolerance=10 ** -5):
    # Digits
    digits = float(len(str(x)) - 2)
    # Indices
    i = 0.0
    # Solved?
    solved = False
    # Algorithm
    while not solved:
        index_1 = x ** i

        if index_1 < tolerance / 10 ** (digits ** digits):
            # If average difference between points is less than tolerance, solved
            solved = True
        else:
            i += 1

    return sum([x ** n for n in range(int(i))]), i, digits


numbers = [0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999, 0.9999999, 0.99999999]

for number in numbers:

    calculated, i1, digits = function(number)
    actual = 1/(1 - number)

    print(abs(actual - calculated), i1, )
    print(actual, calculated)
    print()
