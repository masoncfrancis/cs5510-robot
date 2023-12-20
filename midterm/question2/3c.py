# This code was generated by ChatGPT

import math
import time
import matplotlib.pyplot as plt

# Vehicle parameters
L = 35.0  # Length of the vehicle
V = 8.0   # Constant velocity
R_circle = 9.0  # Radius of the circle
omega_circle = V / R_circle  # Angular velocity for circular motion

# Time step values to test
dt_values = [1.0, 0.1, 0.01]

# Function to calculate the analytical position at a given time
def analytical_position(t):
    x_analytical = R_circle * math.cos(omega_circle * t)
    y_analytical = R_circle * math.sin(omega_circle * t)
    return x_analytical, y_analytical

# Function to perform the forward Euler integration
def forward_euler(dt, total_time):
    num_steps = int(total_time / dt)
    x_numerical, y_numerical = [], []

    x_numerical.append(R_circle)
    y_numerical.append(0.0)

    for _ in range(1, num_steps + 1):
        x_n = x_numerical[-1] + V * dt * math.cos(omega_circle * (_ * dt))
        y_n = y_numerical[-1] + V * dt * math.sin(omega_circle * (_ * dt))
        x_numerical.append(x_n)
        y_numerical.append(y_n)

    return x_numerical, y_numerical

# Function to calculate positional error
def calculate_error(x_analytical, y_analytical, x_numerical, y_numerical):
    errors = [math.sqrt((xa - xn)**2 + (ya - yn)**2) for xa, ya, xn, yn in zip(x_analytical, y_analytical, x_numerical, y_numerical)]
    return errors

# Main simulation loop for different time steps
for dt in dt_values:
    start_time = time.time()

    total_time = 10.0  # Total simulation time

    # Analytical position
    x_analytical, y_analytical = zip(*[analytical_position(t) for t in range(int(total_time))])

    # Numerical position using forward Euler
    x_numerical, y_numerical = forward_euler(dt, total_time)

    # Calculate positional error
    errors = calculate_error(x_analytical, y_analytical, x_numerical, y_numerical)

    # Plot errors over time
    plt.plot(range(int(total_time)), errors, label=f"dt={dt}")

    end_time = time.time()
    print(f"Time for dt={dt}: {end_time - start_time} seconds")

plt.title('Positional Error over Time')
plt.xlabel('Time (s)')
plt.ylabel('Positional Error')
plt.legend()
plt.show()