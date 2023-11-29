import numpy as np
import matplotlib.pyplot as plt
from Files.comparesignal2 import SignalSamplesAreEqual

def moving_average(signal, num_points):
    smoothed_signal = []
    for i in range(len(signal) - num_points + 1):
        average = sum(signal[i:i + num_points]) / num_points
        smoothed_signal.append(average)
    return smoothed_signal





def plot_signals(original_signal, processed_signal, processed_name):
    
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(original_signal)
    plt.title('Original Signal')

    plt.subplot(1, 2, 2)
    plt.plot(processed_signal)
    plt.title(f'{processed_name} Signal')
    plt.tight_layout()
    plt.show()

def load_file(file_path):
    with open(file_path, "r") as file:
        # Skip the first three lines of metadata
        for _ in range(3):
            next(file)

        values = []
        for line in file:
            _, value = line.split()
            values.append(float(value))
        values = np.array(values)

    return values

signal1 =load_file('../Task6/Files/Signal1.txt')
size=int(input("Enter window size : "))
smoothed=moving_average(signal1,size)
plot_signals(signal1,smoothed,"smoothing")
SignalSamplesAreEqual('../Task6/Files/OutMovAvgTest1.txt',smoothed)

signal2=load_file('../Task6/Files/Signal2.txt')
size2=int(input("Enter window size : "))
smoothed2=moving_average(signal2,size2)
plot_signals(signal2,smoothed2,"smoothed")
SignalSamplesAreEqual('../Task6/Files/OutMovAvgTest2.txt',smoothed2)




