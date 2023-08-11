import numpy as np
from matplotlib import pyplot as plt
from src.signal.my_signal import Signal


plt.ion()

fig, ax = plt.subplots()
c = plt.Circle((5, 5), 5, color='#fabcbc')
ax.add_patch(c)
ax.set_aspect('equal')
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)
plt.show()

signal_x = Signal(np.pi, 50, np.pi / 3)
signal_y = Signal(np.pi * 0.5, 60, np.pi / 3 + np.pi / 2)
t = 0

for i in range(1000):
    c.set_center((signal_x(t), signal_y(t)))
    plt.show()
    t += 0.02
    plt.pause(0.02)

plt.pause(20)
