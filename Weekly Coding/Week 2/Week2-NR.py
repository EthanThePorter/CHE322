from math import sqrt
from scipy.optimize import newton, bisect  # the NR method from scipy

# i have also imported bisection for comparison


# constants
maxit = 50  # maximum number of iterations
tol = 0.0001  # default tol
eps = 1  # initialize epsilon, any value OK as long as greater than the tolerance

# function and its derivative
f = lambda x: -0.9 * x ** 2 + 1.7 * x + 2.5  # define function
fderiv = lambda x: -1.8 * x + 1.7  # define derivative of f

# you could also find this with sympy ! Try it!

initial_guess = 5  # initial guess, try changing this

# since i'd like to keep the values of x at each iteration
# I will make a list and update it with each new value

x = [initial_guess]  # initialize list with the guess

i = 0

while eps > tol and i < maxit:  # while loop runs until we either meet the tol or exceed maxit
    newx = x[i] - f(x[i]) / fderiv(x[i])  # NR formula
    x.append(newx)  # append list with new value
    eps = abs((x[i + 1] - x[i]) / x[i + 1])  # find error
    i += 1  # update i to avoid inf loop!

# while loop has ended
if eps > tol:
    print('Maximum number or iterations reached, cannot find any root')

# finding the exact values for the roots of the quadratic
delt = 1.7 ** 2 - 4 * (-0.9) * 2.5
rootcalc1 = (-1.7 + sqrt(delt)) / (2 * -0.9);
rootcalc2 = (-1.7 - sqrt(delt)) / (2 * -0.9);

# now for the NR method from scipy
# lets see what the variables are for this function
# note : we can use the name of the function directly since it has been imported
# so no need to type scipy.optimize.newton
# help(newton)
(root_NR, result_NR) = newton(f, initial_guess, fprime=fderiv, tol=1e-9,
                              full_output=True)  # the NR method with the derivative
(root_bisect, result_bisect) = bisect(f, 0, initial_guess, xtol=1e-9, full_output=True)  # xtol is 2e-12 by default

print('The roots from each method and the number of iterations are')
print(f'roots from using the quadratic formula are x1= {rootcalc1} x2={rootcalc2}')
print(f'x from our NR          = {x[i]:.10f} \t number of iterations = {i + 1}')
print(f'x from scipy NR        = {root_NR:.10f} \t number of iterations = {result_NR.iterations}')
print(f'x from scipy bisection = {root_bisect:.10f} \t number of iterations = {result_bisect.iterations}')
