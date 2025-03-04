# session 2
# functions
# problem num. 11

import sympy as sp

# Define the symbol
x, y = sp.symbols('x y')

# Define the functions
f = 2 * x - 7
g = 2 / ((1/2) * x + 9)
h = 2 ** (3 * x / x) - 4
k = (3 * x - 2) / (2 * x + 7)

# Calculate the inverse functions
f_inv = sp.solve(sp.Eq(y, f), x)[0]
g_inv = sp.solve(sp.Eq(y, g), x)[0]
h_inv = sp.solve(sp.Eq(y, h), x)[0]
k_inv = sp.solve(sp.Eq(y, k), x)[0]

# Simplify the inverse functions
f_inv_simplified = sp.simplify(f_inv)
g_inv_simplified = sp.simplify(g_inv)
h_inv_simplified = sp.simplify(h_inv)
k_inv_simplified = sp.simplify(k_inv)

# Print the inverse functions
print(f"Inverse of f(x): f^(-1)(y) = {f_inv_simplified}")
print(f"Inverse of g(x): g^(-1)(y) = {g_inv_simplified}")
print(f"Inverse of h(x): h^(-1)(y) = {h_inv_simplified}")
print(f"Inverse of k(x): k^(-1)(y) = {k_inv_simplified}")