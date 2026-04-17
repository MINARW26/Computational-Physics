import numpy as np
from pendulum.solver import solve_pendulum

def test_solution_shape():
    t = np.linspace(0, 10, 100)
    sol = solve_pendulum(0.1, 0, t)
    assert sol.shape == (100, 2)


def test_initial_conditions():
    t = np.linspace(0, 10, 100)
    theta0 = 0.2
    omega0 = 0.3
    sol = solve_pendulum(theta0, omega0, t)

    assert np.isclose(sol[0, 0], theta0)
    assert np.isclose(sol[0, 1], omega0)