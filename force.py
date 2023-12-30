import numpy as np
from math import sqrt, pi

GRAVITY_FORCE = np.array([0, -0.1])
def compute_force(positions, velocities, pressure, rho, h, m, viscosity, force, hashmap):
    h_6 = h ** 6
    spiky_const = -45 * m / (pi * h_6)
    viscosity_const = 45 * viscosity * m / (pi * h_6)

    for i in range(len(positions)):
        f_pressure = np.array([0, 0], dtype=float)
        f_viscosity = np.array([0, 0], dtype=float)
        for j in hashmap.neighbours(positions[i]):
            if i != j:
                r = positions[j] - positions[i]
                n = sqrt(r @ r)
                if n < h:
                    f_pressure -= r / n * (pressure[i] + pressure[j]) / (2 * rho[j]) * spiky_const * ((h - n) ** 2)
                    delta_velocity = (velocities[j] - velocities[i])
                    f_viscosity += delta_velocity / rho[j] * viscosity_const * (h - n)
            force[i] = f_pressure + f_viscosity + GRAVITY_FORCE
    return force

