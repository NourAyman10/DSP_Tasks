from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
from Task2.helper_functions import load_file
from Task2.helper_functions import plot_signal


def multiplication(file_path, constant):
    signal = load_file(file_path.get())
    plot_signal(signal, "Before Multiplication:")
    print("Before:", signal)
    result_multiplication = signal * float(constant.get())
    print("After:", result_multiplication)
    plot_signal(result_multiplication, f"Multiplication Result (Constant = {constant.get()})")


class Multiplication:
    def __init__(self, root):
        self.mainColor = '#1C113A'
        self.secondColor = '#18103A'
        self.foregroundColor = '#ffffff'
        width, height = 1000, 563

        self.constant = tk.StringVar(value="")
        self.selected_file = tk.StringVar(value="none")

        canvas = tk.Canvas(root, width=width, height=height)
        canvas.pack()

        img = ImageTk.PhotoImage(Image.open("../DSP_Tasks/Photos/sub_background.png"))
        canvas.background = img
        canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # create widgets
        choose_signal = Image.open("../DSP_Tasks//Photos/Task2/choose_signals_multiply.png")
        self.choose_signal_image = ImageTk.PhotoImage(choose_signal)
        choose_signal_label = Label(root, image=self.choose_signal_image, background="#250F31")

        constant_image_path = Image.open("../DSP_Tasks//Photos/Task2/input.png")
        self.constant_image = ImageTk.PhotoImage(constant_image_path)
        constant_image_label = Label(root, image=self.constant_image, background="#250F31")
        constant_entry = Entry(root, width=18, font=("arial", 15), bd=0,
                               textvariable=self.constant,
                               background=self.secondColor,
                               foreground=self.foregroundColor, insertbackground="#9601AB")

        self.choose_file_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/chooseFileBtn.png")
        choose_file_button = Button(root, image=self.choose_file_button_image, borderwidth=0, cursor="hand2", bd=0,
                                    background='#141345', activebackground='#141345', command=self.open_file_dialog)

        self.get_result_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/get_result.png")
        get_result_button = Button(root, image=self.get_result_button_image, borderwidth=0, cursor="hand2", bd=0,
                                   background='#141345', activebackground='#141345',
                                   command=lambda: multiplication(self.selected_file, self.constant))

        # Put a tkinter widget on the canvas.

        canvas.create_window(150, 120, anchor=tk.NW, window=choose_signal_label)
        canvas.create_window(390, 160, anchor=tk.NW, window=constant_image_label)
        canvas.create_window(410, 165, anchor=tk.NW, window=constant_entry)
        canvas.create_window(390, 230, anchor=tk.NW, window=choose_file_button)
        canvas.create_window(390, 330, anchor=tk.NW, window=get_result_button)

    def open_file_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select a File")
        if file_path:
            self.selected_file.set(file_path)
