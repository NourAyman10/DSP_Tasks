import os
import sys
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from Task2.first_frame import Addition
from Task2.second_frame import Subtraction
from Task2.third_frame import Multiplication
from Task2.fourth_frame import Squaring
from Task2.fifth_frame import Shifting
from Task2.sixth_frame import Normalization
from Task2.seventh_frame import Accumulation


class Task2:
    def __init__(self):
        self.mainColor = '#1C113A'
        self.subColor = '#141445'

        root = tk.Tk()
        root.geometry("1300x563")

        main_frame = Frame(root)
        # setting background image
        image = Image.open("../DSP_Tasks/Photos/sub_background.png")
        background_image = ImageTk.PhotoImage(image)
        background_label = Label(main_frame, image=background_image)

        sub_frame = tk.Frame(main_frame, borderwidth=0, background=self.mainColor)
        image_label = tk.Label(sub_frame, image="", borderwidth=0, background=self.mainColor)

        background_label.place(x=0, y=0)
        sub_frame.place(anchor='center', relx=0.5, rely=0.45)

        main_frame.pack(side=RIGHT)
        main_frame.pack_propagate(False)
        main_frame.configure(width=1000, height=563)

        options_frame = Frame(root, borderwidth=0, background=self.mainColor)

        page1_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/addition.png")
        self.page1_btn = Button(options_frame, image=page1_button_image, borderwidth=0, cursor="hand2", bd=0,
                                background=self.subColor, activebackground=self.subColor,
                                command=lambda: self.indicate(Addition, main_frame, self.page1_btn))

        page2_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/subtraction.png")
        self.page2_btn = Button(options_frame, image=page2_button_image, borderwidth=0, cursor="hand2", bd=0,
                                background=self.subColor, activebackground=self.subColor,
                                command=lambda: self.indicate(Subtraction, main_frame, self.page2_btn))

        page3_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/multiplication.png")
        self.page3_btn = Button(options_frame, image=page3_button_image, borderwidth=0, cursor="hand2", bd=0,
                                background=self.subColor, activebackground=self.subColor,
                                command=lambda: self.indicate(Multiplication, main_frame, self.page3_btn))

        page4_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/squaring.png")
        self.page4_btn = Button(options_frame, image=page4_button_image, borderwidth=0, cursor="hand2", bd=0,
                                background=self.subColor, activebackground=self.subColor,
                                command=lambda: self.indicate(Squaring, main_frame, self.page4_btn))

        page5_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/shifting.png")
        self.page5_btn = Button(options_frame, image=page5_button_image, borderwidth=0, cursor="hand2", bd=0,
                                background=self.subColor, activebackground=self.subColor,
                                command=lambda: self.indicate(Shifting, main_frame, self.page5_btn))

        page6_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/normalization.png")
        self.page6_btn = Button(options_frame, image=page6_button_image, borderwidth=0, cursor="hand2", bd=0,
                                background=self.subColor, activebackground=self.subColor,
                                command=lambda: self.indicate(Normalization, main_frame, self.page6_btn))

        page7_button_image = PhotoImage(file="../DSP_Tasks/Photos/Task2/accumulation.png")
        self.page7_btn = Button(options_frame, image=page7_button_image, borderwidth=0, cursor="hand2", bd=0,
                                background=self.subColor, activebackground=self.subColor,
                                command=lambda: self.indicate(Accumulation, main_frame, self.page7_btn))

        options_frame.pack(side=LEFT)
        options_frame.pack_propagate(False)
        options_frame.configure(width=300, height=563)

        self.page1_btn.place(relx=0.25, rely=0.2)
        self.page2_btn.place(relx=0.15, rely=0.3)
        self.page3_btn.place(relx=0.07, rely=0.4)
        self.page4_btn.place(relx=0.25, rely=0.5)
        self.page5_btn.place(relx=0.25, rely=0.6)
        self.page6_btn.place(relx=0.1, rely=0.7)
        self.page7_btn.place(relx=0.12, rely=0.8)

        image_label.pack()

        root.mainloop()

    def indicate(self, page, main_frame, button):
        self.hide_indicators()
        button.config(bd=8, background="#D00096", relief=FLAT)
        self.navigate(page, main_frame)

    def hide_indicators(self):
        self.page1_btn.config(bd=0, background=self.subColor)
        self.page2_btn.config(bd=0, background=self.subColor)
        self.page3_btn.config(bd=0, background=self.subColor)
        self.page4_btn.config(bd=0, background=self.subColor)
        self.page5_btn.config(bd=0, background=self.subColor)
        self.page6_btn.config(bd=0, background=self.subColor)
        self.page7_btn.config(bd=0, background=self.subColor)

    def navigate(self, page, main_frame):
        self.delete_pages(main_frame)
        page(main_frame)

    def delete_pages(self, main_frame):
        for frame in main_frame.winfo_children():
            frame.destroy()
