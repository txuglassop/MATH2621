import numpy as np
import matplotlib.pyplot as plt

# Define the function f(z)
def f(z):
    return np.exp(z)

# Define centre x_coord and y_coord and radius r
x_co = 0
y_co = 0
r = 2


# Function to plot transformed circle
def plot_transformed_circle(h, k, r, f, color='green', label=None):
    theta = np.linspace(0, 2 * np.pi, 300)
    x_circle = h + r * np.cos(theta)
    y_circle = k + r * np.sin(theta)
    z_circle = x_circle + 1j * y_circle
    w_circle = f(z_circle)
    
    # Plot in z-plane
    plt.subplot(1, 2, 1)
    plt.plot(x_circle, y_circle, color=color, label=label)
    if label:
        plt.legend()
    
    # Plot in w-plane
    plt.subplot(1, 2, 2)
    plt.plot(w_circle.real, w_circle.imag, color=color, label=f'Image of {label}')
    if label:
        plt.legend()

# ---- Plotting ----

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.title('z-plane')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.axis('equal')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.title('w-plane')
plt.xlabel('Re(w)')
plt.ylabel('Im(w)')
plt.axis('equal')
plt.grid(True)

plot_transformed_circle(h=x_co, k=y_co, r=r, f=f, color='green', label='|z - 1| = 1')

plt.tight_layout()
plt.show()
