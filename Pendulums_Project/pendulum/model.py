import numpy as np

def pendulum_equation(theta, omega, g, l):
    """
    Zwraca przyspieszenie kątowe (theta'')
    """
    return -g / l * np.sin(theta)