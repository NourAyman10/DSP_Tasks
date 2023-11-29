import matplotlib.pyplot as plt
import numpy as np


def delay_signal(signal, k):
    delayed_signal = np.pad(signal, (k, 0), 'constant')[:-k]
    return delayed_signal


def advance_signal(signal, k):
    advanced_signal = np.pad(signal, (0, k), 'constant')[k:]
    return advanced_signal


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


signal = load_file('../Task6/Files/Input Shifting.txt')
k = int(input("Enter k steps :"))
delay = delay_signal(signal, k)
k2 = int(input("Enter k steps :"))
advance = advance_signal(signal, k2)

plt.figure(figsize=(10, 5))

plt.subplot(131)
plt.plot(signal, label='Input Signal')
plt.legend()
plt.title('Input Signal')

plt.subplot(132)
plt.plot(delay, label='Delayed Signal')
plt.legend()
plt.title('Delayed Signal')

plt.subplot(133)
plt.plot(advance, label='Advanced Signal')
plt.legend()
plt.title('Advanced Signal')

plt.tight_layout()
plt.show()
