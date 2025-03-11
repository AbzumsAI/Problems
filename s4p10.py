# session 4
# limits and continuity
# problem num. 10

import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = x * sp.sin(1 / x)

# Calculate the limit as x approaches 0
limit_value = sp.limit(f, x, 0)

print("The limit is:", limit_value)