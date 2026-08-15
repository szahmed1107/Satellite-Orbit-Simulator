import numpy as np
from physics.constants import mu_earth, rad_earth
from physics.orbital import (specific_energy,
                             orbital_period,
                             elements_to_state)
from physics.gravity import gravitational_acc
from physics.atmosphere import (atmosphere, 
                                   altitude, 
                                   aero_drag)
from numerical.semi_euler import euler_int
from numerical.RK4 import rk4_step
from numerical.Heun import heun_int

# Orbital Initialisation Inputs
h_p = float(input("Enter altitude at perigee (in km): ")) * 1000
e = float(input("Enter eccentricity: "))
inc_deg = float(input("Enter inclination (in degrees): "))
omega_deg = float(input("Enter argument of periapsis (in degrees): "))

# Satellite Physical Parameters (for Drag)
C_d = 2.2      # Drag coefficient
A = 2.0        # Cross-sectional area (m^2)
m = 100.0      # Mass (kg)

# Compute initial state vector
pos_init, vel_init, a = elements_to_state(rad_earth, mu_earth, h_p, e, inc_deg, omega_deg)
eps_init = specific_energy(vel_init, pos_init, mu_earth)

def total_acceleration(pos, vel):
    alt = altitude(pos, rad_earth)
    rho = atmosphere(alt)
    a_g = gravitational_acc(pos, mu_earth)
    a_d = aero_drag(rho, C_d, A, m, vel)
    return a_g + a_d

# Simulation Time Setup
dt = 10.0  # Time step in seconds
num_orbits = 20
total_time = num_orbits * orbital_period(a, mu_earth)

# 5. Run Integrators with Velocity-Dependent Acceleration Function
pos_euler, vel_euler = euler_int(pos_init, vel_init, total_time, dt, total_acceleration)
pos_rk4, vel_rk4     = rk4_step(pos_init, vel_init, total_time, dt, total_acceleration)
pos_heun, vel_heun   = heun_int(pos_init, vel_init, total_time, dt, total_acceleration)