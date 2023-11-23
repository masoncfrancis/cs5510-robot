import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

class AckermannModel:
   def __init__(self, wheelbase, trackwidth):
       self.wheelbase = wheelbase
       self.trackwidth = trackwidth
       self.state = np.array([0, 0, 0, 0]) # [x, y, theta, psi]

   def step(self, v, psi_dot):
       # Calculate the new state
       x, y, theta, psi = self.state
       dt = 1/2 # 2Hz
       dx = v * np.cos(theta) * dt
       dy = v * np.sin(theta) * dt
       dtheta = v * np.tan(psi) / self.wheelbase * dt
       dpsi = psi_dot * dt

       # Update the state
       self.state = np.array([x + dx, y + dy, theta + dtheta, psi + dpsi])

   def get_state(self):
       return self.state

if __name__ == "__main__":
    model = AckermannModel(10.668, 3.048)

    # mpl.use('TkAgg')

    radius = 18
    velocity = 8
    angular_velocity = velocity / radius

    # Generate commands for 10 seconds
    time = np.arange(0, 10, 0.05)
    commands = angular_velocity * np.ones_like(time)

    print(commands)

    for t, command in zip(time, commands):
        model.step(velocity, command)

    # Get the state
    state = model.get_state()

    # Plot the path
    plt.figure()
    plt.plot(state[0], state[1])
    plt.title('Path')
    plt.xlabel('x')
    plt.ylabel('y')

    # Plot the trajectory
    plt.figure()
    plt.plot(state[0], state[1], state[2])
    plt.title('Trajectory')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show(block=True)


