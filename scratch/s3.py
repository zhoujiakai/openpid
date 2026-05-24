import numpy as np
import matplotlib.pyplot as plt

Kp = 1.0  # 只玩这个
speed = 0  # 电机现在 0 转
goal = 100  # 目标 100 转
speeds = []  # 记录每一秒的速度

for i in range(200):  # 200 轮，每轮 0.1 秒，总共 20 秒
    error = goal - speed  # 差多少
    throttle = Kp * error  # 给多少油门

    friction = 0.1 * speed  # 阻力
    speed = speed + (throttle - friction) * 0.1  # 新转速

    speeds.append(speed)

import matplotlib.pyplot as plt

plt.plot(speeds)
plt.axhline(y=100, color='r', linestyle='--')
plt.show()