from numerical import *
from render_plot import render_plot
from vpython import *
import math


def fx(t, x, v):
    return v, -x / 10


def fy(t, x, v):
    return v, -x / 10


def fz(t, x, v):
    return v, -x / 10


def fxr(t, x, v, r):
    return v, -10 * x / (r ** 3)


def fyr(t, x, v, r):
    return v, -0.01 * x / (r ** 3)


def fzr(t, x, v, r):
    return v, -10 * x / (r ** 3)


if __name__ == '__main__':
    '''ts, xs, vx = runge_kutta4_2nd_order(fx, h=0.1, t_bound=1000.1, t0=0, s0=(1, 5))
    _, ys, vy = runge_kutta4_2nd_order(fy, h=0.1, t_bound=1000.1, t0=0, s0=(1, 5))
    _, zs, vz = runge_kutta4_2nd_order(fy, h=0.1, t_bound=1000.1, t0=0, s0=(1, 5))

    render_plot(ts, [xs, ys, zs, vx,  vy, vz],
                ['x(t)', 'y(t)', 'z(t)', 'vx(t)', 'vy(t)', 'vz(t)'], row=2, column=3)'''

    ts, xs, ys, zs, vx, vy, vz = runge_kutta4_2nd_order_xyz([fxr, fyr, fzr],
                                                            h=0.1, t_bound=1000.1, t0=0,
                                                            s0=(1, 1, 1, 5, 2, -2))

    render_plot(ts, [xs, ys, zs, vx, vy, vz],
                ['x(t)', 'y(t)', 'z(t)', 'vx(t)', 'vy(t)', 'vz(t)'], row=2, column=3)

    ball1 = sphere(pos=vector(1, 1, 1), radius=0.5, color=color.red, make_trail=True, trail_type="points", interval=10)

    ball2 = sphere(pos=vector(0, 0, 0),
                   radius=0.1, color=color.blue)

    i = 0
    for t, x, y, z in zip(ts, xs, ys, zs):
        rate(100)
        ball1.pos = vector(x, y, z)
        print(t)

