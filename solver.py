import numpy as np


def get_solution(parameters, initial_condition, end_time, number_of_intervals):
    m = parameters[0]
    L = parameters[1]
    x_0 = initial_condition[0]
    y_0 = initial_condition[1]
    v_x0 = initial_condition[2]
    v_y0 = initial_condition[3]

    def g(t):
        return 9.81 + 0.05 * np.sin(2 * np.pi * t)

    T_0 = m * L * (v_x0 ** 2 + v_y0 ** 2 - y_0 * g(0)) / (x_0 ** 2 + y_0 ** 2)

    def f(vector_u, t):
        vector_f = np.zeros(5)
        vector_f[0] = vector_u[2]
        vector_f[1] = vector_u[3]
        vector_f[2] = - vector_u[0] * vector_u[4] / (m * L)
        vector_f[3] = -vector_u[1] * vector_u[4] / (m * L) - g(t)
        vector_f[4] = vector_u[0] ** 2 + vector_u[1] ** 2 - L ** 2
        return vector_f

    def D():
        matrix_D = np.zeros((5, 5))
        for i in range(0, 4):
            matrix_D[i][i] = 1
        return matrix_D

    def df_du(vector_u):
        jacobian_matrix = np.zeros((5, 5))
        jacobian_matrix[0][2] = 1
        jacobian_matrix[1][3] = 1
        jacobian_matrix[2][0] = - vector_u[4] / (m * L)
        jacobian_matrix[2][4] = -vector_u[0] / (m * L)
        jacobian_matrix[3][1] = - vector_u[4] / (m * L)
        jacobian_matrix[3][4] = - vector_u[1] / (m * L)
        jacobian_matrix[4][0] = 2 * vector_u[0]
        jacobian_matrix[4][1] = 2 * vector_u[1]
        return jacobian_matrix

    tau = end_time / number_of_intervals
    time = np.linspace(0, end_time, number_of_intervals + 1)

    u = np.zeros((number_of_intervals + 1, 5))
    u[0] = np.array([x_0, y_0, v_x0, v_y0, T_0])

    alpha = (1 + 1j) / 2

    for time_point in range(number_of_intervals):
        w = np.linalg.solve(D() - alpha * tau * df_du(u[time_point]), f(u[time_point], time[time_point] + tau / 2))
        u[time_point + 1] = u[time_point] + tau * w.real

    return u
