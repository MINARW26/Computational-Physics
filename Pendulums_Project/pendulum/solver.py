import numpy as np
from scipy.integrate import odeint
from pendulum.model import pendulum_equation

def dSdt(S, t, g, l):
    theta, omega = S
    dtheta_dt = omega
    domega_dt = pendulum_equation(theta, omega, g, l)
    return [dtheta_dt, domega_dt]


def solve_pendulum(theta0, omega0, t, g=9.81, l=1.0):
    return odeint(dSdt, (theta0, omega0), t, args=(g, l))