import numpy as np
import matplotlib.pyplot as plt

# Define the function f(z)
def f(z):
    return np.exp(z)

# Define ranges and create grid lines
x_range = np.linspace(-2, 2, 100)
y_range = np.linspace(-2, 2, 100)

x_lines = np.linspace(-2, 2, 9)  # 9 vertical lines
y_lines = np.linspace(-2, 2, 9)  # 9 horizontal lines

x_line_values = np.linspace(-2, 2, 100)
y_line_values = np.linspace(-2, 2, 100)

# Prepare lists to store mapped lines
mapped_vertical_lines = []
mapped_horizontal_lines = []

# Map vertical lines (x = constant)
for x0 in x_lines:
    z_points = x0 + 1j * y_line_values
    w_points = f(z_points)
    mapped_vertical_lines.append((w_points.real, w_points.imag))

# Map horizontal lines (y = constant)
for y0 in y_lines:
    z_points = x_line_values + 1j * y0
    w_points = f(z_points)
    mapped_horizontal_lines.append((w_points.real, w_points.imag))

# Plotting
plt.figure(figsize=(14, 6))

# z-plane plot
plt.subplot(1, 2, 1)
for x0 in x_lines:
    plt.plot(np.full_like(y_line_values, x0), y_line_values, color='blue', linewidth=0.5)
for y0 in y_lines:
    plt.plot(x_line_values, np.full_like(x_line_values, y0), color='red', linewidth=0.5)

plt.title('z-plane')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid(True)

# w-plane plot
plt.subplot(1, 2, 2)
for x, y in mapped_vertical_lines:
    plt.plot(x, y, color='blue', linewidth=0.5)
for x, y in mapped_horizontal_lines:
    plt.plot(x, y, color='red', linewidth=0.5)

plt.title('w-plane')
plt.xlabel('Re(w)')
plt.ylabel('Im(w)')
plt.axis('equal')
plt.grid(True)

plt.tight_layout()
plt.show()
