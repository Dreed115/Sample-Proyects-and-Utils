import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

a, b, c = 0.2, 0.2, 5.7

# Define your difference equation for a 3D harmonic oscillator
def difference_equation_3d(x, y, z):
    omega = 1.0
    h = 0.01
    delta_t = 0.1
    xk1 = x + h*(-y-z)
    yk1 = y + h*(x+a*y)
    zk1 = z + h*(b+z*(x-c))
    x1= x + (h/2)*(-y-z + (-yk1-zk1))
    y1= y + (h/2)*(x+a*y + (xk1+a*yk1))
    z1= z + (h/2)*(b+z*(x-c) + (b+zk1*(xk1-c)))
    return x1, y1, z1

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], 'bo', markersize=1, marker=".")  # Assuming a point particle for simplicity

# Set the axis limits
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_zlim(0, 20)

# Initialize the data
x_data, y_data, z_data = [], [], []

# Animation function
def update(frame):
    global x_data, y_data, z_data
    if frame == 0:
        x, y, z = 1.0, 1.0, 1.0  # Initial conditions
    else:
        x, y, z = difference_equation_3d(x_data[-1], y_data[-1], z_data[-1])

    x_data.append(x)
    y_data.append(y)
    z_data.append(z)

    line.set_data(x_data, y_data)
    line.set_3d_properties(z_data)
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=10000, interval=50, blit=True)

#Save the animation
animation.save('animation.mp4', writer='ffmpeg', fps=30)

# Show the animation
plt.show()
