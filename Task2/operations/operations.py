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


def addition(signal1, signal2):
    signal1, signal2 = padding(signal1, signal2)
    result_addition = signal1 + signal2
    plot_signal(result_addition, "Addition Result")
    return result_addition


def subtraction(signal1, signal2):
    signal1, signal2 = padding(signal1, signal2)
    result_subtraction = abs(signal1 - signal2)
    plot_signal(result_subtraction, "Subtraction Result")
    return result_subtraction


def multiplication(signal, constant):
    result_multiplication = signal * constant
    plot_signal(result_multiplication, f"Multiplication Result (Constant = {constant})")
    return result_multiplication


def squaring(signal):
    result_squaring = signal ** 2
    plot_signal(result_squaring, "Squaring Result")
    return result_squaring


signal1 = load_file("input signals/Signal1.txt")
signal2 = load_file("input signals/Signal2.txt")
signal3 = load_file("input signals/signal3.txt")

result_addition = addition(signal1, signal2)
result_addition2 = addition(signal1, signal3)
result_subtraction = subtraction(signal1, signal2)
result_subtraction2 = subtraction(signal1, signal3)
result_multiplication = multiplication(signal1, 5)
result_multiplication2 = multiplication(signal2, 10)
result_inverted = multiplication(signal2, -1)
result_squaring = squaring(signal1)

np.savetxt("output signals/Signal1+signal2.txt", result_addition)
np.savetxt("output signals/signal1+signal3.txt", result_addition2)
np.savetxt("output signals/signal1-signal2.txt", result_subtraction)
np.savetxt("output signals/signal1-signal3.txt", result_subtraction2)
np.savetxt("output signals/MultiplySignalByConstant-Signal1 - by 5.txt", result_multiplication)
np.savetxt("output signals/MultiplySignalByConstant-signal2 - by 10.txt", result_multiplication2)
np.savetxt("output signals/MultiplySignalByConstant-signal2 - by 10.txt", result_inverted)
np.savetxt("output signals/Output squaring signal 1.txt", result_squaring)
