import numpy as np


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
    vs = [x]
    ts = np.arange(t0, t_bound, h)
    for t in ts[0:-1]:
        k1, l1 = func(t, x, v)
        k2, l2 = func(t + h / 2, x + h / 2 * k1, v + h / 2 * l1)
        k3, l3 = func(t + h / 2, x + h / 2 * k2, v + h / 2 * l1)
        k4, l4 = func(t + h, x + h * k3, v + h * l3)
        x += (k1 + 2 * k2 + 2 * k3 + k4) / 6 * h
        v += (l1 + 2 * l2 + 2 * l3 + l4) / 6 * h
        xs.append(x)
        vs.append(v)
    return ts.tolist(), xs, vs





