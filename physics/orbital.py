from physics.constants import mu_earth, rad_earth
import numpy as np

def specific_energy(velocity, position, mu_earth=mu_earth):
    r = np.linalg.norm(position)
    v = np.linalg.norm(velocity)
    return (v**2) / 2 - (mu_earth / r)

def semi_major_axis(mu_earth, eps):    # where eps represents specific energy
    return -mu_earth / (2.0 * eps) 

def orbital_period(a, mu_earth=mu_earth):
    return 2.0 * np.pi * np.sqrt(a**3 / mu_earth)

def angular_mom(position, velocity):
    return np.cross(position, velocity)

def eccentricity(velocity, ang_mom, position, mu_earth=mu_earth):
    r = np.linalg.norm(position)
    ecc_vec = np.cross(velocity, ang_mom) / mu_earth - position / r
    e = np.linalg.norm(ecc_vec)
    return ecc_vec, e

def peri_apo(a,e):
    periapsis = a * (1-e)
    apoapsis = a * (1+e)
    return periapsis, apoapsis

def elements_to_state(rad_earth, mu_earth, h_p, e, inc_deg, omega_deg):
    # Converts Keplerian Orbital Elements to 3D ECI Cartesian initial state vectors.
    # Assumes starting position at periapsis (true anomaly nu = 0).

    if e >= 1.0:
        raise ValueError("Eccentricity must be e < 1.0 for closed orbits.")

    # Orbital geometry & invariants
    r_p = rad_earth + h_p   # Periapsis radius (m)
    a = r_p / (1.0 - e)    # Semi-major axis (m)
    h = np.sqrt(mu_earth * a * (1.0 - e**2))    # Specific angular momentum (m^2/s)

    # State vectors in 2D Perifocal Frame (PQW) at periapsis
    r_pqw = np.array([r_p,0,0])
    v_pqw = np.array([0, mu_earth/h*(1+e),0])

    # Convert angles to radians
    inc = np.radians(inc_deg) 
    omega = np.radians(omega_deg)

    sin_inc, cos_inc = np.sin(inc), np.cos(inc) 
    sin_omg, cos_omg = np.sin(omega), np.cos(omega) 

    # Evaluate rotation matrices
    rot_x = np.array([[1, 0, 0],
                     [0, cos_inc, -sin_inc],
                     [0, sin_inc, cos_inc]])
    
    rot_z = np.array([[cos_omg, -sin_omg, 0],
                     [sin_omg, cos_omg, 0],
                     [0, 0, 1]])

    R = np.dot(rot_x, rot_z)

    # Final Cartesian ECI state vectors
    pos_init = np.dot(R,r_pqw)
    vel_init = np.dot(R,v_pqw)

    return pos_init, vel_init, a

    
