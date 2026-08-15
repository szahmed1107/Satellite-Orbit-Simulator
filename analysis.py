import numpy as np
import matplotlib.pyplot as plt
import time

from physics.constants import mu_earth
from physics.orbital import specific_energy
from physics.gravity import gravitational_acc

from numerical.semi_euler import euler_int
from numerical.Heun import heun_int
from numerical.RK4 import rk4_step

from main import (pos_euler, pos_rk4, pos_heun, 
                  vel_euler, vel_heun, vel_rk4, 
                  eps_init, pos_init, vel_init,
                  total_time)

# Numerical Comptuation Times

def computation_time(function, pos_init, vel_init, 
                     total_time, dt_list, mu_earth, 
                     gravitational_acc, eps_init, specific_energy):

    times = []
    errors = []

    for dt in dt_list:
        eps_true = eps_init
        start_time = time.perf_counter()
        x, v = function(pos_init, vel_init, total_time, dt, mu_earth, gravitational_acc)
        end_time = time.perf_counter()
        eps_list = specific_energy(v,x,mu_earth)
        eps_approx = eps_list[-1]
        comp_time = (end_time - start_time) * 1000
        rel_err = np.abs((eps_approx - eps_true) / eps_true * 100)

        times.append(comp_time)
        errors.append(rel_err)

    return times, errors

dt_list = [100, 50, 25, 10, 5, 2, 1]

# Euler execution times and accuracy
euler_times, euler_errors = computation_time(euler_int, pos_init, vel_init, 
                                             total_time, dt_list, mu_earth, 
                                             gravitational_acc, eps_init, 
                                             specific_energy)

# Heun execution times and accuracy
heun_times, heun_errors = computation_time(heun_int, pos_init, vel_init, 
                                           total_time, dt_list, mu_earth, 
                                           gravitational_acc, eps_init, 
                                           specific_energy)

# RK4 execution times and accuracy
rk4_times, rk4_errors = computation_time(rk4_step, pos_init, vel_init, 
                                         total_time, dt_list, mu_earth, 
                                         gravitational_acc, eps_init, 
                                         specific_energy)

# Plot computation times against relative errors

fig1 = plt.figure(figsize=(8,8))
ax1 = fig1.add_subplot(111)
ax1.plot(euler_errors, euler_times, marker='o', label='Semi-Implicit Euler (Symplectic)', color='orange')
ax1.plot(heun_errors, heun_times, marker='+', label="Heun's Method (Explicit)", color='cyan')
ax1.plot(rk4_errors, rk4_times, marker='*', label='RK4 (Explicit)', color='magenta')

ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.set_xlabel('Relative Error (%) (Log Scale)')
ax1.set_ylabel('Computation Time (ms) (Log Scale)')
ax1.set_title('Performance Trade-off: Computation Time vs. Relative Error')
ax1.grid(True, which="both", linestyle="--", alpha=0.5)
ax1.legend()

# Energy Error Calculations

eps_euler = specific_energy(vel_euler, pos_euler, mu_earth)
eps_heun  = specific_energy(vel_heun, pos_heun, mu_earth)
eps_rk4   = specific_energy(vel_rk4, pos_rk4, mu_earth)

err_eps_euler = np.abs((eps_euler - eps_init) / eps_init * 100)
err_eps_heun  = np.abs((eps_heun - eps_init) / eps_init * 100)
err_eps_rk4   = np.abs((eps_rk4 - eps_init) / eps_init * 100)

# Position Error Calculations 

err_pos_euler = np.linalg.norm(pos_euler - pos_rk4, axis=1) / np.linalg.norm(pos_rk4) * 100
err_pos_heun = np.linalg.norm(pos_heun - pos_rk4, axis=1) / np.linalg.norm(pos_rk4) * 100

# Plots

fig2 = plt.figure(figsize=(10, 8))

# TOP SUBPLOT Energy Error
ax_eps = fig2.add_subplot(211) # Fix: 211 instead of 111
ax_eps.plot(err_eps_euler, label='Semi-Implicit Euler (Symplectic)', color='orange')
ax_eps.plot(err_eps_heun, label="Heun's Method (Explicit)", color='cyan')
ax_eps.plot(err_eps_rk4, label='RK4 (Explicit)', color='magenta')

ax_eps.set_yscale('log')
ax_eps.set_xlabel('Timestep')
ax_eps.set_ylabel('Energy Relative Error (%) (Log Scale)')
ax_eps.set_title('Energy Discrepancy Comparison')
ax_eps.grid(True, which="both", linestyle="--", alpha=0.5)
ax_eps.legend()

# BOTTOM SUBPLOT Position Error
ax_pos = fig2.add_subplot(212)
ax_pos.plot(err_pos_euler, label='Semi-Implicit Euler vs. RK4', color='orange')
ax_pos.plot(err_pos_heun, label="Heun's vs. RK4", color='cyan')

ax_pos.set_yscale('log')
ax_pos.set_xlabel('Timestep')
ax_pos.set_ylabel('Position Error (km) (Log Scale)')
ax_pos.set_title('Position Relative to RK4 Baseline')
ax_pos.grid(True, which="both", linestyle="--", alpha=0.5)
ax_pos.legend()

# Prevents subplot titles/labels from overlapping
plt.tight_layout()
plt.show()





