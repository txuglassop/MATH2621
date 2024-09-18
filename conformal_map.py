import matplotlib.pyplot as plt
import numpy as np

# define function
def f(z):
    return np.exp(z)

# define domain
lim = 3
n = 300
Xv = np.linspace(-lim, lim, n)
Yv = np.linspace(-lim, lim, n)
X, Y = np.meshgrid(Xv, Yv)

# get values of f
Z = X + 1j * Y
Fv = f(Z)
lv = np.linspace(-10,10,21)

fig, (ax, ax2) = plt.subplots(1,2, figsize = (10,5))
fig.suptitle(r"$f(z)=e^z$", fontsize=18)
ax.set_aspect("equal")
ax2.set_aspect("equal")

ax.contour(Xv, Yv, X, colors="blue", linestyles="solid", levels=lv, linewidths=1)
ax.contour(Xv, Yv, Y, colors="red", linestyles="solid", levels=lv, linewidths=1)
ax.set_xlabel("$Re$ $Z$", fontsize=14)
ax.set_ylabel("$Im$ $Z$", fontsize=14)
ax.set_title("Before")

ax2.contour(Xv, Yv, np.real(Fv), colors="blue", linestyles="solid", levels=lv, linewidths=1)
ax2.contour(Xv, Yv, np.imag(Fv), colors="red", linestyles="solid", levels=lv, linewidths=1)
ax2.set_xlabel("$Re$ $Z$", fontsize=14)
ax2.set_ylabel("$Im$ $Z$", fontsize=14)
ax2.set_title("After")

plt.subplots_adjust(wspace=0.5)
plt.show()
