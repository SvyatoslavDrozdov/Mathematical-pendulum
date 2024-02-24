import matplotlib.pyplot as plt
import numpy as np
from task_parameters import parameters, initial_condition, end_time, number_of_intervals
from solver import get_solution

u = get_solution(parameters, initial_condition, end_time, number_of_intervals)
time = np.linspace(0, end_time, number_of_intervals + 1)
x = u[:, 0]
y = u[:, 1]
v_x = u[:, 2]
v_y = u[:, 3]


def plot_y_t():
    """
    Данная функция создает график зависимости положения ординаты математического маятника от времени y(t).
    """

    plt.plot(time, y, label="y(t)")
    plt.ylabel("displacement, [m]")
    plt.xlabel("time, [sec]")
    plt.grid()
    plt.legend()
    plt.show()


plot_y_t()


def plot_length_t():
    """
    Данная функция создает график зависимости длины математического маятника от времени L(t) = (x(t)^2 + y(t)^2)^0.5.
    """
    length = (x ** 2 + y ** 2) ** 0.5
    plt.plot(time, length, label="L(t)")
    L = parameters[1]
    plt.plot([0, end_time], [L, L], label="$L_0$", color="red")
    plt.ylabel("length, [m]")
    plt.xlabel("time, [sec]")
    plt.xlim(0, end_time)
    plt.ylim(0, 10)
    plt.grid()
    plt.legend()
    plt.show()


plot_length_t()


def convergence_L(num_interval_vector):
    """
    Данная функция создает график сходимости в следующих осях:
    По оси абсцисс откладывается количество интервалов, на которые разбивается промежуток времени [0, t_end].
    По оси ординат откладываются значения средней величины длины маятника для каждого решения задачи, соответствующего
    конкретному разбиению промежутка времени [0, t_end].

    :param num_interval_vector: Например, [100, 200, 300...]- список, элементами которого являются значения количества
    интервалов, на которые разбивается промежуток времени [0, t_end]. Для каждого из них решается задача и находится
    среднее значение длины маятника.
    """
    average_length = []
    for num_interval in num_interval_vector:
        u_for_conv = get_solution(parameters, initial_condition, end_time, num_interval)
        x_for_conv = u_for_conv[:, 0]
        y_for_conv = u_for_conv[:, 1]

        length_for_conv = (x_for_conv ** 2 + y_for_conv ** 2) ** 0.5
        av_length = sum(length_for_conv) / len(length_for_conv)
        average_length.append(av_length)

    plt.grid()
    plt.plot(num_interval_vector, average_length)
    plt.ylabel("⟨L⟩, [m]")
    plt.xlabel("N")
    plt.show()


convergence_L(range(100, 1000, 20))


def convergence_y_max(num_interval_vector):
    """
    Данная функция создает график сходимости в следующих осях:
    По оси абсцисс откладывается количество интервалов, на которые разбивается промежуток времени [0, t_end].
    По оси ординат откладываются значения максимальной высоты маятника y_max на последнем периоде колебаний для каждого
    решения задачи, соответствующего конкретному разбиению промежутка времени [0, t_end].

    :param num_interval_vector: Например, [100, 200, 300...]- список, элементами которого являются значения количества
    интервалов, на которые разбивается промежуток времени [0, t_end]. Для каждого из них решается задача и находится
    значение максимальной высоты маятника y_max на последнем периоде.
    """
    y_max_vector = []
    for num_interval in num_interval_vector:
        u_for_conv = get_solution(parameters, initial_condition, end_time, num_interval)
        y_for_conv = u_for_conv[:, 1]
        L_0 = parameters[1]
        y_max = -L_0

        tau = end_time / num_interval
        points_in_period = int(5 / tau)
        for i in range(1, points_in_period):
            if y_for_conv[-i] >= y_max:
                y_max = y_for_conv[-i]

        y_max_vector.append(y_max)

    plt.grid()
    plt.plot(num_interval_vector, y_max_vector)
    plt.ylabel("$y_m$$_a$$_x$, [m]")
    plt.xlabel("N")
    plt.show()


convergence_y_max(range(100, 1000, 20))
