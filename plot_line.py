import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return 1 / (z + 1j)

# Define the line in the form ax + by + c = 0
a = 1
b = 2
c = -2

x_values = np.linspace(-2, 3, 400)
y_values = (-a * x_values - c) / b

z = x_values + 1j * y_values
w = f(z)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values, y_values, color='blue', label='x + y = 1')
plt.title('z-plane')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.legend()
plt.axis('equal')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(w.real, w.imag, color='red', label='Image under f(z)')
plt.title('w-plane')
plt.xlabel('Re(w)')
plt.ylabel('Im(w)')
plt.legend()
plt.axis('equal')
plt.grid(True)

plt.tight_layout()
plt.show()
