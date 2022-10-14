import numpy as np


def runge_kutta4(func, h, t_bound, t0, x0):
    x = x0
    xs = [x0]
    ts = np.arange(t0, t_bound, h)
    for t in ts[0:-1]:
        k1 = func(x, t)
        k2 = func(x + h / 2 * k1, t + h / 2)
        k3 = func(x + h / 2 * k2, t + h / 2)
        k4 = func(x + h * k3, t + h)
        x = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6 * h
        xs.append(x)
    return ts.tolist(), xs






