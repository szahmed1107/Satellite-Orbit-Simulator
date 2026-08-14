import numpy as np
from physics.constants import mu_earth
from physics.orbital import specific_energy, semi_major, orbital_period, angular_mom, eccentricity, peri_apo
from physics.gravity import gravitational_acc
from numerical.semi_euler import euler_int
from numerical.RK4 import rk4_step

pos_init = np.array([6.771e6,0,0]) # initial position of satellite

vel_init = np.array([0,7672.6,0]) # initial velocity of satellite

ener_init = specific_energy(vel_init, pos_init, mu_earth) # initial energy of satellite

a = semi_major(mu_earth,ener_init) # semi-major axis

ang_mom = angular_mom(pos_init, vel_init) # Angular momentum

ecc_vec, e = eccentricity(vel_init,ang_mom,pos_init) # Eccentricity

r_p, r_a = peri_apo(a,e) # Periapsis and Apoapsis

# Time step
dt = 10 # seconds

# Total time 
total_time = orbital_period(a,mu_earth) # seconds

# Simulation

pos_euler, vel_euler = euler_int(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)
pos_rk4, vel_rk4 = rk4_step(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)