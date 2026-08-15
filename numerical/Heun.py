import numpy as np

# Heun's Method 
def heun_int(pos_init, vel_init, total_time, dt, total_acceleration):

    steps = int(total_time / dt)

    positions = [pos_init.copy()]
    velocities = [vel_init.copy()]
    x = pos_init.copy()
    v = vel_init.copy()

    for i in range(steps):

        # Predictor step (Euler prediction)
        a_1 = total_acceleration(x, v)
        x_pred = x + v * dt
        v_pred = v + a_1 * dt

        # Corrector step (Evaluate acceleration at predicted state)
        a_2 = total_acceleration(x_pred, v_pred)

        # Update position and velocity using averaged slopes
        x = x + 0.5 * dt * (v + v_pred)
        v = v + 0.5 * dt * (a_1 + a_2)

        positions.append(x.copy())
        velocities.append(v.copy())

    return np.array(positions), np.array(velocities)