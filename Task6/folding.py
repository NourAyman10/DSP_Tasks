import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from Task6.helper_functions import plot_signals
from Task6.delaying import Delaying
from Task6.advancing import Advancing


class Folding:
    def __init__(self, X):
        self.folded_signal = None
        self.mainColor = '#270D30'
        self.secondColor = '#18103A'
        self.foregroundColor = "#9601AB"
        self.signal = X

        self.root = tk.Tk()
        self.root.title("Smoothing Signal")
        self.root.geometry("491x276")
        self.root.configure(bg=self.mainColor)

        fold_btn = tk.Button(self.root, text="Folding", borderwidth=0,
                               cursor="hand2", bd=0, background=self.foregroundColor, font=("arial", 18),
                               activebackground=self.foregroundColor, foreground="white", width=20,
                               command=lambda: self.folding_signal(self.signal))

        delay_btn = tk.Button(self.root, text="Delay", borderwidth=0,
                             cursor="hand2", bd=0, background=self.foregroundColor, font=("arial", 18),
                             activebackground=self.foregroundColor, foreground="white", width=20,
                             command=lambda: Delaying(self.folded_signal))

        advance_btn = tk.Button(self.root, text="Advance", borderwidth=0,
                             cursor="hand2", bd=0, background=self.foregroundColor, font=("arial", 18),
                             activebackground=self.foregroundColor, foreground="white", width=20,
                             command=lambda: Advancing(self.folded_signal))

        fold_btn.pack(pady=20)
        delay_btn.pack(pady=20)
        advance_btn.pack()
        self.root.mainloop()

    def folding_signal(self, signal):
        self.folded_signal = signal[::-1]
        plot_signals("Original Signal VS Folded Signal", Original_Signal=signal, Folded_Signal=self.folded_signal)
