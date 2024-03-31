# For Macintosh:
# Make sure ffmpeg is installed. Easily via Homebrew:
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# brew install ffmpeg
# Alternatively, directly conda or pip install pillow

import PIL
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g = 9.81  
L1 = 1.0 
L2 = 1.0  
m1 = 1.0 
m2 = 1.0 

def equations(t, y):
    theta1, z1, theta2, z2 = y
    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)
    
    theta1_dot = z1
    z1_dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) -
              (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
    theta2_dot = z2
    z2_dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) +
              m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    
    return theta1_dot, z1_dot, theta2_dot, z2_dot

initial_conditions = [np.pi/2, 0, np.pi/2, 0]
t_span = (0, 20)  # 20 seconds
t_eval = np.linspace(*t_span, 1000)  # Time points at which to solve for the solution
solution = solve_ivp(equations, t_span, initial_conditions, t_eval=t_eval, method='RK45')
theta1, theta2 = solution.y[0], solution.y[2]

x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim((-2.2, 2.2))
ax.set_ylim((-2.2, 2.2))
ax.set_title('Double Pendulum Chaos') 
line, = ax.plot([], [], 'o-', lw=2, color='#00008b')
trace, = ax.plot([], [], '.-', lw=1, ms=2, color='c')  # Changed color to dark blue
xdata, ydata = [], []
xdata, ydata = [], []

def init():
    line.set_data([], [])
    trace.set_data([], [])
    return line, trace
def update(i):
    xdata.append(x2[i])
    ydata.append(y2[i])
    line.set_data([0, x1[i], x2[i]], [0, y1[i], y2[i]])
    trace.set_data(xdata, ydata)
    return line, trace

ani = FuncAnimation(fig, update, frames=range(len(x1)), init_func=init, blit=True, interval=6)
ani.save('/Users/username/Desktop/double_pendulum_simulation.gif', fps=58)

'/mnt/data/double_pendulum_simulation.gif'
