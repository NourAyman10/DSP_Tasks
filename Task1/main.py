from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from point1 import FirstPoint
from point2 import SecondPoint


class Screen:
    def __init__(self):
        self.mainColor = '#1C113A'

        self.root = tk.Tk()
        self.root.geometry("1000x563")

        # setting background image
        self.image = Image.open("Photos/background.png")
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background_label = Label(self.root, image=self.background_image)

        self.main_frame = tk.Frame(self.root, borderwidth=0, background=self.mainColor)
        self.image_label = tk.Label(self.main_frame, image="", borderwidth=0, background=self.mainColor)

        # Creating widgets
        self.choose_point = Image.open("Photos/choosePoint.png")
        self.choose_point_image = ImageTk.PhotoImage(self.choose_point)
        self.choose_point_label = Label(self.root, image=self.choose_point_image, background=self.mainColor)

        self.task1_button_image = PhotoImage(file="Photos/point1Btn.png")
        self.task1Button = Button(self.root, image=self.task1_button_image, borderwidth=0, cursor="hand2", bd=0,
                                  background='#141345', activebackground='#141345', command=FirstPoint)

        self.task2_button_image = PhotoImage(file="Photos/point2Btn.png")
        self.task2Button = Button(self.root, image=self.task2_button_image, borderwidth=0, cursor="hand2", bd=0,
                                  background='#141345', activebackground='#141345', command=self.openSecondPoint)

        # Placing widgets on the screen
        self.background_label.place(x=0, y=0)
        self.main_frame.place(anchor='center', relx=0.5, rely=0.45)
        self.choose_point_label.place(anchor='center', relx=0.5, y=250)
        self.task1Button.place(anchor='center', relx=0.3, y=390)
        self.task2Button.place(anchor='center', relx=0.7, y=390)
        self.image_label.pack()

        self.root.mainloop()

    def openSecondPoint(self):
        self.root.destroy()
        SecondPoint()

Screen()