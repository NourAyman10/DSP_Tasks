import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from Task6.helper_functions import load_file
from Task6.helper_functions import plot_signals
from Task6.helper_functions import delay_signal
from Task6.helper_functions import advance_signal
from Task6.smoothing import Smoothing
from Task6.advancing import Advancing
from Task6.delaying import Delaying
from Task6.folding import Folding


def fold_signal(file_path):
    signal = load_file(file_path.get())
    Folding(signal)


def remove_DC_frequency(file_path):
    signal = load_file(file_path.get())
    N = len(signal)
    dft_signal = np.zeros(N, dtype=np.complex128)
    for k in range(N):
        for n in range(N):
            phase_shift = 2 * np.pi * k * n
            dft_signal[k] += signal[n] * np.exp(-1j * phase_shift / N)

    # Set DC component to zero
    dft_signal[0] = 0

    # Compute the IDFT manually
    dc_removed_signal = np.zeros(N, dtype=np.float_)
    for n in range(N):
        for k in range(N):
            phase_shift = 2 * np.pi * k * n
            dc_removed_signal[n] += dft_signal[k] * np.exp(1j * phase_shift / N)

    dc_removed_signal = dc_removed_signal.real / N

    plot_signals("Original Signal VS DC Removed Signal", Original_Signal=signal, DC_Removed_Signal=dc_removed_signal)


def smoothing_signal(file_path):
    signal = load_file(file_path.get())
    Smoothing(signal)


def advancing_signal(file_path):
    signal = load_file(file_path.get())
    Advancing(signal)


def delaying_signal(file_path):
    signal = load_file(file_path.get())
    Delaying(signal)


def sharpening_signal(file_path):
    InputSignal = load_file(file_path.get())

    FirstDrev = [int(InputSignal[i] - InputSignal[i - 1] if i > 0 else 1) for i in range(len(InputSignal))]

    SecondDrev = [
        int(InputSignal[i + 1] - 2 * InputSignal[i] + InputSignal[i - 1] if i > 1 and i < len(InputSignal) - 1 else 0)
        for i in range(len(InputSignal))]
    # Y(n)= x(n+1)-2x(n)+x(n-1)

    FirstDrev = FirstDrev[:-1]
    SecondDrev = SecondDrev[:-2]

    plot_signals("Original Signal VS First Derivative VS Second Derivative", Original_Signal=InputSignal,
                 First_Derivative=FirstDrev, Second_Derivative=SecondDrev)


class Task6:
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
        self.choose_file_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task6/choose_file.png")
        self.choose_file_button = Button(self.root, image=self.choose_file_button_image, borderwidth=0, cursor="hand2",
                                         bd=0, background='#141345', activebackground='#141345',
                                         command=self.open_file_dialog)

        self.smoothing_signal_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task6/smooth_signal.png")
        self.smoothing_signal_button = Button(self.root, image=self.smoothing_signal_button_image, borderwidth=0,
                                              cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                              command=lambda: smoothing_signal(self.choose_file))

        self.sharpening_signal_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task6/sharpen_signal.png")
        self.sharpening_signal_button = Button(self.root, image=self.sharpening_signal_button_image, borderwidth=0,
                                               cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                               command=lambda: sharpening_signal(self.choose_file))

        self.advancing_signal_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task6/advancing_signal.png")
        self.advancing_signal_button = Button(self.root, image=self.advancing_signal_button_image, borderwidth=0,
                                              cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                              command=lambda: advancing_signal(self.choose_file))

        self.delaying_signal_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task6/delaying_signal.png")
        self.delaying_signal_button = Button(self.root, image=self.delaying_signal_button_image, borderwidth=0,
                                             cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                             command=lambda: delaying_signal(self.choose_file))

        self.folding_signal_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task6/folding_signal.png")
        self.folding_signal_button = Button(self.root, image=self.folding_signal_button_image, borderwidth=0,
                                            cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                            command=lambda: fold_signal(self.choose_file))

        self.remove_dc_component_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task6/remove_dc_component.png")
        self.remove_dc_component_button = Button(self.root, image=self.remove_dc_component_button_image, borderwidth=0,
                                                 cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                                 command=lambda: remove_DC_frequency(self.choose_file))

    def placing_widgets(self):
        self.background2_label.place(x=0, y=0)
        self.main_frame2.place(anchor='center', relx=0.5, rely=0.45)
        self.choose_file_button.place(anchor='center', relx=0.5, y=160)
        self.smoothing_signal_button.place(anchor='center', relx=0.378, y=240)
        self.sharpening_signal_button.place(anchor='center', relx=0.624, y=240)
        self.advancing_signal_button.place(anchor='center', relx=0.378, y=290)
        self.delaying_signal_button.place(anchor='center', relx=0.624, y=290)
        self.folding_signal_button.place(anchor='center', relx=0.5, y=340)
        self.remove_dc_component_button.place(anchor='center', relx=0.5, y=390)
        self.image_label.pack()

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.choose_file.set(file_path)
