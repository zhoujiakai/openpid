import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
T = 30
setpoint = 1.0

# 切换到"无 Ki"版本，让系统本性暴露
Kp, Ki, Kd = 0.3, 0.0, 0.05

plt.figure(figsize=(10, 5))

for tau, label, ls in [(2.0, 'tau=2', '-'), (5.0, 'tau=5', '--')]:
    y = 0.0
    integral = 0.0
    prev_error = 0.0
    t_hist, y_hist = [], []

    for step in range(int(T / dt)):
        t = step * dt
        error = setpoint - y
        integral += error * dt
        derivative = (error - prev_error) / dt
        u = Kp * error + Ki * integral + Kd * derivative
        y += (u - y) / tau * dt
        prev_error = error
        t_hist.append(t)
        y_hist.append(y)

    plt.plot(t_hist, y_hist, ls, label=label, linewidth=2)

plt.axhline(setpoint, color='gray', linestyle=':', alpha=0.5)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title(f'Kp={Kp}, Ki={Ki}, Kd={Kd} — "Ki off, compare system dynamics"')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()