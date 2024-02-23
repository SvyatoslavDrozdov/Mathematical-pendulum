# Parameters of pendulum
m = 1
L = 5
parameters = [m, L]

# Initial condition
x_0 = 3
y_0 = -4
v_0 = 1
v_x0 = - v_0 * abs(y_0) / (x_0 ** 2 + y_0 ** 2) ** 0.5
v_y0 = - v_0 * abs(x_0) / (x_0 ** 2 + y_0 ** 2) ** 0.5
initial_condition = [x_0, y_0, v_x0, v_y0]

# Time parameters
quasi_period = 2 * 3.146 * (L / 9.81) ** 0.5
# end_time = 2 * quasi_period
end_time = 10
number_of_intervals = 1000
