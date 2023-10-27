from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np


def load_file(file_path):
    with open(file_path, "r") as file:
        for _ in range(3):
            next(file)
        indices = []
        values = []
        for line in file:
            n, value = line.split()
            indices.append(int(n))
            values.append(float(value))

    indices = np.array(indices)
    values = np.array(values)
    return indices, values


def plot_signal(signal, indices, title):
    plt.figure()
    plt.plot(indices, signal)
    plt.title(title)
    plt.xlabel("Sample")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()


def shifting(signal_path, constant):
    indices, signal = load_file(signal_path.get())
    print("before", signal)
    result = indices - float(constant.get())
    print("After", result)
    plot_signal(signal, indices, "After shifting")
    print("indices", indices)


class Shifting:
    def __init__(self, root):
        self.mainColor = '#1C113A'
        self.secondColor = '#18103A'
        self.foregroundColor = '#ffffff'

        width, height = 1000, 563
        self.signal_selected_file = tk.StringVar(value="none")
        self.constant = tk.StringVar(value="")

        canvas = tk.Canvas(root, width=width, height=height)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("../DSP_Tasks/Photos/sub_background.png"))
        canvas.background = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # create widget
        choose_signals = Image.open("../DSP_Tasks//Photos/Task2/choose_shifting.png")
        self.choose_signals_image = ImageTk.PhotoImage(choose_signals)
        choose_signals_label = Label(root, image=self.choose_signals_image, background="#250F31")

        constant_image_path = Image.open("../DSP_Tasks//Photos/Task2/input.png")
        self.constant_image = ImageTk.PhotoImage(constant_image_path)
        constant_image_label = Label(root, image=self.constant_image, background="#250F31")
        constant_entry = Entry(root, width=18, font=("arial", 15), bd=0,
                               textvariable=self.constant,
                               background=self.secondColor,
                               foreground=self.foregroundColor, insertbackground="#9601AB")

        self.file_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/chooseFileBtn.png")
        file_button = Button(root, image=self.file_button_image, borderwidth=0, cursor="hand2", bd=0,
                             background='#141345', activebackground='#141345', command=self.open_file_dialog)

        self.get_result_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/get_result.png")
        get_result_button = Button(root, image=self.get_result_button_image, borderwidth=0, cursor="hand2", bd=0,
                                   background='#141345', activebackground='#141345',
                                   command=lambda: shifting(self.signal_selected_file, self.constant))

        # Put a tkinter widget on the canvas.
        canvas.create_window(150, 120, anchor=tk.NW, window=choose_signals_label)
        canvas.create_window(390, 160, anchor=tk.NW, window=constant_image_label)
        canvas.create_window(410, 165, anchor=tk.NW, window=constant_entry)
        canvas.create_window(390, 230, anchor=tk.NW, window=file_button)
        canvas.create_window(390, 330, anchor=tk.NW, window=get_result_button)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.signal_selected_file.set(file_path)
