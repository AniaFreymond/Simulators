import numpy as np
import matplotlib.pyplot as plt

a = 1.4
b = 0.3
x0, y0 = 0.1, 0.3
N = 10000
x = np.zeros(N)
y = np.zeros(N)
x[0], y[0] = x0, y0

for i in range(1, N):
    x[i] = 1 - a * x[i-1]**2 + y[i-1]
    y[i] = b * x[i-1]

plt.figure(figsize=(8, 5))
plt.plot(x, y, ',k', alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Hénon Map Iterations')
plt.show()
