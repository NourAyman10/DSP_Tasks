import numpy as np
import matplotlib.pyplot as plt

def load_file(file_path):
    with open(file_path, "r") as file:
        for _ in range(3):
            next(file)

        values = []
        for line in file:
            _, value = line.split()
            values.append(float(value))
        values = np.array(values)

    return values


def plot_signals(window_title, **signals):
    plt.figure()
    for title, signal in signals.items():
        plt.plot(signal, label=title)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title(window_title)
    plt.legend()
    plt.show()


def delay_signal(signal, k):
    return np.pad(signal, (k, 0), 'constant')[:-k]


def advance_signal(signal, k):
    return np.pad(signal, (0, k), 'constant')[k:]