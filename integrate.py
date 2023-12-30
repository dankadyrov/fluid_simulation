from collisions import collision


def make_step(positions, velocities, force, rho, dt, xlim, ylim, hashmap):
    for particle_index in range(len(positions)):
        velocities[particle_index] += force[particle_index] / rho[particle_index] * dt
        positions[particle_index] += velocities[particle_index] * dt
        collision(positions, velocities, xlim, ylim, particle_index)
        hashmap.move(particle_index, positions[particle_index])

