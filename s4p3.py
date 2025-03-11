# session 4
# limits and continuity
# problem num. 3

import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the sign function using Piecewise
sgn = sp.Piecewise(
    (-1, x < 0),
    (0, sp.Eq(x, 0)),
    (1, x > 0)
)

# Compute the limits
limit_right = sp.limit(sgn, x, 0, '+')
limit_left = sp.limit(sgn, x, 0, '-')
limit = sp.limit(sgn, x, 0)

# Print the results
print(f"lim_{{x -> 0^+}} sgn(x) = {limit_right}")
print(f"lim_{{x -> 0^-}} sgn(x) = {limit_left}")
print(f"lim_{{x -> 0}} sgn(x) = {limit}")

# answers are wrong. why? :)