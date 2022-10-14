from matplotlib import pyplot as plt


def render_plot(ts, xs, ys, zs):
    figure, axis = plt.subplots(1, 3,  figsize=(13, 4))
    axis[0].plot(ts, xs, color="red", linestyle='solid')
    axis[0].set(xlabel='x(t)', ylabel='t')
    axis[0].grid(True)

    axis[1].plot(ts, ys, color="green", linestyle='solid')
    axis[1].set(xlabel='y(t)', ylabel='t')
    axis[1].grid(True)

    axis[2].plot(ts, zs, color="blue", linestyle='solid')
    axis[2].set(xlabel='z(t)', ylabel='t')
    axis[2].grid(True)
    plt.show()
