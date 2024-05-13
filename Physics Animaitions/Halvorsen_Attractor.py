import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

a = 2

# Define your difference equation for a 3D harmonic oscillator
def difference_equation_3d(x, y, z):
    h = 0.01
    xk1 = x + h*(-a*x -(4+y)*y -4*z)
    yk1 = y + h*(-4*x -a*y -(4+z)*z)
    zk1 = z + h*(-(4+x)*x -4*y -a*z)
    #Euler method
    x1= x + (h/2)*(-a*x -(4+y)*y -4*z + (-a*xk1 -(4+yk1)*yk1 -4*zk1))
    y1= y + (h/2)*(-4*x -a*y -(4+z)*z + (-4*xk1 -a*yk1 -(4+zk1)*zk1))
    z1= z + (h/2)*(-(4+x)*x -4*y -a*z + (-(4+xk1)*xk1 -4*yk1 -a*zk1))
    return x1, y1, z1

# Set up the figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
line, = ax.plot([], [], [], 'bo', markersize=1, marker=".")  # Assuming a point particle for simplicity

# Set the axis limits
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.set_zlim(-20, 10)

# Initialize the data
x_data, y_data, z_data = [], [], []

# Animation function
def update(frame):
    global x_data, y_data, z_data
    if frame == 0:
        x, y, z = -1.48, -1.51, 2.04  # Initial conditions
    else:
        x, y, z = difference_equation_3d(x_data[-1], y_data[-1], z_data[-1])

    x_data.append(x)
    y_data.append(y)
    z_data.append(z)

    line.set_data(x_data, y_data)
    line.set_3d_properties(z_data)

    ax.view_init(elev=30, azim=frame * 0.1)
    return line,

# Create the animation
animation = FuncAnimation(fig, update, frames=2000, interval=50, blit=True)

#Save the animation
animation.save('Halvorsen_Attractor.mp4', writer='ffmpeg', fps=30)

# Show the animation
plt.show()
