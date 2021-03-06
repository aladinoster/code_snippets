"""
    It works!
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd


def plot_curves(x_data, y_data):
    fig, ax = plt.subplots()
    xadd, yadd = [], []

    bc, = ax.plot(x_data, y_data, '-', color=[0, 0, 1, 0.1], animated=True)
    ln, = ax.plot([], [], '-', lw=0.5, animated=True)

    def init():
        ax.set_xlim(0, max(x_data))
        ax.set_ylim(0, max(y_data))
        return ln, bc

    def update(frame):
        bc.set_data(x_data, y_data)
        xadd.append(x_data[frame])
        yadd.append(y_data[frame])
        ln.set_data(xadd, yadd)
        return ln, bc

    steps = range(len(x_data))

    ani = FuncAnimation(fig, update, frames=steps,
                        init_func=init, blit=True, interval=10)
    plt.grid()
    plt.show()
    return ani


def main():
    v = 25
    dt = 0.1
    t0, tf = (0, 40)
    x_data = np.arange(t0, tf + dt, dt)
    s_c = 4
    n_veh = 1
    data = pd.DataFrame(index=x_data)
    for i in range(n_veh):
        y_data = v * x_data - s_c * i
        data[i] = y_data

    print(data.head(5))
    # data.plot(color=['b'] * n_veh, alpha=0.3, animated=True)
    # plt.show()
    # x_data = np.linspace(0, 2 * np.pi, 128)
    # y_data = np.sin(x_data)
    plot_curves(x_data, y_data)
    plot_curves(x_data, [i - 3 for i in y_data])


if __name__ == "__main__":
    main()
