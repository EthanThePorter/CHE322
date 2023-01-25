# Ethan Porter, Student ID: 20909618

def mypolyval(p, x):
    """
    (list,float)-> float
    function to evaluate a polynomial p at x.
    """
    # Check for empty list
    if not p:
        return 0.0
    # Initialize variable to store total as Horner's scheme progresses
    total = 0.0
    # Store polynomial constant term
    constant = p[0]
    # Format polynomial by removing constant in first position, then reversing list
    p = p[1:][::-1]
    # Run Horner's scheme on the list
    for i in p:
        # Add term coefficient to the total
        total += i
        # Multiply everything by x
        total *= x
    # Add constant to the end
    total += constant
    return total


def average_of_values(x: list):
    x.sort()
    average = sum(x) / len(x)
    return x + [average]


def quadratic(a, b, c):
    root1 = (-b + (b ** 2 - 4 * a * c) ** 1/2) / (2 * a)
    root2 = (-b - (b ** 2 - 4 * a * c) ** 1/2) / (2 * a)

    return root1, root2


print(quadratic(1, 6, 9))