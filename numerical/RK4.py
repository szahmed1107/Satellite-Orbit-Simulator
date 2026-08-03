import numpy as np

# Fourth order Runge-Kutta integration

def rk4_step(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc):

    steps = int(total_time / dt)

    positions = [pos_init.copy()]
    velocities = [vel_init.copy()]
    x = pos_init.copy()
    v = vel_init.copy()

    for i in range(steps):

        # Stage 1
        k1 = gravitational_acc(mu_earth, x)
        m1 = v

        # Stage 2 
        k2 = gravitational_acc(mu_earth, x + dt/2 * m1)
        m2 = v + dt/2 * k1

        # Stage 3 
        k3 = gravitational_acc(mu_earth, x + dt/2 * m2)
        m3 = v + dt/2 * k2

        # Stage 4 
        k4 = gravitational_acc(mu_earth, x + dt * m3)
        m4 = v + dt * k3

        # Update velocity and position 
        v = v + dt / 6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + dt / 6 * (m1 + 2*m2 + 2*m3 + m4)

        positions.append(x.copy())
        velocities.append(v.copy())

    return np.array(positions), np.array(velocities)
