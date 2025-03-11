# session 4
# limits and continuity
# problem num. 6

import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
f = 1 / x**2

# Calculate the limit
limit_value = sp.limit(f, x, 0)

# Print the result
print("The value of the limit is:", limit_value)

# the answer is wrong. why? :)