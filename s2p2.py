# session 2
# functions
# problem num. 2

import sympy as sp

# Define the symbols
y = sp.symbols('y', real=True)

# Define the relation
x = y / sp.sqrt(1 + y**2)

# Solve for y in terms of x
y_solutions = sp.solve(x - y / sp.sqrt(1 + y**2), y)

# Check if there is exactly one solution for y
if len(y_solutions) == 1:
    print("The relation is a function because each x corresponds to exactly one y.")
else:
    print("The relation is not a function because some x values correspond to more than one y.")


