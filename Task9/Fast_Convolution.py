import numpy as np
import matplotlib.pyplot as plt
from Task9.Files.Convolution.ConvTest import ConvTest


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


def DFT(signal):
    N = len(signal)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k] += signal[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    return X


def IDFT(frequency_domain_signal):
    N = len(frequency_domain_signal)
    idft_result = []
    for n in range(N):
        x_n = 0
        for k in range(N):
            x_n += frequency_domain_signal[k] * np.exp(2j * np.pi * k * n / N)
        x_n /= N
        idft_result.append(x_n)
    return idft_result


def FastConvolution(signal1_path, signal2_path):
    indices_signal1, samples_signal1 = load_file(signal1_path)
    indices_signal2, samples_signal2 = load_file(signal2_path)

    N1 = len(samples_signal1)
    N2 = len(samples_signal2)
    N = N1 + N2 - 1
    signal1 = np.pad(samples_signal1, (0, N - N1))
    signal2 = np.pad(samples_signal2, (0, N - N2))

    signal1_dft = DFT(signal1)
    signal2_dft = DFT(signal2)
    convolution_freq_domain = [a * b for a, b in zip(signal1_dft, signal2_dft)]
    convolution_time_domain = IDFT(convolution_freq_domain)

    convolution_indices = indices_signal1[0] + indices_signal2[0] + np.arange(N)
    convolution_samples_real = [x.real for x in convolution_time_domain]

    ConvTest(convolution_indices, convolution_samples_real)
    plot_signals_convolution(indices_signal1, samples_signal1, indices_signal2, samples_signal2, convolution_indices,
                             convolution_samples_real)
    # return convolution_indices, convolution_samples_real


# signal1 = 'Files/Convolution/Input_conv_Sig1.txt'
# signal2 = 'Files/Convolution/Input_conv_Sig2.txt'
# indices_signal1, samples_signal1 = load_file(signal1)
# indices_signal2, samples_signal2 = load_file(signal2)
# convolution_indices, convolution_samples = FastConvolution(indices_signal1, samples_signal1, indices_signal2,
#                                                            samples_signal2)
# ConvTest(convolution_indices, convolution_samples)
# plot_signals_convolution(indices_signal1, samples_signal1, indices_signal2, samples_signal2, convolution_indices,
#                          convolution_samples)
