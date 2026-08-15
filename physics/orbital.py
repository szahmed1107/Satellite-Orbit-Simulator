from physics.constants import mu_earth
import numpy as np

def specific_energy(velocity, position, mu_earth):

    r = np.linalg.norm(position, axis=-1)
    v = np.linalg.norm(velocity, axis=-1)

    energy = (v**2) / 2.0 - (mu_earth / r)

    return energy

def semi_major(mu_earth,energy):

    a = -mu_earth / (2*energy) # semi-major axis

    return a

def orbital_period(a, mu_earth):

    period = 2 * np.pi * np.sqrt(a**3 / mu_earth)

    return period

def angular_mom(position, velocity):

    ang_mom = np.cross(position,velocity)

    return ang_mom

def eccentricity(velocity,ang_mom,position):

    r = np.linalg.norm(position)
    ecc_vec = np.cross(velocity,ang_mom) / mu_earth - position / r
    e = np.linalg.norm(ecc_vec)

    return ecc_vec, e

def peri_apo(a,e):

    periapsis = a * (1-e)
    apoapsis = a * (1+e)

    return periapsis, apoapsis