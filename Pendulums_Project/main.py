import numpy as np
import matplotlib.pyplot as plt
from pendulum.solver import solve_pendulum

t = np.linspace(0, 10, 500)

theta0 = np.pi * 0.2
omega0 = 0.0

solution = solve_pendulum(theta0, omega0, t)

plt.plot(t, solution[:, 0])
plt.xlabel("Time (s)")
plt.ylabel("Angle (rad)")
plt.title("Simple Pendulum")
plt.show()