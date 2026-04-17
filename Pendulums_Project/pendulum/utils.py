import numpy as np

def get_x_y(theta, l):
    x = l * np.sin(theta)
    y = -l * np.cos(theta)
    return x, y