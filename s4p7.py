# session 4
# limits and continuity
# problem num. 7

import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x / sp.sqrt(x**2 + 1)

# Calculate the limit as x approaches infinity
limit_value = sp.limit(f, x, sp.oo)

print("The value of the limit is:", limit_value)