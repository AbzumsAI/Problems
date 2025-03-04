# session 2
# functions
# problem num. 1

import sympy as sp

# Define the symbol and function
x = sp.symbols('x')
f = sp.Function('f')

# Given equation: f(4x + 1) + 2f(3) = 2x + 5
equation = f(4*x + 1) + 2*f(3) - (2*x + 5)

# To find f(-1), we need to find a relationship or solve for f
# Let's substitute x with a specific value to create equations
# Let's choose x = 0 and x = 1 to create two equations

# Substituting x = 0
eq1 = equation.subs(x, 0)

# Substituting x = 1
eq2 = equation.subs(x, 1)

# Now we have two equations:
# eq1: f(1) + 2f(3) = 5
# eq2: f(5) + 2f(3) = 7

# To solve for f(-1), we need another equation involving f(-1)
# Let's substitute x = -1 in the original equation
eq3 = equation.subs(x, -1)

# Now we have three equations:
# eq1: f(1) + 2f(3) = 5
# eq2: f(5) + 2f(3) = 7
# eq3: f(-3) + 2f(3) = 3

# We need to express f(1), f(5), and f(-3) in terms of f(3)
# Let's assume f is linear, i.e., f(x) = a*x + b
a, b = sp.symbols('a b')
f_linear = a*x + b

# Substitute f_linear into the equations
eq1_linear = eq1.subs(f, f_linear)
eq2_linear = eq2.subs(f, f_linear)
eq3_linear = eq3.subs(f, f_linear)

# Solve the system of equations for a and b
solution = sp.solve([eq1_linear, eq2_linear, eq3_linear], (a, b))

# Now, find f(-1) using the linear function
f_minus_1 = f_linear.subs(x, -1).subs(solution)

print(f"The value of f(-1) is: {f_minus_1}")

