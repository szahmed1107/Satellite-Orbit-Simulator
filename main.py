import numpy as np
from physics.constants import mu_earth, rad_earth
from physics.orbital import (specific_energy,
                             orbital_period,
                             elements_to_state)
from physics.gravity import gravitational_acc
from numerical.semi_euler import euler_int
from numerical.RK4 import rk4_step
from numerical.Heun import heun_int

h_p = float(input("Enter altitude (in km): "))
e = float(input("Enter eccentricity: "))
inc_deg = float(input("Enter inclination (in degrees): "))
omega_deg = float(input("Enter argument of periapsis (in degrees): "))

pos_init, vel_init, a = elements_to_state(rad_earth, mu_earth, h_p, e, inc_deg, omega_deg) # initial position of satellite

eps_init = specific_energy(vel_init, pos_init, mu_earth) # initial energy of satellite

# Time step
dt = 10 # seconds

# Total time 
total_time = orbital_period(a,mu_earth) # seconds

# Simulation

pos_euler, vel_euler = euler_int(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)
pos_rk4, vel_rk4 = rk4_step(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)
pos_heun, vel_heun = heun_int(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)