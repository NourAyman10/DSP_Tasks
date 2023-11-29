import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from Task6.helper_functions import plot_signals


class Smoothing:
    def __init__(self, X):
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = "#9601AB"
        self.signal = X

        self.root = tk.Tk()
        self.root.title("Smoothing Signal")
        self.root.geometry("491x276")
        self.root.configure(bg=self.mainColor)

        number_of_points_label = tk.Label(self.root, text="Number Of Points", borderwidth=0, background=self.mainColor,
                                          foreground="#FCD24F", font=("Arial", 18))

        self.number_of_points_value = StringVar(self.root, value="")
        number_of_points_entry = Entry(self.root, width=18, font=("arial", 18), bd=1,
                                       textvariable=self.number_of_points_value,
                                       background=self.mainColor, foreground=self.foregroundColor,
                                       insertbackground="#9601AB")

        smooth_btn = tk.Button(self.root, text="Smooth", borderwidth=0,
                               cursor="hand2", bd=0, background=self.foregroundColor, font=("arial", 18),
                               activebackground=self.foregroundColor, foreground="white", width=20,
                               command=lambda: self.smooth_signal(self.signal))

        number_of_points_label.pack()
        number_of_points_entry.pack()
        smooth_btn.pack(pady=20)
        self.root.mainloop()

    def smooth_signal(self, signal):
        num_points = int(self.number_of_points_value.get())

        smoothed_signal = []
        for i in range(len(signal) - num_points + 1):
            average = sum(signal[i:i + num_points]) / num_points
            smoothed_signal.append(average)

        plot_signals("Smoothing Signals", Original_Signal=self.signal, Smoothed_Signal=smoothed_signal)
        return smoothed_signal
