import matplotlib.pyplot as plt
import numpy as np
from task_parameters import parameters, initial_condition, end_time, number_of_intervals
from solver import get_solution

u = get_solution(parameters, initial_condition, end_time, number_of_intervals)

x = u[:, 0]
y = u[:, 1]

time = np.linspace(0, end_time, number_of_intervals + 1)

plt.plot(time, x, label="x")
plt.plot(time, y, label="y")

plt.grid()
plt.legend()
plt.show()

length = (x ** 2 + y ** 2) ** 0.5
plt.plot(time, length, label="length")
plt.xlim(0, end_time)
plt.ylim(0, 6)
plt.grid()
plt.legend()
plt.show()
