from main import pos_euler, vel_euler
from main import pos_rk4, vel_rk4
import matplotlib.pyplot as plt

# Cartesian coordinates - Euler
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

# Set up 3D figure
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot trajectories
ax.plot(x_euler, y_euler, z_euler, label='Euler', linestyle='--')
ax.plot(x_rk4, y_rk4, z_rk4, label='RK4', linewidth=2)

# Labels and legend
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Orbit Simulation: Euler vs. RK4')
ax.legend()

plt.show()