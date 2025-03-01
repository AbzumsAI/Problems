# session 1
# algebra
# problem num. 3

import sympy as sp

# Define the variable and function
x = sp.symbols('x')
p = lambda x: x**2 + 1

# Compute p(p(x)) + p^2(x)
result = sp.simplify(p(p(x)) + p(x)**2)

# Output the result
print("The value of p(p(x)) + p^2(x) is:", result)




