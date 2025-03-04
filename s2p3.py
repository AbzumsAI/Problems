# session 2
# functions
# problem num. 3

import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define f(x)
f = (x + 1) / (x - 2)

# Given (g ∘ f)(x) = 1 / (x + 2)
g_of_f = 1 / (x + 2)

# To find g(x), we need to express g(f(x)) in terms of f(x)
# Let y = f(x), then g(y) = 1 / (x + 2)
# We need to express x in terms of y

# Solve y = (x + 1) / (x - 2) for x
x_in_terms_of_y = sp.solve(sp.Eq(y, f), x)

# Since x_in_terms_of_y is a list, we take the first solution
x_expr = x_in_terms_of_y[0]

# Substitute x_expr into g_of_f to get g(y)
g_y = g_of_f.subs(x, x_expr)

# Simplify g(y)
g_y_simplified = sp.simplify(g_y)

print(f"The function g(x) is: {g_y_simplified}")