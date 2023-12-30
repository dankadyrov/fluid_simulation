from math import pi


def compute_density_pressure(positions, pressure, rho, h, m, k, rest_density, hashmap):
    h_squared = h ** 2
    h_9 = h ** 9
    pressure_poly6 = m * 315 / (64 * pi * h_9)
    for i in range(len(positions)):
        rho[i] = 0
        for j in hashmap.neighbours(positions[i]):
            r = positions[j] - positions[i]
            r_squared = r @ r
            if r_squared <= h_squared:
                rho[i] += pressure_poly6 * (h_squared - r_squared) ** 3
        pressure[i] = k * (rho[i] - rest_density)
    return pressure, rho

