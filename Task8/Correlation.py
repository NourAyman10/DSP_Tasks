import math
import numpy as np
import matplotlib.pyplot as plt

from Files.CompareSignal import Compare_Signals
def load_file(file_path):
    with open(file_path, "r") as file:
        
        for _ in range(3):
            next(file)

        values = []
        for line in file:
            _, value = line.split()
            values.append(float(value))
        

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

def calculate_correlation(signal1, signal2, float_point):
    N = len(signal1)
    result = []

    x1_square = [i ** 2 for i in signal1]
    x2_square = [i ** 2 for i in signal2]
    p12_denominator = math.sqrt((sum(x1_square) * sum(x2_square))) / N
    p12_denominator = round(p12_denominator, float_point)

    # from r1 to r_end
    for i in range(1, N + 1):
        signal2_shifted = signal2[i:] + signal2[0:N - (N - i)]
        print(signal2_shifted, i)
        r = round(sum([signal1[i] * signal2_shifted[i] for i in range(N)]) / N, float_point)
        p = round(r / p12_denominator, float_point)
        result.append(p)

    # r0 == r_end
    result = [result[N - 1]] + result
    indices=list(range(N))
    return indices,result[:N]


signal1=load_file('Files/Corr_input signal1.txt')
signal2=load_file('Files/Corr_input signal2.txt')

float_point = 8

indices,result = calculate_correlation(signal1, signal2, float_point)
print(result)

plot_signals_correlation(signal1, signal2, result)
Compare_Signals('Files/CorrOutput.txt',indices,result)
