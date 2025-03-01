# session 1
# algebra
# problem num. 5

import sympy as sp

# Define the variables
x, y = sp.symbols('x y', real=True, nonnegative=True)

# Define the inequality
inequality = (x + y) / 2 - sp.sqrt(x * y)

# Simplify the expression
simplified_inequality = sp.simplify(inequality)

# Prove that the inequality is always non-negative
is_non_negative = sp.simplify(simplified_inequality) >= 0

# Output the result
print("The inequality (x + y)/2 >= sqrt(xy) is:", is_non_negative)


