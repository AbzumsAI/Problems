# session 2
# functions
# problem num. 5

import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return 2 * x**2 - 5 * x + 3

def g(x):
    return x**3 + 6 * x**2 - 3 * x - 5

def h(x):
    return (2 * x - 4) / (x + 5)

# Create a range of x values
x_values = np.linspace(-10, 10, 400)

# Plot f(x)
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(x_values, f(x_values), label='$f(x) = 2x^2 - 5x + 3$', color='blue')
plt.title('Graph of $f(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Plot g(x)
plt.subplot(1, 3, 2)
plt.plot(x_values, g(x_values), label='$g(x) = x^3 + 6x^2 - 3x - 5$', color='green')
plt.title('Graph of $g(x)$')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.legend()

# Plot h(x)
# Avoid division by zero by excluding x = -5
x_values_h = np.linspace(-10, 10, 400)
x_values_h = x_values_h[x_values_h != -5]  # Exclude x = -5

plt.subplot(1, 3, 3)
plt.plot(x_values_h, h(x_values_h), label='$h(x) = \\frac{2x - 4}{x + 5}$', color='red')
plt.title('Graph of $h(x)$')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()