import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Files.ConvTest import ConvTest

def plot_signals_convolution(indices_signal1, values_signal1, indices_signal2, values_signal2, conv_indices, conv_values):
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

def convolution(x, h):
    lenx = len(x)
    lenh = len(h)
    leny = lenx + lenh - 1
    y = [0] * leny
    indices = [0] * leny

    for n in range(leny):
        min_index_x = max(0, n - (lenh - 1))
        max_index_x = min(lenx - 1, n)
        min_index_h = max(0, (lenh - 1) - n)
        max_index_h = min(lenh - 1, n)

        if min_index_x + min_index_h <= n <= max_index_x + max_index_h:
            indices[n] = n - (lenh - 1)

        for k in range(min_index_x, lenx):
            if n - k >= 0 and n - k < lenh:
                y[n] += x[k] * h[n - k]

    return indices, y

file_path_signal1 = "Task7/Files/Input_conv_Sig1.txt"
file_path_signal2 = "Task7/Files/Input_conv_Sig2.txt"

indices_signal1, values_signal1 = load_file(file_path_signal1)
indices_signal2, values_signal2 = load_file(file_path_signal2)


indices,y=convolution(values_signal1,values_signal2) 

print(indices)
print(y)

plot_signals_convolution(indices_signal1,values_signal1,indices_signal2,values_signal2,indices,y)

ConvTest(indices,y)