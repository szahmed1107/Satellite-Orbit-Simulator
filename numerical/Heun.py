import numpy as np

# Heun's Method

def heun_int(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc):

    steps = int(total_time / dt)

    positions = [pos_init.copy()]
    velocities = [vel_init.copy()]
    x = pos_init.copy()
    v = vel_init.copy()

    for i in range(steps):

        # Euler prediction
        g_e = gravitational_acc(mu_earth, x)
        x_e = x + v*dt
        v_e = v + g_e*dt

        g = gravitational_acc(mu_earth, x_e)
        x += 0.5 * dt * (v + v_e)
        v += 0.5 * dt * (g_e + g)

        positions.append(x.copy())
        velocities.append(v.copy())

    return np.array(positions), np.array(velocities)