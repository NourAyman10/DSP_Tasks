from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

from comparesignals import SignalSamplesAreEqual
from tkinter import messagebox


class SecondPoint:
    def __init__(self):
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = '#ffffff'
        self.time = []
        self.Y = []

        self.root = tk.Tk()
        self.root.geometry("1000x563")

        # setting background image
        self.setting_background()

        # Creating widgets
        self.create_widgets()

        # Placing widgets on the screen
        self.placing_widgets()

        self.root.mainloop()

    def setting_background(self):
        self.image = Image.open("../Photos/sub_background.png")
        self.background2_image = ImageTk.PhotoImage(self.image)
        self.background2_label = Label(self.root, image=self.background2_image)
        self.main_frame2 = tk.Frame(self.root, borderwidth=0, background=self.mainColor)
        self.image_label = tk.Label(self.main_frame2, image="", borderwidth=0, background=self.mainColor)

    def create_widgets(self):

        self.choose_type = Image.open("../Photos/Task1/chooseType.png")
        self.choose_type_image = ImageTk.PhotoImage(self.choose_type)
        self.choose_type_label = Label(self.root, image=self.choose_type_image, background=self.mainColor)
        # Type(sin, cos) Radio Button
        self.type_value = StringVar(value="none")
        self.SinImage = PhotoImage(file="../Photos/Task1/Point2/sinusoidal.png")
        self.SinRadioButton = Radiobutton(self.root, variable=self.type_value,
                                          value="sin", background=self.mainColor, image=self.SinImage,
                                          activebackground=self.mainColor)
        self.CosImage = PhotoImage(file="../Photos/Task1/Point2/cosinusoidal.png")
        self.CosRadioButton = Radiobutton(self.root, variable=self.type_value,
                                          value="cos", background=self.mainColor, image=self.CosImage,
                                          activebackground=self.mainColor)
        # Textbox inputs labels
        self.inputs_labels = Image.open("../Photos/Task1/Point2/inputs.png")
        self.inputs_labels_image = ImageTk.PhotoImage(self.inputs_labels)
        self.inputs_labels_label = Label(self.root, image=self.inputs_labels_image, background='#18103A')
        self.amplitude_value = StringVar(value="")
        self.amplitudeEntry = Entry(self.root, width=18, font=("arial", 15), bd=0, textvariable=self.amplitude_value,
                                    background=self.secondColor,
                                    foreground=self.foregroundColor, insertbackground="#9601AB")
        self.analogFrequency_value = StringVar(value="")
        self.analogFrequencyEntry = Entry(self.root, width=18, font=("arial", 15), bd=0,
                                          textvariable=self.analogFrequency_value,
                                          background=self.secondColor,
                                          foreground=self.foregroundColor, insertbackground="#9601AB")
        self.samplingFrequency_value = StringVar(value="")
        self.samplingFrequencyEntry = Entry(self.root, width=18, font=("arial", 15), bd=0,
                                            textvariable=self.samplingFrequency_value,
                                            background=self.secondColor,
                                            foreground=self.foregroundColor, insertbackground="#9601AB")
        self.phaseShift_value = StringVar(value="")
        self.phaseShiftEntry = Entry(self.root, width=18, font=("arial", 15), bd=0, textvariable=self.phaseShift_value,
                                     background=self.secondColor,
                                     foreground=self.foregroundColor, insertbackground="#9601AB")
        self.generate_button_image = PhotoImage(file="../Photos/Task1/Point2/generateBtn.png")
        self.generateButton = Button(self.root, image=self.generate_button_image, borderwidth=0, cursor="hand2", bd=0,
                                     background='#141345', activebackground='#141345', command=self.generate_wave)
        self.compare_button_image = PhotoImage(file="../Photos/Task1/Point2/compareBtn.png")
        self.compareButton = Button(self.root, image=self.compare_button_image, borderwidth=0, cursor="hand2", bd=0,
                                    background='#141345', activebackground='#141345', command=self.compare_values)

    def placing_widgets(self):
        self.background2_label.place(x=0, y=0)
        self.main_frame2.place(anchor='center', relx=0.5, rely=0.45)
        self.choose_type_label.place(anchor='center', relx=0.5, y=130)
        self.SinRadioButton.place(anchor='center', relx=0.3, y=180)
        self.CosRadioButton.place(anchor='center', relx=0.68, y=180)
        self.inputs_labels_label.place(anchor='center', relx=0.5, y=300)
        self.amplitudeEntry.place(anchor='center', relx=0.73, y=240)
        self.analogFrequencyEntry.place(anchor='center', relx=0.73, y=280)
        self.samplingFrequencyEntry.place(anchor='center', relx=0.73, y=320)
        self.phaseShiftEntry.place(anchor='center', relx=0.73, y=360)
        self.generateButton.place(anchor='center', relx=0.35, y=430)
        self.compareButton.place(anchor='center', relx=0.65, y=430)
        self.image_label.pack()

    def generate_wave(self):
        # validate inputs
        validate = bool(self.validate_inputs())

        if validate:
            amplitude = float(self.amplitude_value.get())
            analog_frequency = float(self.analogFrequency_value.get())
            sampling_frequency = float(self.samplingFrequency_value.get())
            phase_shift = float(self.phaseShift_value.get())

            if analog_frequency == 0:
                self.Y = amplitude * np.cos(phase_shift)

            # sampling frequency obeys the sampling theorem
            min_sampling_frequency = 2 * analog_frequency
            if sampling_frequency < min_sampling_frequency or sampling_frequency == 0:
                messagebox.showerror("Error!!", f"Sampling frequency should be at least {min_sampling_frequency} Hz.")

            else:
                self.time = np.arange(0, 1, 1 / sampling_frequency)
                if self.type_value.get() == "sin":
                    self.Y = amplitude * np.sin((2 * np.pi * analog_frequency * self.time) + phase_shift)
                elif self.type_value.get() == "cos":
                    self.Y = amplitude * np.cos((2 * np.pi * analog_frequency * self.time) + phase_shift)
                else:
                    messagebox.showerror("Error!!", "Please, Enter valid type")

                self.draw_wave()

    def draw_wave(self):
        plt.figure(figsize=(20, 5))
        plt.plot(self.time, self.Y)
        plt.title(f"{(self.type_value.get()).capitalize()} Wave")
        plt.xlabel("Time(s)")
        plt.ylabel("Amplitude")
        plt.show()

    def validate_inputs(self):
        if self.type_value.get().strip() and str(self.amplitude_value.get()).strip() and str(
                self.analogFrequency_value.get()).strip() and str(self.samplingFrequency_value.get()).strip() and str(
                self.phaseShift_value.get()).strip():
            return True
        else:
            messagebox.showerror("Error!!", "Please, Fill all empty inputs")
            return False

    def compare_values(self):
        # validate inputs
        validate = bool(self.validate_inputs())

        if validate:
            if self.type_value.get() == "sin":
                SignalSamplesAreEqual("Files/SinOutput.txt", self.time, self.Y)
            elif self.type_value.get() == "cos":
                SignalSamplesAreEqual("Files/CosOutput.txt", self.time, self.Y)
            else:
                messagebox.showerror("Compare Values", "You Should Choose Signal Type")
