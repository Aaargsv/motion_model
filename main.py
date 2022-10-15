from numerical import *
from render_plot import render_plot
from vpython import *
import math


def fx(t, x, v):
    return v, -x / 1000


def fy(t, x, v):
    return v, -x / 1000


def fz(t, x, v):
    return v, -x / 1000


def fxr(t, x, v, r):
    return v, -mu * x / (r ** 3)


def fyr(t, x, v, r):
    mu = 3.98603 * 1e14
    return v, -mu * x / (r ** 3)


def fzr(t, x, v, r):
    return v, -mu * x / (r ** 3)


if __name__ == '__main__':

    '''ts, xs, vx = runge_kutta4_2nd_order(fx, h=0.1, t_bound=1000.1, t0=0, s0=(1, 5))
    _, ys, vy = runge_kutta4_2nd_order(fy, h=0.1, t_bound=1000.1, t0=0, s0=(1, 5))
    _, zs, vz = runge_kutta4_2nd_order(fy, h=0.1, t_bound=1000.1, t0=0, s0=(1, 5))

    render_plot(ts, [xs, ys, zs, vx,  vy, vz],
                ['x(t)', 'y(t)', 'z(t)', 'vx(t)', 'vy(t)', 'vz(t)'], row=2, column=3)'''


    p = 6800 * 1e3
    e = 2e-3
    i = 45 * math.pi / 180
    omega = 0
    w = 70 * math.pi / 180
    u = 70 * math.pi / 180
    nu = 0
    mu = 3.98603 * 1e14

    r = p / (1 + e * math.cos(nu))
    x = r * (math.cos(u) * math.cos(omega) - math.sin(u) * math.sin(omega) * math.cos(i))
    y = r * (math.cos(u) * math.sin(omega) - math.sin(u) * math.cos(omega) * math.cos(i))
    z = r * math.sin(u) * math.sin(i)
    v_r = math.sqrt(mu / p) * e * math.sin(nu) / r
    v_n = math.sqrt(mu / p) * (1 + e * math.cos(nu))
    v_x = x * v_r + v_n * (-math.sin(u) * math.cos(omega) - math.cos(u) * math.sin(omega) * math.cos(i))
    v_y = y * v_r + v_n * (-math.sin(u) * math.sin(omega) - math.cos(u) * math.cos(omega) * math.cos(i))
    v_z = z * v_r + v_n * math.cos(u) * math.sin(i)

    print(x, y, z, v_x, v_y, v_z)

    ts, xs, ys, zs, vx, vy, vz = runge_kutta4_2nd_order_xyz([fxr, fyr, fzr],
                                                            h=10, t_bound=100000.1, t0=0,
                                                            s0=(x, y, z, v_x, v_y, v_z))

    render_plot(ts, [xs, ys, zs, vx, vy, vz],
                ['x(t)', 'y(t)', 'z(t)', 'vx(t)', 'vy(t)', 'vz(t)'], row=2, column=3)















    ball1 = sphere(pos=vector(x * 1e-6, y * 1e-6, z * 1e-6), radius=0.5, color=color.red, make_trail=True, trail_type="points", interval=10)

    ball2 = sphere(pos=vector(0, 0, 0),
                   radius=5, color=color.blue)

    for t, x, y, z in zip(ts, xs, ys, zs):
        rate(100)
        ball1.pos = vector(x * 1e-6, y * 1e-6, z * 1e-6)
        


