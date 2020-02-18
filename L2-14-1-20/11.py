import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

x=np.linspace(-3, 3, num=100)
y=np.linspace(-3, 3, num=100,endpoint=False)
print(x,y)


X, Y = np.meshgrid(x, y)
Z=np.sqrt(X**2+Y**2)
print(Z)
"""
plt.contourf(X, Y, Z, 20, cmap='RdGy')
plt.colorbar();
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
"""
fig = plt.figure()
ax = Axes3D(fig)
cset = ax.contour(X, Y, Z,50)
ax.clabel(cset, fontsize=9, inline=1)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()
