# session 4
# limits and continuity
# problem num. 4

import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the function
f = sp.Abs(x - 2) / (x**2 + x - 6)

# Compute the limit as x approaches 2
limit_value = sp.limit(f, x, 2)

print("The value of the limit is:", limit_value)