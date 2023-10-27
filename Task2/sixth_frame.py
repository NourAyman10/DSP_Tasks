from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
from tkinter import messagebox
from tkinter import filedialog
from Task2.helper_functions import load_file
from Task2.helper_functions import plot_signal


def normalization(file_path, normalization_range):
    signal = load_file(file_path.get())

    plot_signal(signal, "Before normalization")
    if normalization_range.get() == "0 to 1":
        result = (signal - np.min(signal)) / (np.max(signal) - np.min(signal))
        plot_signal(result, "After normalization")

    elif normalization_range.get() == "-1 to 1":
        result = (2 * (signal - np.min(signal)) / (np.max(signal) - np.min(signal))) - 1
        plot_signal(result, "After normalization")
    else:
        messagebox.showerror("Error!!", "Invalid range option. Please choose either '0 to 1' or ' -1 to 1'.")


class Normalization:
    def __init__(self, root):
        self.mainColor = '#1C113A'
        width, height = 1000, 563

        range_number = StringVar(value="none")
        self.selected_file = tk.StringVar(value="none")

        canvas = tk.Canvas(root, width=width, height=height)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("../DSP_Tasks/Photos/sub_background.png"))
        canvas.background = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # create widgets
        choose_range = Image.open("../DSP_Tasks//Photos/Task2/choose_range.png")
        self.choose_range_image = ImageTk.PhotoImage(choose_range)
        choose_range_label = Label(root, image=self.choose_range_image, background="#250F31")

        # choose range Radio Button
        self.from0to1Image = PhotoImage(file="../DSP_Tasks/Photos/Task2/from 0 to 1.png")
        from0to1Button = Radiobutton(root, variable=range_number,
                                     value="0 to 1", background=self.mainColor, image=self.from0to1Image,
                                     activebackground=self.mainColor)

        self.from_1to1Image = PhotoImage(file="../DSP_Tasks/Photos/Task2/from -1 to 1.png")
        from_1to1Button = Radiobutton(root, variable=range_number,
                                      value="-1 to 1", background=self.mainColor, image=self.from_1to1Image,
                                      activebackground=self.mainColor)

        self.choose_file_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/chooseFileBtn.png")
        choose_file_button = Button(root, image=self.choose_file_button_image, borderwidth=0, cursor="hand2", bd=0,
                                    background='#141345', activebackground='#141345', command=self.open_file_dialog)

        self.get_result_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/get_result.png")
        get_result_button = Button(root, image=self.get_result_button_image, borderwidth=0, cursor="hand2", bd=0,
                                   background='#141345', activebackground='#141345',
                                   command=lambda: normalization(self.selected_file, range_number))

        # Put a tkinter widget on the canvas.
        canvas.create_window(150, 120, anchor=tk.NW, window=choose_range_label)
        canvas.create_window(150, 180, anchor=tk.NW, window=from0to1Button)
        canvas.create_window(550, 180, anchor=tk.NW, window=from_1to1Button)
        canvas.create_window(390, 230, anchor=tk.NW, window=choose_file_button)
        canvas.create_window(390, 330, anchor=tk.NW, window=get_result_button)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.selected_file.set(file_path)
