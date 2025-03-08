# session 3
# functions
# problem num. 2

from sympy import symbols, Eq, simplify

# Define symbols
x, y, k = symbols('x y k')

# Define the function f(x) = kx
f = lambda x: k * x

# Define the functional equation
left_side = x * f(x) - y * f(y)
right_side = (x - y) * f(x + y)
equation = Eq(left_side, right_side)

# Simplify the equation
simplified_eq = simplify(equation)

# Check if the equation holds true
if simplified_eq == True:
    print("The function f(x) = kx satisfies the equation for any constant k.")
else:
    print("The function f(x) = kx does not satisfy the equation.")