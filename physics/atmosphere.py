import numpy as np
from physics.constants import rad_earth

def altitude(position, rad_earth=rad_earth):
    r = np.linalg.norm(position)
    return r - rad_earth

R = 287.05287   # Air gas constant
g = 9.80665     # Sea level gravity 

ISA_layers = np.array([
    [0, -0.0065, 288.15, 101325],           # Sea-level
    [11000, 0.0, 216.65, 22632.1],          # Troposphere
    [20000, 0.0010, 216.65, 5474.89],       # Lower Stratosphere
    [32000, 0.0028, 228.65, 868.019],       # Upper Stratosphere
    [47000, 0.0, 270.65, 110.906],          # Stratopause
    [51000, -0.0028, 270.65, 66.9389],      # Lower Mesosphere
    [71000, -0.0020, 214.65, 3.95642],      # Upper Mesosphere
])

LEO_layers = np.array([
    (86000.0,    6.958e-6,     5600.0),      # Mesopause Transition (86 km - 100 km)
    (100000.0,   5.558e-7,     5800.0),      # Thermosphere Base (100 km)
    (150000.0,   2.076e-9,     22500.0),     # LEO Layer 1
    (200000.0,   2.789e-10,    37500.0),     # LEO Layer 2
    (300000.0,   2.418e-11,    53600.0),     # LEO Layer 3
    (500000.0,   5.215e-13,    64200.0),     # LEO Layer 4
    (700000.0,   3.070e-14,    87500.0),     # LEO Layer 5
    ])

def atmosphere(alt):

    if alt <= 0:
        return 1.225
    if alt >= 1_000_000:
        return 0.0

    if 0<= alt <86000:
    # Based on International Standard Atmosphere (ISA)
    # if altitude is less than 86km

        idx = 0
        for i in range(len(ISA_layers)):
            if alt >= ISA_layers[i, 0]:
                idx = i

        h_b, lapse, T_b, P_b = ISA_layers[idx]

        if lapse != 0:
            T = T_b + lapse*(alt-h_b)
            P = P_b * (T/T_b)**(-g/(lapse*R))
        else:
            T = T_b
            P = P_b * np.exp((-g*(alt-h_b))/(R*T_b))

        rho = P/(R*T)

    else:
    # Based on U.S. Standard Atmosphere (1976) reference model
    # if altitude is greater than 86km but less than 1000km
    # Low Earth Orbit (LEO)

        idx = 0
        for i in range(len(LEO_layers)):
            if alt >= LEO_layers[i, 0]:
                idx = i

        h_b, rho_b, H_b = LEO_layers[idx]
        rho = rho_b * np.exp(-(alt-h_b)/H_b)

    return rho

def aero_drag(rho,C_d,A,m,vel):
    if rho == 0.0:
        return np.zeros_like(vel)
    v_m = np.linalg.norm(vel)
    return - 1/2 * rho * (C_d*A)/m * vel * v_m



    


