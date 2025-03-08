# session 3
# functions
# problem num. 1

from sympy import symbols, Eq, Function, solve

# Define the symbol
x = symbols('x')

# Define the function f(x)
f = Function('f')

# Define the functional equation
equation = Eq(2*f(x) + f(1 - x), x**2)

# Substitute x with 1 - x to get another equation
equation_sub = equation.subs(x, 1 - x)

# Now we have a system of two equations:
# 2*f(x) + f(1 - x) = x^2
# 2*f(1 - x) + f(x) = (1 - x)^2

# Solve the system of equations
solution = solve([equation, equation_sub], (f(x), f(1 - x)))

# Extract the solution for f(x)
f_x_solution = solution[f(x)]

print("The solution for f(x) is:", f_x_solution)