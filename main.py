from force import compute_force
from integrate import make_step
from pressure import compute_density_pressure

from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from data_structures import HashTable

NUM_POINTS = 800
WIDTH = 250
HEIGHT = 250
EDGE = 5
XLIM = [EDGE, WIDTH - EDGE]
YLIM = [EDGE, HEIGHT - EDGE]

M = 1
K = 20
TARGET_DENSITY = 1
H = 5
VISCOSITY = 1
dt = 0.01

positions = np.zeros((NUM_POINTS, 2))
velocities = np.zeros((NUM_POINTS, 2))
force = np.zeros((NUM_POINTS, 2))
rho = np.zeros(NUM_POINTS)
pressure = np.zeros(NUM_POINTS)
hashmap = HashTable(WIDTH, HEIGHT, H)

i = 0
dam_YLIM = (YLIM[0], YLIM[1] - 1)
dam_XLIM = (int((XLIM[1] - XLIM[0]) * 0.3), int((XLIM[1] - XLIM[0]) * 0.8))
if NUM_POINTS > ((dam_YLIM[1] - dam_YLIM[0]) // H) * ((dam_XLIM[1] - dam_XLIM[0]) // H):
    raise ValueError()

print(dam_XLIM)
for y in range(*dam_YLIM, H):
    for x in range(*dam_XLIM, H):
        if i < NUM_POINTS:
            positions[i] = x + np.random.uniform(0, H * 0.1), y + np.random.uniform(0, H * 0.1)
            hashmap.move(i, positions[i])
        i += 1
    pass


fig = plt.figure()
ax = plt.axes(xlim=(0, WIDTH), ylim=(0, HEIGHT))
scat = ax.scatter([], [])
def animate(i, positions, velocities, force, rho, pressure, h, m, k, density, dt, viscosity):
    pressure, rho = compute_density_pressure(positions, pressure, rho, h, m, k, density, hashmap)
    force = compute_force(positions, velocities, pressure, rho, h, m, viscosity, force, hashmap)
    make_step(positions, velocities, force, rho, dt, XLIM, YLIM, hashmap)
    scat.set_offsets(positions)

print("Calculation...")
anim = animation.FuncAnimation(fig, animate, frames=range(2000), interval=10, blit=False, repeat=False, fargs=(
    positions, velocities, force, rho, pressure, H, M, K, TARGET_DENSITY, dt, VISCOSITY))
print("Writing...")
writer_gif = animation.PillowWriter(fps=100)
anim.save('test.gif', writer=writer_gif)
plt.show()
