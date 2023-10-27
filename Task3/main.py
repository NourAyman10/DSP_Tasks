import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from Task3.files_comparison import Compare
from Task3.helper_functions import load_file



def get_levels(number, typ):
    if typ == "level":
        return number
    else:
        return 2 ** int(number)


def quantization(file_path, number, typ):
    signal = load_file(file_path.get())
    levels = get_levels(number, typ)
    get_interval_idx(signal, levels)


def binary_search(target, array):
    sorted_array = sorted(array)

    left = 1
    right = len(sorted_array) - 1

    while left <= right:
        mid = np.round((left + right) // 2)

        if sorted_array[mid] == target:
            return mid
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return right + 1


def generate_range(signal, levels):
    min_amp = np.min(signal)
    max_amp = np.max(signal)
    delta = (max_amp - min_amp) / int(levels)
    ranges = [min_amp + i * delta for i in range(int(levels) + 1)]
    return np.round(ranges, 2)


def get_interval_idx(signal, levels):
    ranges = generate_range(signal, levels)
    interval_indices = []
    for i in signal:
        x = binary_search(i, ranges)
        interval_indices.append(x)
    quantized_signal(signal, levels, interval_indices)


def calculate_midpoints(indices):
    midpoints = []
    for i in range(len(indices) - 1):
        start_index = indices[i]
        end_index = indices[i + 1]
        midpoint = (start_index + end_index) / 2.0
        midpoints.append(midpoint)
    return (np.round(midpoints, 3)).tolist()


def quantized_signal(signal, levels, indices):
    ranges = generate_range(signal, levels)
    midpoints = calculate_midpoints(ranges)

    xq = []
    for i in indices:
        xq.append(midpoints[i - 1])

    quantized_error(signal, xq)


def quantized_error(signal, xq):
    quantization_error_values = xq - signal
    plot(signal, xq, quantization_error_values)
    return quantization_error_values


def average_power_error(signal, xq):
    quantized_err = quantized_error(signal, xq)
    error = [sample ** 2 for sample in quantized_err]
    average_power = sum(error) / len(error)
    messagebox.showerror("Average Power Error", f"Your Average Power Error is {average_power}.")


def encoded_signal(signal, levels):
    x = get_interval_idx(signal, levels)
    num_bits = len(bin(levels - 1)) - 2  # Calculate the number of bits required
    formatted_output = [format(i - 1, f'0{num_bits}b') for i in x]
    return formatted_output

def plot(signal, quantized_signal_values, quantization_error_values):
    # Plot the original signal, quantized signal, and quantization error
    plt.figure(figsize=(10, 8))
    plt.subplot(3, 1, 1)
    plt.plot(signal, 'b', label='Original Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(quantized_signal_values, 'r', label='Quantized Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(quantization_error_values, 'g', label='Quantization Error')
    plt.xlabel('Time')
    plt.ylabel('Error')
    plt.legend()

    plt.tight_layout()
    plt.show()



class Task3:
    def __init__(self):
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = '#ffffff'

        self.root = tk.Tk()
        self.root.geometry("1000x563")

        # setting background image
        self.setting_background()

        # Creating widgets
        self.create_widgets()

        # Placing widgets on the screen
        self.placing_widgets()

        self.root.mainloop()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.select_file.set(file_path)

    def setting_background(self):
        self.image = Image.open("../DSP_Tasks/Photos/sub_background.png")
        self.background2_image = ImageTk.PhotoImage(self.image)
        self.background2_label = Label(self.root, image=self.background2_image)
        self.main_frame2 = tk.Frame(self.root, borderwidth=0, background=self.mainColor)
        self.image_label = tk.Label(self.main_frame2, image="", borderwidth=0, background=self.mainColor)

    def create_widgets(self):
        self.choose_type = Image.open("../DSP_Tasks/Photos/Task3/chooseType.png")
        self.choose_type_image = ImageTk.PhotoImage(self.choose_type)
        self.choose_type_label = Label(self.root, image=self.choose_type_image, background=self.mainColor)

        # Type(Bits, Levels) Radio Button
        self.type_value = StringVar(value="none")
        self.bitsImage = PhotoImage(file="../DSP_Tasks/Photos/Task3/bits.png")
        self.bitsRadioButton = Radiobutton(self.root, variable=self.type_value,
                                           value="bits", background=self.mainColor, image=self.bitsImage,
                                           activebackground=self.mainColor)
        self.levelsImage = PhotoImage(file="../DSP_Tasks/Photos/Task3/levels.png")
        self.levelsRadioButton = Radiobutton(self.root, variable=self.type_value,
                                             value="level", background=self.mainColor, image=self.levelsImage,
                                             activebackground=self.mainColor)
        # Textbox inputs labels
        self.number_label = Image.open("../DSP_Tasks/Photos/Task3/input.png")
        self.number_label_image = ImageTk.PhotoImage(self.number_label)
        self.number_label_value = Label(self.root, image=self.number_label_image, background='#18103A')
        self.number_value = StringVar(value="")
        self.numberEntry = Entry(self.root, width=18, font=("arial", 28), bd=0, textvariable=self.number_value,
                                 background=self.secondColor,
                                 foreground=self.foregroundColor, insertbackground="#9601AB")

        self.select_file = StringVar(value="none")
        self.file_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task3/chooseFileBtn.png")
        self.file_button = Button(self.root, image=self.file_button_image, borderwidth=0, cursor="hand2", bd=0,
                                  background='#141345', activebackground='#141345', command=self.open_file_dialog)

        self.generate_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task3/generateBtn.png")
        self.generateButton = Button(self.root, image=self.generate_button_image, borderwidth=0, cursor="hand2", bd=0,
                                     background='#141345', activebackground='#141345',
                                     command=lambda: quantization(self.select_file, self.number_value.get(),
                                                                  self.type_value.get()))
        self.compare_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task3/compareBtn.png")
        self.compareButton = Button(self.root, image=self.compare_button_image, borderwidth=0, cursor="hand2", bd=0,
                                    background='#141345', activebackground='#141345', command=Compare)

    def placing_widgets(self):
        self.background2_label.place(x=0, y=0)
        self.main_frame2.place(anchor='center', relx=0.5, rely=0.45)
        self.choose_type_label.place(anchor='center', relx=0.5, y=130)
        self.bitsRadioButton.place(anchor='center', relx=0.25, y=180)
        self.levelsRadioButton.place(anchor='center', relx=0.73, y=180)
        self.number_label_value.place(anchor='center', relx=0.5, y=240)
        self.numberEntry.place(anchor='center', relx=0.5, y=240)
        self.file_button.place(anchor='center', relx=0.5, y=340)
        self.generateButton.place(anchor='center', relx=0.35, y=430)
        self.compareButton.place(anchor='center', relx=0.65, y=430)
        self.image_label.pack()

# Task3()
