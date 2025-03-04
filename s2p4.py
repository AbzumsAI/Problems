# session 2
# functions
# problem num. 4

import sympy as sp

# Define the symbols
x, a, b = sp.symbols('x a b', real=True, nonnegative=True)

# Define the functions f(x) and g(x)
f = sp.sqrt(x + sp.sqrt(x))
g = sp.sqrt(x - sp.sqrt(x))

# Compute (f + g)(x)
f_plus_g = f + g

# Given expression for (f + g)(x)
given_expression = sp.sqrt(a*x + 2*sp.sqrt(x**2) - b*x)

# Simplify the given expression
given_expression_simplified = sp.simplify(given_expression)

# Equate the computed sum to the given expression
equation = sp.Eq(f_plus_g, given_expression_simplified)

# Solve for a and b
solution = sp.solve(equation, (a, b))

print(f"The values of a and b are: {solution}")

