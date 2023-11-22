from Task3.helper_functions import load_file
import numpy as np
import matplotlib.pyplot as plt
from Task3.Files.QuanTest2 import QuantizationTest2
from Task3.Files.QuanTest1 import QuantizationTest1


def get_levels(number, type):
    if type == "level":
        return number
    else:
        return 2 ** int(number)


def quantization(file_path, number, typ):
    signal = load_file(file_path)
    levels = get_levels(number, typ)
    generate_range(signal, levels)
    return signal, levels


def binary_search(target, array):
    sorted_array = sorted(array)

    left = 1
    right = len(sorted_array) - 1

    while left <= right:
        mid = np.round((left + right) // 2)

        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return right + 1


def generate_range(signal, levels):
    min_amp = np.min(signal)
    max_amp = np.max(signal)
    delta = (max_amp - min_amp) / levels
    ranges = [min_amp + i * delta for i in range(levels + 1)]
    return np.round(ranges, 2)


def get_interval_idx(signal, levels):
    ranges = generate_range(signal, levels)
    interval_indices = []
    for i in signal:
        x = binary_search(i, ranges)
        interval_indices.append(x)
    return interval_indices


def calculate_midpoints(indices):
    midpoints = []
    for i in range(len(indices) - 1):
        start_index = indices[i]
        end_index = indices[i + 1]
        midpoint = (start_index + end_index) / 2.0
        midpoints.append(midpoint)
    return (np.round(midpoints, 3)).tolist()


def quantized_signal(signal, levels):
    indices = get_interval_idx(signal, levels)
    ranges = generate_range(signal, levels)
    midpoints = calculate_midpoints(ranges)

    xq = []
    for i in indices:
        xq.append(midpoints[i - 1])
    return xq


def quantized_error(signal, levels):
    xq = quantized_signal(signal, levels)
    return xq - signal


def average_power_error(signal, levels):
    quantized_err = quantized_error(signal, levels)
    error = [sample ** 2 for sample in quantized_err]
    average_power = sum(error) / len(error)
    return average_power


def encoded_signal(signal, levels):
    x = get_interval_idx(signal, levels)
    num_bits = len(bin(levels - 1)) - 2  # Calculate the number of bits required
    formatted_output = [format(i - 1, f'0{num_bits}b') for i in x]
    return formatted_output

def plot(signal, quantized_signal_values, quantization_error_values):
    # Plot the original signal, quantized signal, and quantization error
    plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(signal, 'b', label='Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(quantized_signal_values, 'r', label='Quantized Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(quantization_error_values, 'g', label='Quantization Error')
    plt.xlabel('Time')
    plt.ylabel('Error')
    plt.legend()

    plt.tight_layout()
    plt.show()


class Compare:
    def __init__(self):
        signal1, levels1 = quantization("../DSP_Tasks/Task3/Files/Quan1_input.txt", 8,
                                        "level")
        signal2, levels2 = quantization("../DSP_Tasks/Task3/Files/Quan2_input.txt", 4,
                                        "level")

        QuantizationTest1("../DSP_Tasks/Task3/Files/Quan1_Out.txt",
                          encoded_signal(signal1, levels1), quantized_signal(signal1, levels1))

        QuantizationTest2("../DSP_Tasks/Task3/Files/Quan2_Out.txt",
                          get_interval_idx(signal2, levels2),
                          encoded_signal(signal2, levels2), quantized_signal(signal2, levels2),
                          quantized_error(signal2, levels2))

        plot(signal1, quantized_signal(signal1, levels1), quantized_error(signal1, levels1))
        plot(signal2, quantized_signal(signal2, levels2), quantized_error(signal2, levels2))














