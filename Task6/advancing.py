import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from Task6.helper_functions import plot_signals
from Task6.helper_functions import advance_signal


class Advancing:
    def __init__(self, X):
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = "#9601AB"
        self.signal = X

        self.root = tk.Tk()
        self.root.title("Smoothing Signal")
        self.root.geometry("491x276")
        self.root.configure(bg=self.mainColor)

        number_of_points_label = tk.Label(self.root, text="Number Of Steps", borderwidth=0, background=self.mainColor,
                                          foreground="#FCD24F", font=("Arial", 18))

        self.number_of_points_value = StringVar(self.root, value="")
        number_of_points_entry = Entry(self.root, width=18, font=("arial", 18), bd=1,
                                       textvariable=self.number_of_points_value,
                                       background=self.mainColor, foreground=self.foregroundColor,
                                       insertbackground="#9601AB")

        smooth_btn = tk.Button(self.root, text="Advancing", borderwidth=0,
                               cursor="hand2", bd=0, background=self.foregroundColor, font=("arial", 18),
                               activebackground=self.foregroundColor, foreground="white",
                               command=lambda: self.advancing_signal(self.signal))

        number_of_points_label.pack()
        number_of_points_entry.pack()
        smooth_btn.pack()
        self.root.mainloop()

    def advancing_signal(self, signal):
        number_of_steps = int(self.number_of_points_value.get())
        advance = advance_signal(signal, number_of_steps)
        plot_signals("Original Signal VS Advance Signal", Original_Signal=signal, Advance_Signal=advance)



