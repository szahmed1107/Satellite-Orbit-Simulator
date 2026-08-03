import numpy as np
from physics.constants import mu_earth

def gravitational_acc(mu_earth, position):

    distance = np.linalg.norm(position)

    if distance == 0:
        acceleration_g = 0
    else:
        acceleration_g = - (mu_earth * position / distance**3)

    return acceleration_g

