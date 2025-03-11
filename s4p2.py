# session 4
# limits and continuity
# problem num. 2

import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the function
f = (x**2 - 1) / (x - 1)

# Compute the limit as x approaches 1
limit_value = sp.limit(f, x, 1)

print("The value of the limit is:", limit_value)

