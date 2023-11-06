import numpy as np
import matplotlib.pyplot as plt
import json
from signalcompare import SignalComapreAmplitude,SignalComaprePhaseShift
 

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

def DFT(signal):
    N=len(signal)
    X=np.zeros(N,dtype=complex)

    for k in range(N):
        for n in range(N):
            X[k]+=signal[n]*np.exp(-1j*2 *np.pi*k*n/N)
    return X

def Calculate_Amplitude_and_phaseShift(X,Frequency_samples):
    N=len(X)
    Ts=1/Frequency_samples
    amplitude=np.zeros(N)
    phaseShift=np.zeros(N)
    FundamentalFrequancy=np.zeros(N) 

    for i in range(N):
        amplitude[i]=np.sqrt((X[i].real**2)+(X[i].imag**2)) 
        phaseShift[i]=np.arctan2(X[i].imag,X[i].real) 
        FundamentalFrequancy[i]=(2*np.pi/(N*Ts)*(i+1))  


    return amplitude,phaseShift,FundamentalFrequancy     


def plot(X,Frequency_samples):
    amplitude,phase_shift,frequencies=Calculate_Amplitude_and_phaseShift(X,Frequency_samples)
    for a, p ,f in zip(amplitude, phase_shift ,frequencies):
        adjusted_phase = (p + np.pi) % (2 * np.pi) - np.pi
        print(f"{a}f\t\t{adjusted_phase}f\t\t{f}f")
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1)
    plt.stem(frequencies,amplitude)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("Visualize Between Frequency and Amplitude")

    plt.subplot(1,2,2)
    plt.stem(frequencies,phase_shift)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase Shift")
    plt.title("Visualize Between Frequency and Phase Shift")

    plt.tight_layout()
    plt.show()

    data = {'Amplitude': amplitude.tolist(), 'Phase': phase_shift.tolist()}
    with open('frequency_components.txt', 'w') as file:
        json.dump(data, file, indent=4)



signal=load_file("Task4/input_Signal_DFT.txt")
Frequency_samples=float(input("Enter the Sampling frequency in Hz : "))
X=DFT(signal)
plot(X,Frequency_samples)




# with open('frequency_components.txt', 'r') as file:
#     data = json.load(file)


# amplitude_data = data['Amplitude']
# phase_shift_data = data['Phase']


# amplitude_file_data = {'Amplitude': amplitude_data}
# with open('amplitude_data.txt', 'w') as amplitude_file:
#     json.dump(amplitude_file_data, amplitude_file, indent=4)


# phase_shift_file_data = {'Phase': phase_shift_data}
# with open('phase_shift_data.txt', 'w') as phase_shift_file:
#     json.dump(phase_shift_file_data, phase_shift_file, indent=4)



# # Read the JSON file
# with open('amplitude_data.txt', 'r') as file:
#     data = json.load(file)
# amplitude_values = data['Amplitude']

# with open('amplitude_values_rounded.txt', 'w') as output_file:
#     for value in amplitude_values:
#         rounded_amplitude= round(value, 13)  # Rounding to 13 decimal places
#         output_file.write(str(rounded_amplitude) + '\n')


# with open('phase_shift_data.txt', 'r') as file:
#     data = json.load(file)
# phase_values = data['Phase']
# with open('phase_values.txt', 'w') as output_file:
#     for value in phase_values:
#         rounded_phase=round(value,14)
#         output_file.write(str(rounded_phase) + '\n')













# amplitude_test = SignalComapreAmplitude(amplitudes, rounded_amplitude)
# phase_test = SignalComaprePhaseShift(phases, rounded_phase)  

# if amplitude_test and phase_test:
#     print("The output matches the reference signals.")
# else:
#     print("The output does not match the reference signals.")