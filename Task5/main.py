import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from Task5.comparesignal2 import SignalSamplesAreEqual


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
    with open("Task5/selected_coefficients.txt", "w") as file:
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


def run(file, coefficients_num_m):
    signal = load_file(file.get())
    plot_signal_frequency_domain(signal)
    m = int(coefficients_num_m.get())
    print("m = ", m)
    dct_result = compute_DCT(signal)
    print("Signal With DC\n", dct_result)
    save_coefficients_to_file(dct_result, m)
    messagebox.showinfo(title="Successfully saved",
                        message=f"Saved first {m} coefficients to 'selected_coefficients.txt'")
    signal_Dc = load_file('Task5/Remove DC component/DC_component_input.txt')
    signal_without_dc = remove_DC(signal_Dc)
    print("Signal Without DC\n", signal_without_dc)
    plot_signal_without_dc(signal_Dc, signal_without_dc)


def compare_signals(file):
    signal = load_file(file.get())
    dct_result = compute_DCT(signal)

    signal_Dc = load_file('Task5/Remove DC component/DC_component_input.txt')
    signal_without_dc = remove_DC(signal_Dc)

    DCT_OUTPUT = 'Task5/DCT/DCT_output.txt'
    DCT = SignalSamplesAreEqual(DCT_OUTPUT, dct_result)

    DC_OUTPUT = 'Task5/Remove DC component/DC_component_output.txt'
    DC_REMOVE = SignalSamplesAreEqual(DC_OUTPUT, signal_without_dc)

    if(DCT):
        messagebox.showinfo(title="DCT Compare Results", message="DCT Test case passed successfully")
    else:
        messagebox.showerror(title="DCT Compare Results", message="DCT Test case failed")

    if(DC_REMOVE):
        messagebox.showinfo(title="Remove DC component Compare Results",
                            message="Remove DC component Test case passed successfully")
    else:
        messagebox.showerror(title="Remove DC component Compare Results", message="DCT Test case failed")

class Task5:
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
        self.fill_inputs = Image.open("../DSP_Tasks/Photos/Task4/fill_inputs.png")

        self.fill_inputs_image = ImageTk.PhotoImage(self.fill_inputs)
        self.fill_inputs_label = Label(self.root, image=self.fill_inputs_image, background=self.mainColor)

        self.choose_file_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task4/choose_file.png")
        self.choose_file_button = Button(self.root, image=self.choose_file_button_image, borderwidth=0, cursor="hand2",
                                         bd=0, background='#141345', activebackground='#141345',
                                         command=self.open_file_dialog)

        # Textbox sampling frequency
        self.coefficients_num_m_label = Image.open("../DSP_Tasks/Photos/Task5/coefficientsNum.png")
        self.coefficients_num_m_image = ImageTk.PhotoImage(self.coefficients_num_m_label)
        self.coefficients_num_m_label_value = Label(self.root, image=self.coefficients_num_m_image,
                                                    background='#18103A')
        self.coefficients_num_m_value = StringVar(value="")
        self.coefficients_num_m_entry = Entry(self.root, width=11, font=("arial", 17), bd=0,
                                              textvariable=self.coefficients_num_m_value, background=self.secondColor,
                                              foreground=self.foregroundColor, insertbackground="#9601AB")

        self.Compute_DCT_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task5/Compute_DCT.png")
        self.Compute_DCT_button = Button(self.root, image=self.Compute_DCT_button_image, borderwidth=0,
                                         cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                         command=lambda: run(self.choose_file, self.coefficients_num_m_value))

        self.compare_results_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task5/compare_results.png")
        self.compare_results_button = Button(self.root, image=self.compare_results_button_image, borderwidth=0,
                                             cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                             command=lambda: compare_signals(self.choose_file))


    def placing_widgets(self):
        self.background2_label.place(x=0, y=0)
        self.main_frame2.place(anchor='center', relx=0.5, rely=0.45)
        self.fill_inputs_label.place(anchor='center', relx=0.5, y=130)
        self.choose_file_button.place(anchor='center', relx=0.5, y=190)
        self.coefficients_num_m_label_value.place(anchor='center', relx=0.5, y=250)
        self.coefficients_num_m_entry.place(anchor='center', relx=0.717, y=250)
        self.Compute_DCT_button.place(anchor='center', relx=0.5, y=310)
        self.compare_results_button.place(anchor='center', relx=0.5, y=370)
        self.image_label.pack()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.choose_file.set(file_path)

# Task5()
