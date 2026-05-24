import numpy as np
import matplotlib.pyplot as plt

# 你的"电机"：一阶系统 G(s) = 1/(τs + 1)
tau = 5.0  # 时间常数
dt = 0.1  # 仿真步长
T = 30  # 仿真时长

# PID 参数
Kp, Ki, Kd = 0.3, 0.1, 0.05

setpoint = 1.0  # 目标值
y = 0.0  # 当前输出
integral = 0.0
prev_error = 0.0

t_hist, y_hist = [], []

for step in range(int(T / dt)):
    t = step * dt
    error = setpoint - y
    integral += error * dt
    derivative = (error - prev_error) / dt
    u = Kp * error + Ki * integral + Kd * derivative

    # 电机动力学：一阶欧拉近似
    y += (u - y) / tau * dt

    prev_error = error
    t_hist.append(t)
    y_hist.append(y)

plt.plot(t_hist, y_hist)
plt.axhline(setpoint, color='r', linestyle='--')
plt.title(f"PID: Kp={Kp}, Ki={Ki}, Kd={Kd}")
plt.show()