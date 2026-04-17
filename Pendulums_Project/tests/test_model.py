import numpy as np
from pendulum.model import pendulum_equation

def test_zero_angle():
    assert pendulum_equation(0, 0, 9.81, 1) == 0


def test_small_angle_approximation():
    theta = 0.01
    result = pendulum_equation(theta, 0, 9.81, 1)
    expected = -9.81 * theta  # sin(theta) ~ theta
    assert np.isclose(result, expected, atol=1e-3)