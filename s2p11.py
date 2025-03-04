# session 2
# functions
# problem num. 11

import sympy as sp

# Define the symbol and function
x = sp.symbols('x')
f = sp.Function('f')

# Given equation: 2f(x) + f(1/x) = 2x + 1
equation = 2 * f(x) + f(1 / x) - (2 * x + 1)

# To find f(x), we need another equation involving f(x) and f(1/x)
# Let's substitute x with 1/x in the original equation
equation_substituted = equation.subs(x, 1 / x)

# Now we have two equations:
# eq1: 2f(x) + f(1/x) = 2x + 1
# eq2: 2f(1/x) + f(x) = 2/x + 1

# Solve the system of equations for f(x) and f(1/x)
solution = sp.solve([equation, equation_substituted], [f(x), f(1 / x)])

# Extract f(x) from the solution
f_x = solution[f(x)]

# Simplify the expression for f(x)
f_x_simplified = sp.simplify(f_x)

print(f"The explicit form of f(x) is: {f_x_simplified}")


