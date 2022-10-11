from numerical import runge_kutta4
from matplotlib import pyplot as plt
import math

if __name__ == '__main__':
    def func(x, t):
        return t * math.sqrt(x)

    ts, xs = runge_kutta4(func, h=0.1, t_bound=10.1, t0=0, x0=1)
    _, ys = runge_kutta4(func, h=0.1, t_bound=10.1, t0=0, x0=1)
    _, zs = runge_kutta4(func, h=0.1, t_bound=10.1, t0=0, x0=1)

    figure, axis = plt.subplots(1, 3)

    plt.plot(ts, xs, color="red",  linestyle='solid')
    plt.ylabel("x(t)")
    plt.xlabel("t")
    plt.show()

