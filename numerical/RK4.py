import numpy as np

# Fourth-order Runge-Kutta integration
def rk4_step(pos_init, vel_init, total_time, dt, total_acceleration):

    steps = int(total_time / dt)

    positions = [pos_init.copy()]
    velocities = [vel_init.copy()]
    x = pos_init.copy()
    v = vel_init.copy()

    for i in range(steps):

        # Stage 1
        m1 = v
        k1 = total_acceleration(x, v)

        # Stage 2
        x2 = x + 0.5 * dt * m1
        v2 = v + 0.5 * dt * k1
        m2 = v2
        k2 = total_acceleration(x2, v2)

        # Stage 3
        x3 = x + 0.5 * dt * m2
        v3 = v + 0.5 * dt * k2
        m3 = v3
        k3 = total_acceleration(x3, v3)

        # Stage 4
        x4 = x + dt * m3
        v4 = v + dt * k3
        m4 = v4
        k4 = total_acceleration(x4, v4)

        # Update position and velocity 
        x = x + (dt / 6.0) * (m1 + 2*m2 + 2*m3 + m4)
        v = v + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)

        positions.append(x.copy())
        velocities.append(v.copy())

    return np.array(positions), np.array(velocities)
