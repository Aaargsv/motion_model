from numerical import runge_kutta4
from render_plot import render_plot
from vpython import *
import math

if __name__ == '__main__':
    def func(x, t):
        return t * math.sqrt(x)

    ts, xs = runge_kutta4(func, h=0.1, t_bound=10.1, t0=0, x0=1)
    _, ys = runge_kutta4(func, h=0.1, t_bound=10.1, t0=0, x0=1)
    _, zs = runge_kutta4(func, h=0.1, t_bound=10.1, t0=0, x0=1)

    render_plot(ts, xs, ys, zs)

