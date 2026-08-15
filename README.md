# Satellite Orbit Simulator

## Objective

Numerically propagate satellite trajectories using Newtonian gravity and investigate the accuracy and computational performance of different numerical integration methods.

## Current Features

### Physics

- Two-body Newtonian gravitational model
- Earth gravitational parameter
- Orbital initialisation from periapsis and apoapsis
- Vis-viva equation for initial velocity
- Orbital mechanics analysis

### Numerical Methods

- Semi-implicit Euler (Symplectic Euler)
- Heun's Method (Explicit)
- Fourth-order Runge-Kutta (RK4)

### Orbital Analysis

The simulator calculates:

- Specific mechanical energy
- Specific angular momentum
- Eccentricity vector
- Eccentricity
- Semi-major axis
- Orbital period
- Periapsis
- Apoapsis

### Visualisation

- 3D orbital trajectories
- Comparison of numerical integration methods
- Energy conservation error
- Position error relative to RK4
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

a = -μr/r³

where μ is Earth's gravitational parameter.

### Conserved Orbital Quantities

For an ideal two-body orbit, specific mechanical energy and specific angular momentum should remain constant.

#### Specific Mechanical Energy

ε = v²/2 - μ/r

#### Specific Angular Momentum

h = r × v

#### Eccentricity Vector

e = (v × h)/μ - r/r

#### Orbital Period

T = 2π√(a³/μ)

#### Periapsis and Apoapsis

rₚ = a(1-e)

rₐ = a(1+e)

## Results

The numerical investigation demonstrates the trade-off between computational cost and numerical accuracy.

RK4 provides significantly greater accuracy than Heun for a given timestep, at the cost of additional computation. Despite being a 1st-order method, Semi-Implicit Euler outperforms 2nd-order Heun's method in energy conservation due to its phase-space volume-preserving properties.

The effect of timestep size on energy and position error is also investigated.

## Performance & Numerical Results (Level 3)

![Performance Trade-off](analysis/Performance%20Tradeoff%20-%20Computation%20time%20vs%20rel%20error.png)

*Figure 1: Work-Precision trade-off comparing computation time vs. energy relative error across sweeping timesteps (dt = 100s to 1s).*

![Specific Energy and Position Comparison](analysis/Specific%20energy%20and%20position%20comparison.png)

*Figure 2: Specific mechanical energy discrepancy and position error relative to the RK4 baseline over time.*

## Future Development

- Atmospheric drag model
- J₂ gravitational perturbation
- Three-dimensional orbital elements
- Orbital manoeuvres
- Hohmann transfer simulation
- Improved visualisation
- Automated validation tests

