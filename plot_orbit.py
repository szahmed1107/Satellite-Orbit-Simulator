from main import (pos_euler, vel_euler, 
                  pos_rk4, vel_rk4,
                  pos_heun, vel_heun,
                  pos_init)
from physics.constants import rad_earth
import numpy as np
import matplotlib.pyplot as plt

# Cartesian coordinates - Semi-Implicit Euler
x_euler = pos_euler[:,0]
y_euler = pos_euler[:,1]
z_euler = pos_euler[:,2]

u_euler = vel_euler[:,0]
v_euler = vel_euler[:,1]
w_euler = vel_euler[:,2]

# Cartesian coordinates - RK4
x_rk4 = pos_rk4[:,0]
y_rk4 = pos_rk4[:,1]
z_rk4 = pos_rk4[:,2]

u_rk4 = vel_rk4[:,0]
v_rk4 = vel_rk4[:,1]
w_rk4 = vel_rk4[:,2]

# Cartesian coordinates - Heun
x_heun = pos_heun[:,0]
y_heun = pos_heun[:,1]
z_heun = pos_heun[:,2]

u_heun = vel_heun[:,0]
v_heun = vel_heun[:,1]
w_heun = vel_heun[:,2]

# Cartesian coordination - initial position
x_init = pos_init[0]
y_init = pos_init[1]
z_init = pos_init[2]

# Set up 3D figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot 3D Earth Sphere at Origin (0,0,0)
u = np.linspace(0, 2 * np.pi, 30)
v = np.linspace(0, np.pi, 30)
x_earth = rad_earth * np.outer(np.cos(u), np.sin(v))
y_earth = rad_earth * np.outer(np.sin(u), np.sin(v))
z_earth = rad_earth * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x_earth, y_earth, z_earth, color='royalblue', alpha=0.2, edgecolor='navy', linewidth=0.3)

# Plot Trajectories & Start Point
ax.plot(x_euler, y_euler, z_euler, label='Semi-Implicit Euler', linestyle='--', color='orange')
ax.plot(x_heun, y_heun, z_heun, label='Heun', linestyle='-.', color='cyan')
ax.plot(x_rk4, y_rk4, z_rk4, label='RK4', linestyle='-', color='magenta')

# Start marker (Perigee)
ax.scatter(x_init, y_init, z_init, color='black', s=50, label='Start (Periapsis)', zorder=5)

# Equal Axis Scaling (Fixes Visual Distortion)
max_range = np.array([
    x_rk4.max() - x_rk4.min(),
    y_rk4.max() - y_rk4.min(),
    z_rk4.max() - z_rk4.min()
]).max() / 2.0

mid_x = (x_rk4.max() + x_rk4.min()) * 0.5
mid_y = (y_rk4.max() + y_rk4.min()) * 0.5
mid_z = (z_rk4.max() + z_rk4.min()) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Labels and legend
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Orbit Simulation: Semi-Implicit Euler vs RK4 vs Heun')
ax.legend(loc='upper right')

plt.tight_layout()
plt.show()