import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from task_parameters import parameters, initial_condition, end_time, number_of_intervals
from solver import get_solution

u = get_solution(parameters, initial_condition, end_time, number_of_intervals)

x = u[:, 0][::2]  # I use [::2] because not all points x,y,t are needed to create the animation
y = u[:, 1][::2]  # For animation, I use every second point

time = np.linspace(0, end_time, number_of_intervals + 1)[::2]

dataSet = np.array([x, y])
numDataPoints = len(time)

L = parameters[1]
x_circle = np.linspace(-L, L, 500)
y_circle = -(L ** 2 - x_circle ** 2) ** 0.5


def animate_func(num):
    ax.clear()

    ax.plot(x_circle, y_circle, 'b--')
    ax.plot([0.5, -0.5], [0, 0], color='black')
    ax.plot([0, dataSet[0, num]], [0, dataSet[1, num]], c='black', marker='o')
    ax.plot(dataSet[0, num], dataSet[1, num], c='blue', marker='o')

    ax.set_xlim([-4, 4])
    ax.set_ylim([-8, 0])
    plt.grid()
    plt.axis("equal")

    ax.set_title('Time = ' + str(np.round(time[num], decimals=2)) + ' sec')
    ax.set_xlabel('x')
    ax.set_ylabel('y')


fig, ax = plt.subplots()

line_ani = animation.FuncAnimation(fig, animate_func, interval=1, frames=numDataPoints)
plt.show()

I_want_to_save_animation = False
if I_want_to_save_animation:
    f = r"pendulum_animation.gif"
    writer_gif = animation.PillowWriter(fps=30)
    line_ani.save(f, writer=writer_gif)
