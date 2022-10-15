import numpy as np
import math


def runge_kutta4(func, h, t_bound, t0, x0):
    x = x0
    xs = [x0]
    ts = np.arange(t0, t_bound, h)
    for t in ts[0:-1]:
        k1 = func(t, x)
        k2 = func(t + h / 2, x + h / 2 * k1)
        k3 = func(t + h / 2, x + h / 2 * k2)
        k4 = func(t + h, x + h * k3)
        x += (k1 + 2 * k2 + 2 * k3 + k4) / 6 * h
        xs.append(x)
    return ts.tolist(), xs


def runge_kutta4_2nd_order(func, h, t_bound, t0, s0):
    x, v = s0
    xs = [x]
    vs = [v]
    ts = np.arange(t0, t_bound, h)
    for t in ts[0:-1]:
        k1, l1 = func(t, x, v)
        k2, l2 = func(t + h / 2, x + h / 2 * k1, v + h / 2 * l1)
        k3, l3 = func(t + h / 2, x + h / 2 * k2, v + h / 2 * l2)
        k4, l4 = func(t + h, x + h * k3, v + h * l3)
        x += (k1 + 2 * k2 + 2 * k3 + k4) / 6 * h
        v += (l1 + 2 * l2 + 2 * l3 + l4) / 6 * h
        xs.append(x)
        vs.append(v)
    return ts.tolist(), xs, vs


def one_step(func, t, x, v, h, *args):
    r = args[0]
    k1, l1 = func(t, x, v, r)
    k2, l2 = func(t + h / 2, x + h / 2 * k1, v + h / 2 * l1, r)
    k3, l3 = func(t + h / 2, x + h / 2 * k2, v + h / 2 * l2, r)
    k4, l4 = func(t + h, x + h * k3, v + h * l3, r)
    x_next = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6 * h
    v_next = v + (l1 + 2 * l2 + 2 * l3 + l4) / 6 * h
    return x_next, v_next


def runge_kutta4_2nd_order_xyz(funcs, h, t_bound, t0, s0):
    x, y, z, vx, vy, vz = s0
    xs = [x]
    ys = [y]
    zs = [z]
    vxs = [vx]
    vys = [vy]
    vzs = [vz]

    ts = np.arange(t0, t_bound, h)
    for t in ts[0:-1]:
        r = math.sqrt(x**2 + y**2 + z**2)
        #r = 10
        x, vx = one_step(funcs[0], t, x, vx, h,  r)
        y, vy = one_step(funcs[1], t, y, vy, h,  r)
        z, vz = one_step(funcs[2], t, z, vz, h,  r)

        xs.append(x)
        vxs.append(vx)
        ys.append(y)
        vys.append(vy)
        zs.append(z)
        vzs.append(vz)

    return ts.tolist(), xs, ys, zs, vxs, vys, vzs







