# Satellite Orbit Simulator

## Objective

Numerically propagate satellite trajectories using Newtonian gravity and investigate the accuracy and computational performance of different numerical integration methods.

## Current Features

### Physics

- Two-body Newtonian gravitational model
- Earth gravitational parameter
- Orbital initialisation from periapsis and apoapsis
- Vis-viva equation for angular momentum and state vector analysis
- Classical orbital element (COE) initialisation
- Orbital mechanics analysis
- Perifocal frame to 3d Earth-Centered Intertial frame

### Numerical Methods

- Semi-implicit Euler (Symplectic Euler)
- Heun's Method (Explicit)
- Fourth-order Runge-Kutta (RK4)

### Orbital Analysis

The simulator calculates:

- Specific mechanical energy
- Specific angular momentum
- Eccentricity vector and magnitude
- Semi-major axis
- Orbital period
- Periapsis and apoapsis distances
- Satellite altitude

### Visualisation

- Interactive 3D orbital trajectories around an equal-aspect-ratio 3D Earth sphere
- Comparison of numerical integration methods
- Energy conservation error
- Position error relative to RK4 (baseline)
- Computation time vs. numerical error

### Numerical Investigation

The simulator compares Euler, Heun and RK4 across multiple timesteps.

The following quantities are investigated:

- Computation time
- Relative energy error
- Position error
- Effect of timestep on numerical accuracy

## Physics

The simulator solves the two-body equation of motion:

a_g = -μr/|r|^3

where μ is Earth's gravitational parameter and r is the satellite position vector in the Earth-Centered Inertial (ECI) frame.

Atmospheric drag is also included in the total acceleration:

a_d = - 1/2 x ρ x (C_dxA)/m x v|v|

where:

ρ is atmospheric density
C_d is the drag coefficient
A is the satellite cross-sectional area
m is satellite mass
v is the velocity vector

The total acceleration is therefore:

a = a_g + a_d

The atmospheric model uses the International Standard Atmosphere (ISA) for lower altitudes and an exponential density model for the higher Low Earth Orbit (LEO) region.

## Perifocal Initial Conditions

The initial position and velocity are calculated in the perifocal orbital plane at periapsis.

r_pqw = [r_p,0,0]
v_pqw = [0,μ/h x (1+e),0]

## Perifocal to ECI Transformation

The initial state is transformed using:
- Ω = right ascension of ascending node
- i = inclination
- ω = argument of periapsis

r_ECI = R.r_pqw
v_ECI = R.v_pqw

### Conserved Orbital Quantities

For an ideal two-body orbit, specific mechanical energy and specific angular momentum should remain constant.

#### Specific Mechanical Energy

ε = v^2/2 - μ/r

#### Specific Angular Momentum

h = r × v

#### Eccentricity Vector

e = (v × h)/μ - r/|r|

#### Orbital Period

T = 2π√(a^3/μ)

#### Periapsis and Apoapsis

r_p = a(1-e)

r_a = a(1+e)

## Performance & Numerical Results

The numerical investigation demonstrates the trade-off between computational cost and numerical accuracy.

RK4 provides significantly greater accuracy than Heun for a given timestep, at the cost of additional computation. Despite being a 1st-order method, Semi-Implicit Euler outperforms 2nd-order Heun's method in energy conservation due to its phase-space volume-preserving properties.

The effect of timestep size on energy and position error is also investigated.

![Performance Trade-off](analysis/Performance%20Tradeoff%20-%20Computation%20time%20vs%20rel%20error.png)

*Figure 1: Work-Precision trade-off comparing computation time vs. energy relative error across sweeping timesteps (dt = 100s to 1s).*

![Specific Energy and Position Comparison](analysis/Specific%20energy%20and%20position%20comparison.png)

*Figure 2: Specific mechanical energy discrepancy and position error relative to the RK4 baseline over time.*

![3D Orbit Simulation](analysis/Orbit%20Simulation%201%20-%20Semi-Implicit%20Euler%20vs%20RK4%20vs%20Heun.png)

*Figure 3:3D inclined satellite orbit propagation comparing Semi-Implicit Euler, Heun, and RK4 around a 3D Earth spherical model.*

## Future Development

- J₂ gravitational perturbation
- Orbital manoeuvres
- Hohmann transfer simulation
- Automated validation tests

