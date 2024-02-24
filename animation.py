import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

from task_parameters import parameters, initial_condition, end_time, number_of_intervals
from solver import get_solution

u = get_solution(parameters, initial_condition, end_time, number_of_intervals)

x = u[:, 0][::2]
y = u[:, 1][::2]
time = np.linspace(0, end_time, number_of_intervals + 1)[::2]

positions = np.array([x, y])
num_positions = len(time)

L = parameters[1]
x_circle = np.linspace(-L, L, 500)
y_circle = -(L ** 2 - x_circle ** 2) ** 0.5


def animate_func(num):
    ax.clear()

    ax.plot(x_circle, y_circle, 'b--')
    ax.plot([0, 0], [0.5, -0.5], color='black')
    ax.plot([0.5, -0.5], [0, 0], color='black')
    ax.plot([0, positions[0, num]], [0, positions[1, num]], c='black', marker='o')
    ax.plot(positions[0, num], positions[1, num], c='blue', marker='o')

    ax.set_xlim([-4, 4])
    ax.set_ylim([-8, 0])
    plt.xticks(np.linspace(-6, 6, 13))
    plt.grid()
    plt.axis('equal')

    ax.set_title('Time = ' + str(np.round(time[num], decimals=2)) + ' [sec]')
    ax.set_xlabel('x, [m]')
    ax.set_ylabel('y, [m]')


fig, ax = plt.subplots()
line_ani = animation.FuncAnimation(fig, animate_func, interval=10, frames=num_positions)

# Что бы сохранить анимацию требуется заменить "False" на "True"
I_want_to_save_animation = False
if I_want_to_save_animation:
    f = r"pendulum_animation.gif"
    writer_gif = animation.PillowWriter(fps=30)
    line_ani.save(f, writer=writer_gif)
else:
    plt.show()
