import sys
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from Task1.main import Screen
from Task2.main import Task2
from Task3.main import Task3
from Task4.main import Task4
from Task5.main import Task5
from Task6.main import Task6


def open_task(root, page):
    root.destroy()
    page()


class MainScreen:
    def __init__(self):
        mainColor = '#1C113A'

        root = tk.Tk()
        root.geometry("1000x563")

        # setting background image
        image = Image.open("Photos/background.png")
        background_image = ImageTk.PhotoImage(image)
        background_label = Label(root, image=background_image)

        main_frame = tk.Frame(root, borderwidth=0, background=mainColor)
        image_label = tk.Label(main_frame, image="", borderwidth=0, background=mainColor)

        # Creating widgets
        choose_point = Image.open("Photos/chooseTask.png")
        choose_point_image = ImageTk.PhotoImage(choose_point)
        choose_point_label = Label(root, image=choose_point_image, background=mainColor)

        task1_button_image = PhotoImage(file="Photos/task1Btn.png")
        task1_button = Button(root, image=task1_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=lambda: open_task(root, Screen))

        task2_button_image = PhotoImage(file="Photos/task2Btn.png")
        task2_button = Button(root, image=task2_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=lambda: open_task(root, Task2))

        task3_button_image = PhotoImage(file="Photos/task3Btn.png")
        task3_button = Button(root, image=task3_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=lambda: open_task(root, Task3))

        task4_button_image = PhotoImage(file="Photos/task4Btn.png")
        task4_button = Button(root, image=task4_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=lambda: open_task(root, Task4))

        task5_button_image = PhotoImage(file="Photos/task5Btn.png")
        task5_button = Button(root, image=task5_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=lambda: open_task(root, Task5))

        task6_button_image = PhotoImage(file="Photos/task6Btn.png")
        task6_button = Button(root, image=task6_button_image, borderwidth=0, cursor="hand2", bd=0,
                              background='#141345', activebackground='#141345', command=lambda: open_task(root, Task6))

        # Placing widgets on the screen
        background_label.place(x=0, y=0)
        main_frame.place(anchor='center', relx=0.5, rely=0.45)
        choose_point_label.place(anchor='center', relx=0.5, y=250)
        task1_button.place(anchor='center', relx=0.3, y=350)
        task2_button.place(anchor='center', relx=0.5, y=350)
        task3_button.place(anchor='center', relx=0.7, y=350)
        task4_button.place(anchor='center', relx=0.3, y=420)
        task5_button.place(anchor='center', relx=0.5, y=420)
        task6_button.place(anchor='center', relx=0.7, y=420)
        image_label.pack()

        root.mainloop()


MainScreen()
