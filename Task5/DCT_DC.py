import numpy as np
import matplotlib.pyplot as plt
from comparesignal2 import SignalSamplesAreEqual


def compute_DCT(input_signal):
    N = len(input_signal)
    dct_result = np.zeros(N)
    for k in range(N):
        sum_val = 0.0
        for n in range(N):
            sum_val += input_signal[n] * np.cos((np.pi / (4 * N)) * (2 * n - 1) * (2 * k - 1))
        dct_result[k] = sum_val * np.sqrt(2 / N)
    return dct_result


def remove_DC(signal):
    avg = np.mean(signal)
    return np.round((signal - avg), 3)


def save_coefficients_to_file(coefficients, m):
    with open("selected_coefficients.txt", "w") as file:
        for i in range(m):
            file.write(f"{coefficients[i]}\n")


def plot_signal_frequency_domain(signal):
    plt.figure(figsize=(8, 4))
    plt.title("Frequency Domain Signal (DCT)")
    dct_result = compute_DCT(signal)
    plt.plot(dct_result)
    plt.xlabel("Frequency Index (k)")
    plt.ylabel("Magnitude")
    plt.show()


def plot_signal_without_dc(signal, signal_without_dc):
    plt.figure(figsize=(8, 4))
    plt.subplot(2, 1, 1)
    plt.title("Time Domain Signal")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.plot(signal)
    plt.subplot(2, 1, 2)
    plt.title("Signal without DC Component")
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.plot(signal_without_dc)
    plt.tight_layout()
    plt.show()


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


signal = load_file('Task5/DCT/DCT_input.txt')
plot_signal_frequency_domain(signal)
m = int(input("Enter the number of coefficients to save: "))
dct_result = compute_DCT(signal)
print(dct_result)
save_coefficients_to_file(dct_result, m)

print(f"Saved first {m} coefficients to 'selected_coefficients.txt'")
signal_Dc = load_file('Task5/Remove DC component/DC_component_input.txt')
signal_without_dc = remove_DC(signal_Dc)
print(signal_without_dc)
plot_signal_without_dc(signal_Dc, signal_without_dc)

DCT_OUTPUT = 'Task5/DCT/DCT_output.txt'
DCT = SignalSamplesAreEqual(DCT_OUTPUT, dct_result)

DC_OUTPUT = 'Task5/Remove DC component/DC_component_output.txt'
DC_REMOVE = SignalSamplesAreEqual(DC_OUTPUT, signal_without_dc)
