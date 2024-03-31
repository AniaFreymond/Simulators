# Example of how simple nonlinear dynamical systems can exhibit complex behaviour including chaos, following the logistic equation:
# x_(n+1) = rx_n(1-x_n)

import numpy as np
import matplotlib.pyplot as plt

r_range = np.linspace(2.5, 4.0, 10000)
states = []
rs = []
settling = 1000
recording = 100

for r in r_range:
    x = 0.5
    for _ in range(settling):
        x = r * x * (1 - x)
    for _ in range(recording):
        x = r * x * (1 - x)
        states.append(x)
        rs.append(r)

plt.figure(figsize=(10, 6))
plt.scatter(rs, states, s=0.05, c=rs, cmap='hot', alpha=0.6)
plt.title("Bifurcation Diagram of the Logistic Map")
plt.xlabel("r")
plt.ylabel("x")
plt.xlim(2.5, 4.0)
plt.ylim(0, 1)
plt.colorbar(label='r')
plt.show()
