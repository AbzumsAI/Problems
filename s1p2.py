# session 1
# algebra
# problem num. 2

import sympy as sp

# Define the variables
a, b, c = sp.symbols('a b c', real=True, nonnegative=True)

# Define the equations
eq1 = a - b + sp.sqrt(c) - 6
eq2 = sp.sqrt(a) + sp.sqrt(b) - sp.sqrt(c) - 3

# Solve the system of equations
solutions = sp.solve((eq1, eq2), (a, b, c))

# Display the solutions
for sol in solutions:
    a_val, b_val, c_val = sol
    print(f"a = {a_val}, b = {b_val}, c = {c_val}")




    