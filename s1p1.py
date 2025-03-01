# session 1
# algebra
# problem num. 1

import sympy as sp

# Define the variable
x = sp.symbols('x')

# Define the equation
eq = sp.sqrt(x + 11) - sp.sqrt(x + 3) - sp.sqrt(2)

# Solve the equation
solution = sp.solve(eq, x)

# Check if the solution is valid
if solution:
    x_value = solution[0]
    a_plus_b = sp.sqrt(4 * x_value + 26)
    print(f"The value of √(x+11) + √(x+3) is: {a_plus_b}")
else:
    print("No solution found.")

