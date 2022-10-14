from matplotlib import pyplot as plt


def render_plot(ts, ys, axs_names, row, column):
    figure, axis = plt.subplots(row, column,  figsize=(4.5*column, 4*row))
    for axs, y, an in zip(axis.flatten(), ys, axs_names):
        axs.plot(ts, y, linestyle='solid')
        axs.set(xlabel=an, ylabel='t')
        axs.grid(True)
    plt.show()
