def function(x: float, tolerance=10 ** -5):
    # Digits
    if x < 0:
        digits = len(str(x)) - 3
    else:
        digits = len(str(x)) - 2
    # summation
    total = 0.0
    # Indices
    i = 0.0
    # Check for 0 as the input
    if x == 0:
        return 1
    # Solved?
    solved = False
    if abs(x < 0.99):
        # Algorithm for numbers less than 0.99
        while not solved:
            # Calculate next term
            value = x ** i
            # Check status of solution
            if abs(value) < tolerance / 10 ** (digits + 9):
                # If average difference between points is less than tolerance, solved
                solved = True
            else:
                i += 1
            total += value
        return total
    else:
        # Configure index
        i = 1
        # Algorithm for numbers approaching 1
        while not solved:
            # Calculate next term
            value = x ** i
            # Check status of solution
            if abs(value) < tolerance / 10 ** (digits + 9):
                # If average difference between points is less than tolerance, solved
                solved = True
            else:
                i *= 10

        return sum([x ** n for n in range(i)])


numbers = [0.99, 0.999, 0.9999, 0.99999]


for number in numbers:

    calculated = function(number)
    actual = 1/(1 - number)

    print(abs(actual - calculated))
    print(actual, calculated)
    print()



