import numpy as np
from Task9.Files.Correlation.CompareSignal import Compare_Signals
import matplotlib.pyplot as plt

def load_file(file_path):
    values = []

    with open(file_path, "r") as file:
        for _ in range(3):
            next(file)

        for line in file:
            n, value = line.split()
            values.append(int(value))

    return values

def plot_signals_correlation(signal1, signal2, result):
    plt.figure(figsize=(10, 5))

    plt.subplot(3, 1, 1)
    plt.plot(signal1)
    plt.title('Signal 1')
    plt.xlabel('Indices')
    plt.ylabel('Values')

    plt.subplot(3, 1, 2)
    plt.plot(signal2)
    plt.title('Signal 2')
    plt.xlabel('Indices')
    plt.ylabel('Values')

    plt.subplot(3, 1, 3)
    plt.plot(result)
    plt.title('Correlation Result')
    plt.xlabel('Indices')
    plt.ylabel('Values')

    plt.tight_layout()
    plt.show()

def DFT(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-1j * 2 * np.pi * k * n / N)
        X[k] = round(X[k].real, 2) + round(X[k].imag, 2) * 1j
    return list(X)


def IDFT(x):
    N = len(x)
    time_samples = np.zeros(N, dtype=np.complex128)

    for n in range(N):
        for k in range(N):
            phase = 2 * np.pi * k * n / N
            time_samples[n] += x[k] * np.exp(1j * phase) / N

    reconstructed_signal = np.real(time_samples)

    return [round(signal) for signal in list(reconstructed_signal)]


def fast_correlation(signal1_path, signal2_path):
    signal1 = load_file(signal1_path)
    signal2 = load_file(signal2_path)

    N = len(signal1)
    X1 = DFT(signal1)
    X2 = DFT(signal2)

    X1_conjugate = np.conjugate(X1)
    FD_inverse = [X2[i] * X1_conjugate[i] for i in range(N)]
    correlation = IDFT(FD_inverse)

    correlation = [signal / N for signal in correlation]
    converted_array = [int(x) if x.is_integer() else x for x in correlation]

    Compare_Signals("Task9/Files/Correlation/Corr_Output.txt", list(range(len(converted_array))), converted_array)
    plot_signals_correlation(signal1, signal2, correlation)

# return converted_array


# signal1 = "Files/Correlation/Corr_input signal1.txt"
# signal2 = "Files/Correlation/Corr_input signal2.txt"
# print("-------------------------------------------------------------------------------------------")
# correlation_result = fast_correlation(signal1, signal2)
#
# Compare_Signals("Files/Correlation/Corr_Output.txt", list(range(len(correlation_result))), correlation_result)