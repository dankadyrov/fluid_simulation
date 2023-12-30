DAMPING_COEF = 0.5


def collision(positions, velocities, xlim, ylim, particle_index):
    if positions[particle_index, 0] < xlim[0]:
        velocities[particle_index, 0] *= -DAMPING_COEF
        positions[particle_index, 0] = xlim[0]
    elif positions[particle_index, 0] > xlim[1]:
        velocities[particle_index, 0] *= -DAMPING_COEF
        positions[particle_index, 0] = xlim[1]

    if positions[particle_index, 1] < ylim[0]:
        velocities[particle_index, 1] *= -DAMPING_COEF
        positions[particle_index, 1] = ylim[0]
    elif positions[particle_index, 1] > ylim[1]:
        velocities[particle_index, 1] *= -DAMPING_COEF
        positions[particle_index, 1] = ylim[1]
