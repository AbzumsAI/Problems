# session 4
# limits and continuity
# problem num. 9

import numpy as np

def limit_expression(x):
    return x * np.abs(1 / x)

# Values approaching 0 from the negative side
x_values = [-0.1, -0.01, -0.001, -0.0001]

# Calculate the expression for each x value
for x in x_values:
    print(f"x = {x}, value = {limit_expression(x)}")

# the answer is wrong. why? :)