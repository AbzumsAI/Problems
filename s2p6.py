# session 2
# functions
# problem num. 6

import numpy as np
import matplotlib.pyplot as plt

# Define the functions
def f(x):
    return 1 / (x**2 + 1)

def g(x):
    return np.log(x - 3)

def h(x):
    return x**3 - (3 * x**2) / 2 - 6 * x + 7

def k(x):
    return np.sin(x - np.pi / 2)

# Create a range of x values
x_values = np.linspace(-10, 10, 400)

# Plot f(x)
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(x_values, f(x_values), label='$f(x) = \\frac{1}{x^2 + 1}$', color='blue')
plt.title('Graph of $f(x)$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Plot g(x)
# g(x) is defined for x > 3
x_values_g = np.linspace(3.1, 10, 400)
plt.subplot(2, 2, 2)
plt.plot(x_values_g, g(x_values_g), label='$g(x) = \\log(x - 3)$', color='green')
plt.title('Graph of $g(x)$')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.legend()

# Plot h(x)
plt.subplot(2, 2, 3)
plt.plot(x_values, h(x_values), label='$h(x) = x^3 - \\frac{3x^2}{2} - 6x + 7$', color='red')
plt.title('Graph of $h(x)$')
plt.xlabel('x')
plt.ylabel('h(x)')
plt.grid(True)
plt.legend()

# Plot k(x)
plt.subplot(2, 2, 4)
plt.plot(x_values, k(x_values), label='$k(x) = \\sin\\left(x - \\frac{\\pi}{2}\\right)$', color='purple')
plt.title('Graph of $k(x)$')
plt.xlabel('x')
plt.ylabel('k(x)')
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()

