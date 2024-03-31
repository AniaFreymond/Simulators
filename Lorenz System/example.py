# Make sure Pillow is installed

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.cm import viridis

def lorenz(xyz, s=10, r=28, b=8/3):
    x, y, z = xyz
    x_dot = s * (y - x)
    y_dot = r * x - y - x * z
    z_dot = x * y - b * z
    return np.array([x_dot, y_dot, z_dot])

dt = 0.01
num_steps = 2000
xyzs = np.empty((num_steps + 1, 3))
xyzs[0] = (0., 1., 1.)

for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
z_normalized = (xyzs[:, 2] - xyzs[:, 2].min()) / (xyzs[:, 2].max() - xyzs[:, 2].min())
colors = viridis(z_normalized)

def update(num, xyzs, ax, colors):
    ax.clear()
    ax.view_init(30, num * (360 / num_steps))
    for i in range(num):
        if i == 0: continue
        ax.plot(xyzs[i-1:i+1, 0], xyzs[i-1:i+1, 1], xyzs[i-1:i+1, 2], color=colors[i], lw=0.5)
    ax.set_xlim([xyzs[:, 0].min(), xyzs[:, 0].max()])
    ax.set_ylim([xyzs[:, 1].min(), xyzs[:, 1].max()])
    ax.set_zlim([xyzs[:, 2].min(), xyzs[:, 2].max()])
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Z Axis")
    ax.set_title("Lorenz Attractor")

ani = FuncAnimation(fig, update, frames=np.arange(1, num_steps, 11), fargs=(xyzs, ax, colors), interval=51)

gif_path = '/Users/username/Desktop/lorenz_attractor.gif'
ani.save(gif_path, writer='imagemagick', fps=10)
