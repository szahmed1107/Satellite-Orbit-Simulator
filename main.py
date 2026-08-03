import numpy as np
from physics.constants import mu_earth, rad_earth
from physics.orbital import orbital_vel, semi_major, orbital_period
from physics.gravity import gravitational_acc
from numerical.semi_euler import euler_int
from numerical.RK4 import rk4_step

## Simulation Conditions

# Periapsis and Apoapsis (as altitudes)
peri_alt = 400e+3
apo_alt = 600e+3

# Update periapsis and apoapsis to be from centre of Earth
peri_rad = peri_alt + rad_earth
apo_rad = apo_alt + rad_earth
a = semi_major(peri_rad, apo_rad)

# Time step
dt = 10 # seconds

# Total time 
total_time = orbital_period(a,mu_earth) # seconds

# Initial position of satellite
pos_init = np.array([peri_rad,0,0])

# Initial velocity of satellite
speed = orbital_vel(mu_earth, a, peri_rad)
vel_init = np.array([0,speed,0]) 

# Simulation

pos_euler, vel_euler = euler_int(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)
pos_rk4, vel_rk4 = rk4_step(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)