import numpy as np
import matplotlib.pyplot as plt
from Task7.Files.ConvTest import ConvTest
from tkinter import messagebox


def plot_signals_convolution(indices_signal1, values_signal1, indices_signal2, values_signal2,
                             conv_indices, conv_values):
    plt.figure(figsize=(10, 5))

    plt.subplot(3, 1, 1)
    plt.stem(indices_signal1, values_signal1, basefmt='b-', use_line_collection=True)
    plt.title('Signal 1')
    plt.xlabel('Indices')
    plt.ylabel('Values')

    plt.subplot(3, 1, 2)
    plt.stem(indices_signal2, values_signal2, basefmt='r-', use_line_collection=True)
    plt.title('Signal 2')
    plt.xlabel('Indices')
    plt.ylabel('Values')

    plt.subplot(3, 1, 3)
    plt.stem(conv_indices, conv_values, basefmt='g-', use_line_collection=True)
    plt.title('Convolution Result')
    plt.xlabel('Indices')
    plt.ylabel('Values')

    plt.tight_layout()
    plt.show()


def load_file(file_path):
    indices = []
    values = []

    with open(file_path, "r") as file:
        for _ in range(3):
            next(file)

        for line in file:
            n, value = line.split()
            indices.append(int(n))
            values.append(int(value))

    return np.array(indices), np.array(values)


def generate_indices(h_indices, x_indices):
    min_index = min(x_indices) + min(h_indices)
    max_index = max(x_indices) + max(h_indices)
    indices = list(range(min_index, max_index + 1))
    return indices


def calculate_convolution(x_values, x_indices, h_values, h_indices):
    len_x = len(x_values)
    len_h = len(h_values)
    leny = len_x + len_h - 1
    y = [0] * leny
    indices = generate_indices(h_indices, x_indices)

    for n in range(leny):
        min_index_x = max(0, n - (len_h - 1))
        for k in range(min_index_x, len_x):
            if 0 <= n - k < len_h:
                y[n] += x_values[k] * h_values[n - k]

    return indices, y


def convolution(file1_path, file2_path):
    indices_signal1, values_signal1 = load_file(file1_path.get())
    indices_signal2, values_signal2 = load_file(file2_path.get())

    y_indices, y_values = calculate_convolution(values_signal1, indices_signal1, values_signal2, indices_signal2)
    plot_signals_convolution(indices_signal1, values_signal1, indices_signal2, values_signal2, y_indices, y_values)

    messagebox.showinfo("Compare Signals", ConvTest(y_indices, y_values))
