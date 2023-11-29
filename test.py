import matplotlib.pyplot as plt
import numpy as np
from Task6.helper_functions import load_file
from Task6.helper_functions import plot_signals
from Task6.helper_functions import delay_signal
from Task6.helper_functions import advance_signal

def fold_signal(signal):
    return signal[::-1]


def plot_signal(**signals):
    plt.figure()
    for title, signal in signals.items():
        plt.plot(signal, label=title)
    plt.xlabel('Index')
    plt.ylabel('Value')
    # plt.title('Original Signal vs. Folded Signal')
    plt.legend()
    plt.show()


def remove_DC_frequency(signal):
    N = len(signal)
    dft_signal = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            phase_shift = 2 * np.pi * k * n
            dft_signal[k] += signal[n] * np.exp(-1j * phase_shift / N)

    # Set DC component to zero
    dft_signal[0] = 0

    # Compute the IDFT manually
    dc_removed_signal = np.zeros(N, dtype=np.float_)
    for n in range(N):
        for k in range(N):
            phase_shift = 2 * np.pi * k * n
            dc_removed_signal[n] += dft_signal[k] * np.exp(1j * phase_shift / N)

    dc_removed_signal = dc_removed_signal.real / N

    return dc_removed_signal


def sharpening_signal(signal):
    # Compute first derivative
    y_first = np.zeros_like(signal)
    y_first[0] = signal[0]  # First element remains the same
    for n in range(1, len(signal)):
        y_first[n] = signal[n] - signal[n - 1]

    # Compute second derivative
    y_second = np.zeros_like(signal)
    y_second[0] = signal[0]  # First element remains the same
    y_second[-1] = signal[-1]  # Last element remains the same
    for n in range(1, len(signal) - 1):
        y_second[n] = signal[n + 1] - 2 * signal[n] + signal[n - 1]

    plot_signals("Original Signal VS First Derivative VS Second Derivative", Original_Signal=signal, First_Derivative=y_first, Second_Derivative=y_second)


signal = load_file("D:\CS\semester7\DSP\Code\DSP_Tasks\Task6\TestCases\Remove DC component\DC_component_input.txt")

# folded_signal = fold_signal(signal)

# plot_signal(Original_Signal=signal, Folded_Signal=folded_signal)
#
# removed_DC_signal = remove_DC_frequency(signal)
#
# plot_signal(Original_Signal=signal, Removed_DC_Signal=removed_DC_signal)

sharpening_signal(signal)

