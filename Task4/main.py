import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from Task4.modification import Modification
from Task4.helper_functions import load_file
from Task4.signalcompare import SignalComapreAmplitude, SignalComaprePhaseShift


def DFT(file):
    try:
        signal = load_file(file.get())
        N = len(signal)
        X = np.zeros(N, dtype=complex)

        for k in range(N):
            for n in range(N):
                X[k] += signal[n] * np.exp(-1j * 2 * np.pi * k * n / N)
        return X
    except:
        messagebox.showerror("File Error", "Please Choose File First")
    compare()


def Calculate_Amplitude_and_phaseShift(X, Frequency_samples):
    N = len(X)
    Ts = 1 / Frequency_samples
    amplitude = np.zeros(N)
    phaseShift = np.zeros(N)
    FundamentalFrequancy = np.zeros(N)

    for i in range(N):
        amplitude[i] = np.sqrt((X[i].real ** 2) + (X[i].imag ** 2))
        phaseShift[i] = np.arctan2(X[i].imag, X[i].real)
        FundamentalFrequancy[i] = (2 * np.pi / (N * Ts) * (i + 1))

    return amplitude, phaseShift, FundamentalFrequancy


def plot(X, Frequency_samples):
    amplitude, phase_shift, frequencies = Calculate_Amplitude_and_phaseShift(X, Frequency_samples)
    for a, p, f in zip(amplitude, phase_shift, frequencies):
        adjusted_phase = (p + np.pi) % (2 * np.pi) - np.pi
        print(f"{a}f\t\t{adjusted_phase}f\t\t{f}f")
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.stem(frequencies, amplitude)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title("Visualize Between Frequency and Amplitude")

    plt.subplot(1, 2, 2)
    plt.stem(frequencies, phase_shift)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase Shift")
    plt.title("Visualize Between Frequency and Phase Shift")

    plt.tight_layout()
    plt.show()


def modify_signal(file):
    X = DFT(file)
    Modification(X)


def generate_fourier_transform(file, Frequency_samples):
    Freq_samples = float(Frequency_samples.get())

    X = DFT(file)
    amplitude, phase_shift, frequencies = Calculate_Amplitude_and_phaseShift(X, Freq_samples)
    plot(X, Freq_samples)
    save_frequency_components(amplitude, phase_shift, frequencies)


def save_frequency_components(amplitude, phase_shift, frequencies):
    amplitude_rounded = [round(a, 13) for a in amplitude]
    phase_shift_rounded = [round(p, 14) for p in phase_shift]
    with open('frequency_components_rounded.txt', 'w') as file:
        for amp, phase, freq in zip(amplitude_rounded, phase_shift_rounded, frequencies):
            amp_str = f"{int(amp) if amp.is_integer() else amp}{'f' if not amp.is_integer() else ''}"
            phase_str = f"{int(phase) if phase.is_integer() else phase}{'f' if not phase.is_integer() else ''}"
            file.write(f"{amp_str} {phase_str}\n")


def compare():
    file1_amplitudes = []
    file1_phases = []

    with open('Task4/TestCases/DFT/Output_Signal_DFT_A,Phase.txt', 'r') as file:
        lines = file.readlines()[3:]
        for line in lines:
            data = line.strip().split()
            if len(data) >= 2:
                amplitude, phase = data
                amplitude = round(float(amplitude[:-1]) if amplitude.endswith('f') else float(amplitude), 14)
                phase = float(phase[:-1]) if phase.endswith('f') else float(phase)
                file1_amplitudes.append(amplitude)
                file1_phases.append(phase)

    file2_amplitudes = []
    file2_phases = []
    with open('Task4/OutputFiles/frequency_components_rounded.txt', 'r') as file:
        for line in file:
            data = line.strip().split()
            if len(data) >= 2:
                amplitude, phase = data
                amplitude = round(float(amplitude[:-1]) if amplitude.endswith('f') else float(amplitude), 14)
                phase = float(phase[:-1]) if phase.endswith('f') else float(phase)
                file2_amplitudes.append(amplitude)
                file2_phases.append(phase)

    amplitude_comparison = SignalComapreAmplitude(file1_amplitudes, file2_amplitudes)
    phase_comparison = SignalComaprePhaseShift(file1_phases, file2_phases)

    if amplitude_comparison and phase_comparison:
        print("Amplitude and Phase values match in the two files.")
    else:
        print("Amplitude and/or Phase values don't match in the two files.")


class Task4:
    def __init__(self):
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = '#ffffff'

        self.root = tk.Tk()
        self.root.geometry("1000x563")

        self.choose_file = StringVar(value="none")

        # setting background image
        self.setting_background()

        # Creating widgets
        self.create_widgets()

        # Placing widgets on the screen
        self.placing_widgets()

        self.root.mainloop()

    def setting_background(self):
        self.image = Image.open("../DSP_Tasks/Photos/sub_background.png")
        # self.image = Image.open("../Photos/sub_background.png")

        self.background2_image = ImageTk.PhotoImage(self.image)
        self.background2_label = Label(self.root, image=self.background2_image)
        self.main_frame2 = tk.Frame(self.root, borderwidth=0, background=self.mainColor)
        self.image_label = tk.Label(self.main_frame2, image="", borderwidth=0, background=self.mainColor)

    def create_widgets(self):
        # self.fill_inputs = Image.open("../DSP_Tasks/Photos/Task4/fill_inputs")
        self.fill_inputs = Image.open("../DSP_Tasks/Photos/Task4/fill_inputs.png")

        self.fill_inputs_image = ImageTk.PhotoImage(self.fill_inputs)
        self.fill_inputs_label = Label(self.root, image=self.fill_inputs_image, background=self.mainColor)

        self.choose_file_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task4/choose_file.png")
        self.choose_file_button = Button(self.root, image=self.choose_file_button_image, borderwidth=0, cursor="hand2",
                                         bd=0, background='#141345', activebackground='#141345',
                                         command=self.open_file_dialog)

        # Textbox sampling frequency
        self.sampling_frequency_label = Image.open("../DSP_Tasks/Photos/Task4/sampling_frequency_with_input.png")
        self.sampling_frequency_image = ImageTk.PhotoImage(self.sampling_frequency_label)
        self.sampling_frequency_label_value = Label(self.root, image=self.sampling_frequency_image,
                                                    background='#18103A')
        self.sampling_frequency_value = StringVar(value="")
        self.samplingFrequencyEntry = Entry(self.root, width=14, font=("arial", 17), bd=0,
                                            textvariable=self.sampling_frequency_value, background=self.secondColor,
                                            foreground=self.foregroundColor, insertbackground="#9601AB")

        self.fourier_transform_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task4/apply_fourier_transform.png")
        self.fourierTransformButton = Button(self.root, image=self.fourier_transform_button_image, borderwidth=0,
                                             cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                             command=lambda: generate_fourier_transform(self.choose_file,
                                                                                        self.sampling_frequency_value))

        self.modify_signal_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task4/modify_signal.png")
        self.modifySignalButton = Button(self.root, image=self.modify_signal_button_image, borderwidth=0,
                                         cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                         command=lambda: modify_signal(self.choose_file))

        self.compareButton = Button(self.root, text="Compare", borderwidth=0,
                                         cursor="hand2", bd=0, background='red', activebackground='#141345',
                                         command=lambda: compare())

    def placing_widgets(self):
        self.background2_label.place(x=0, y=0)
        self.main_frame2.place(anchor='center', relx=0.5, rely=0.45)
        self.fill_inputs_label.place(anchor='center', relx=0.5, y=130)
        self.choose_file_button.place(anchor='center', relx=0.5, y=190)
        self.sampling_frequency_label_value.place(anchor='center', relx=0.5, y=250)
        self.samplingFrequencyEntry.place(anchor='center', relx=0.693, y=250)
        self.fourierTransformButton.place(anchor='center', relx=0.5, y=310)
        self.modifySignalButton.place(anchor='center', relx=0.5, y=370)
        self.compareButton.pack()
        self.image_label.pack()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.choose_file.set(file_path)

# Task4()
