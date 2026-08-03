import numpy as np

# Semi-implicit Euler integration

def euler_int(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc):

    steps = int(total_time / dt)

    positions = [pos_init.copy()]
    velocities = [vel_init.copy()]
    x = pos_init.copy()
    v = vel_init.copy()

    for i in range(steps):

        g = gravitational_acc(mu_earth, x)
        v = v + g*dt
        x = x + v*dt

        positions.append(x.copy())
        velocities.append(v.copy())

    return np.array(positions), np.array(velocities)