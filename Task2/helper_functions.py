import numpy as np
import matplotlib.pyplot as plt
from tkinter import filedialog


def load_file(file_path):
    with open(file_path, "r") as file:
        # Skip the first three lines of metadata
        for _ in range(3):
            next(file)

        values = []
        for line in file:
            _, value = line.split()
            values.append(float(value))
        values = np.array(values)

    return values


def plot_signal(signal, title):
    plt.figure()
    plt.plot(signal)
    plt.title(title)
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()


def padding(signal1, signal2):
    pad = max(len(signal1), len(signal2))
    if len(signal1) < pad:
        signal1 = signal1 + [0] * (pad - len(signal1))
    if len(signal2) < pad:
        signal2 = signal2 + [0] * (pad - len(signal2))
    return signal1, signal2


