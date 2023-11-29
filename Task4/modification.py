import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox


class Modification:
    def __init__(self, X):
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = "#9601AB"
        self.signal = X

        self.root = tk.Tk()
        self.root.title("Modify Signal")
        self.root.geometry("491x276")
        self.root.configure(bg=self.mainColor)

        amplitude_label = tk.Label(self.root, text="Amplitude", borderwidth=0, background=self.mainColor,
                                   foreground="#FCD24F", font=("Arial", 18))

        self.amplitude_value = StringVar(self.root, value="")
        amplitude_entry = Entry(self.root, width=18, font=("arial", 18), bd=1, textvariable=self.amplitude_value,
                                background=self.mainColor, foreground=self.foregroundColor,
                                insertbackground="#9601AB")

        phase_shift_label = tk.Label(self.root, text="Phase Shift", borderwidth=0, background=self.mainColor, foreground="#FCD24F",
                                     font=("Arial", 18))

        self.phase_shift_value = StringVar(self.root, value="")
        phase_shift_entry = Entry(self.root, width=18, font=("arial", 18), bd=1, textvariable=self.phase_shift_value,
                                  background=self.mainColor, foreground=self.foregroundColor,
                                  insertbackground="#9601AB")

        generate_btn = tk.Button(self.root, text="Generate", borderwidth=0,
                                 cursor="hand2", bd=0, background=self.foregroundColor, font=("arial", 18),
                                 activebackground=self.foregroundColor, foreground="white",
                                 command=lambda: self.modify_amplitude_and_phase(self.signal, self.amplitude_value,
                                                                                 self.phase_shift_value))

        amplitude_label.pack()
        amplitude_entry.pack()
        phase_shift_label.pack()
        phase_shift_entry.pack()
        generate_btn.pack()
        self.root.mainloop()

    def modify_amplitude_and_phase(self, X, new_amplitude, new_phase_shift):
        amplitude = np.abs(X) * float(new_amplitude.get())
        phase = np.angle(X) * float(new_phase_shift.get())
        print("Modified amplitude and phase shift")
        print(amplitude, phase)



