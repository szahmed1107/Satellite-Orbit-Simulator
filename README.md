# Satellite-Orbit-Simulator

## Objective

Numerically propagate satellite trajectories using Newtonian gravity.

## Current Features

- Two-body gravitational model
- Euler integration
- RK4 integration
- Automated orbital initialisation (calculates semi-major axis, eccentricity, period, and state vectors)
- Orbital mechanics analysis (calculates energy, angular momentum, periapsis, and apoapsis)
- 3D trajectory visualisation

## Physics

The simulator solves the two-body equation of motion:

a = -μr/r³

where μ is Earth's gravitational parameter.

### Conserved Orbital Quantities
The simulator keeps track of the main orbital values that never change as time moves forward:

- Specific Mechanical Energy:
  eps = v^2 / 2 - μ / r

- Specific Angular Momentum:
  h = r x v

- Eccentricity Vector:
  e = (v x h) / μ - r / r

- Orbital Period:
  T = 2pi x sqrt(a^3/μ)

## Future Development

- Implement Heun's method
- Energy conservation analysis
- Numerical method comparison
- Atmospheric drag
- J2 perturbations

