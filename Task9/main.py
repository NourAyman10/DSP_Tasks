import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from Task9.Fast_Convolution import FastConvolution
from Task9.Fast_Correlation import fast_correlation


class Task9:
    def __init__(self):
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = '#ffffff'

        self.root = tk.Tk()
        self.root.geometry("1000x563")

        self.choose_file1 = StringVar(value="none")
        self.choose_file2 = StringVar(value="none")

        # setting background image
        self.setting_background()

        # Creating widgets
        self.create_widgets()

        # Placing widgets on the screen
        self.placing_widgets()

        self.root.mainloop()

    def setting_background(self):
        self.image = Image.open("../DSP_Tasks/Photos/sub_background.png")

        self.background2_image = ImageTk.PhotoImage(self.image)
        self.background2_label = Label(self.root, image=self.background2_image)
        self.main_frame2 = tk.Frame(self.root, borderwidth=0, background=self.mainColor)
        self.image_label = tk.Label(self.main_frame2, image="", borderwidth=0, background=self.mainColor)

    def create_widgets(self):
        self.choose_file1_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task7/first_file.png")
        self.choose_file1_button = Button(self.root, image=self.choose_file1_button_image, borderwidth=0, cursor="hand2",
                                          bd=0, background='#141345', activebackground='#141345',
                                          command=self.open_file1_dialog)

        self.choose_file2_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task7/second_file.png")
        self.choose_file2_button = Button(self.root, image=self.choose_file2_button_image, borderwidth=0, cursor="hand2",
                                          bd=0, background='#141345', activebackground='#141345',
                                          command=self.open_file2_dialog)


        self.fast_convolution_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task9/fast_conv.png")
        self.fast_convolution_button = Button(self.root, image=self.fast_convolution_button_image, borderwidth=0,
                                              cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                              command=lambda: FastConvolution(self.choose_file1.get(), self.choose_file2.get()))

        self.fast_correlation_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task9/fast_corr.png")
        self.fast_correlation_button = Button(self.root, image=self.fast_correlation_button_image, borderwidth=0,
                                              cursor="hand2", bd=0, background='#141345', activebackground='#141345',
                                              command=lambda: fast_correlation(self.choose_file1.get(), self.choose_file2.get()))

    def placing_widgets(self):
        self.background2_label.place(x=0, y=0)
        self.main_frame2.place(anchor='center', relx=0.5, rely=0.45)
        self.choose_file1_button.place(anchor='center', relx=0.5, y=180)
        self.choose_file2_button.place(anchor='center', relx=0.5, y=240)

        self.fast_convolution_button.place(anchor='center', relx=0.5, y=340)
        self.fast_correlation_button.place(anchor='center', relx=0.5, y=400)
        self.image_label.pack()

    def open_file1_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/Task9", title="Select a File")
        if file_path:
            self.choose_file1.set(file_path)

    def open_file2_dialog(self):
        file_path = filedialog.askopenfilename(initialdir="/Task9", title="Select a File")
        if file_path:
            self.choose_file2.set(file_path)
