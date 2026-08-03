from physics.constants import mu_earth
import numpy as np

def semi_major(peri, apo):

    a = (peri + apo) / 2 # semi-major axis

    return a

def orbital_vel(mu_earth, a, rad_orbital):

    vel_orb = np.sqrt(mu_earth * (2/rad_orbital - 1/a))

    return vel_orb

def orbital_period(a, mu_earth):

    period = 2 * np.pi * np.sqrt(a**3 / mu_earth)

    return period

def specific_energy(vel_orb, mu_earth, rad_orbital):

    energy = vel_orb**2 / 2 - mu_earth / rad_orbital

    return energy