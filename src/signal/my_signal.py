from typing import Any
import numpy as np
from matplotlib import pyplot as plt


class Signal:
    def __init__(self, omega: float, amp: float, phase: float) -> None:
        self.omega = omega
        self.amp = amp
        self.phase = phase

    def __call__(self, t: float) -> Any:
        return self.amp * np.sin(self.omega * t + self.phase)


class Ball:
    def __init__(self, r: float) -> None:
        self.r = r
        self.X = np.zeros((2, 1))


class Animation:
    def __init__(self, ball_r: float) -> None:
        self.fig, self.ax = plt.subplots()
        self.object = Ball(r=ball_r)

    def animate(self):
        self.ax.scatter(self.object.X[0, 0], self.object.X[1, 0], s=self.object.r)


def main():
    animation = Animation(ball_r=100)
    animation.animate()
    plt.show()


if __name__ == '__main__':
    main()
