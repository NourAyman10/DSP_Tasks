from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Task2.helper_functions import load_file
from Task2.helper_functions import plot_signal
from Task2.helper_functions import padding


def addition(signal1_file_path, signal2_file_path):
    signal1 = load_file(signal1_file_path.get())
    signal2 = load_file(signal2_file_path.get())

    signal1, signal2 = padding(signal1, signal2)
    result_addition = signal1 + signal2
    plot_signal(result_addition, "Addition Result")


class Addition:
    def __init__(self, root):
        self.mainColor = '#1C113A'
        width, height = 1000, 563

        self.signal1_selected_file = tk.StringVar(value="none")
        self.signal2_selected_file = tk.StringVar(value="none")

        canvas = tk.Canvas(root, width=width, height=height)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("../DSP_Tasks/Photos/sub_background.png"))
        canvas.background = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # create widgets
        choose_signals = Image.open("../DSP_Tasks//Photos/Task2/choose_signals_add.png")
        self.choose_signals_image = ImageTk.PhotoImage(choose_signals)
        choose_signals_label = Label(root, image=self.choose_signals_image, background="#250F31")

        self.file1_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/chooseFileBtn.png")
        file1_button = Button(root, image=self.file1_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=self.open_file1_dialog)

        self.file2_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/chooseFileBtn.png")
        file2_button = Button(root, image=self.file2_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=self.open_file2_dialog)

        self.get_result_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/get_result.png")
        get_result_button = Button(root, image=self.get_result_button_image, borderwidth=0, cursor="hand2", bd=0,
                                   background='#141345', activebackground='#141345',
                                   command=lambda: addition(self.signal1_selected_file, self.signal2_selected_file))

        # Put a tkinter widget on the canvas.
        canvas.create_window(150, 120, anchor=tk.NW, window=choose_signals_label)
        canvas.create_window(390, 170, anchor=tk.NW, window=file1_button)
        canvas.create_window(390, 230, anchor=tk.NW, window=file2_button)
        canvas.create_window(390, 330, anchor=tk.NW, window=get_result_button)

    def open_file1_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.signal1_selected_file.set(file_path)

    def open_file2_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.signal2_selected_file.set(file_path)
