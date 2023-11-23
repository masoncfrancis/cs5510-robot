# The following code was generated with the help of ChatGPT and modified by me to run a simulation of a complete circle trace


import math
import matplotlib.pyplot as plt

# Parameters
L = 35.0  # Length of the firetruck
W = 10.0  # Width of the firetruck
V = 8.0   # Constant velocity
R = 18.0  # Radius of the circle
freq = 2.0  # Control frequency
dt = 1.0 / freq  # Time for one control cycle

# Initial state
x = 0.0
y = 0.0
theta = 0.0

# Lists to store data for plotting
path_x = []
path_y = []
trajectory_x = []
trajectory_y = []
angular_velocities = []

# Simulation loop
for _ in range(int(15 * freq)):  # Simulate for 15 seconds in order to complete a whole circle
    # Calculate Ackermann steering angle
    delta = math.atan(L / R)

    # Print out the commands
    print(f"Command: changeInSteeringAngle={delta}, distanceTravelledPerHalfSecond={V * dt}, changeInAngleOrientationPerHalfSecond={V * dt / R}")

    # Calculate displacement
    ds = V * dt

    # Calculate change in orientation
    dtheta = ds / R

    # Update robot's position and orientation
    x += ds * math.cos(theta)
    y += ds * math.sin(theta)
    theta += dtheta

    # Store data for plotting
    path_x.append(x)
    path_y.append(y)
    trajectory_x.append(x)
    trajectory_y.append(y)
    angular_velocities.append(dtheta)

# Plotting
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(path_x, path_y, label='Path')
plt.title('Path')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(trajectory_x, label='X')
plt.plot(trajectory_y, label='Y')
plt.plot(angular_velocities, label='Angular Velocity')
plt.title('Trajectory')
plt.xlabel('Time (s)')
plt.ylabel('Values')
plt.grid(True)
plt.legend()

plt.show()
