from helper_functions import load_file
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Files.QuanTest2 import QuantizationTest2


def get_levels(number,type):
    print("get levels")
    if type=="level":
        return number
    else:
        return 2**int(number)

    


def quantization():
    print("Quantization")
    signal=load_file('DSP_Tasks/Task3/Files/Quan2_input.txt')
    levels=get_levels(3,'level')
    generate_range(signal,levels)
    return signal,levels
def binary_search(array,target):
    print("binary search")
    left=0
    right=len(array)-1
    while left<= right:
        mid=(left+right)//2
        if array[mid]==target:
            return mid
        elif array[mid]<target:
            left=mid+1
        else:
            right=mid-1    
    return -1


def generate_range(signal,levels):
    print("generate range")
    min_amp=np.min(signal)
    max_amp=np.max(signal)
    delta=(max_amp-min_amp)/levels
    ranges=np.arange(min_amp,max_amp,delta)
    return ranges

def get_interval_idx(signal,levels):
    print("get_interval_idx")
    ranges=generate_range(signal,levels)
    interval_indices=[]
    for i in signal:
        interval_indices.append(int(binary_search(ranges,i)+1))
    return interval_indices



def calculate_midpoints(indices):
    print("calculate_midpoints")
    midpoints = []
    for i in range(len(indices) - 1):
        start_index = indices[i]
        end_index = indices[i + 1]
        midpoint = (start_index + end_index) / 2.0
        midpoints.append(midpoint)
    return midpoints    


def quantized_signal(signal,levels):
    print("quantized_signal")
    indices=get_interval_idx(signal,levels)
    midpoints=calculate_midpoints(indices)
    xq=[]
    for i in indices:
        xq.append(midpoints[i-1])
    return xq


def quantizated_error(signal,levels):
    print("quantized_error")
    xq=quantized_signal(signal,levels)
    return xq-signal

def Average_power_error(signal,levels):
    print("Average_power_error")
    quantized_err=quantizated_error(signal,levels)
    error = [sample ** 2 for sample in quantized_err]  
    average_power = sum(error) / len(error)
    return average_power

# def encoded_signal(signal,levels):
#     print("encode_signal")
#     return bin(get_interval_idx(signal,levels))

def encoded_signal(signal, levels):
    interval_indices = get_interval_idx(signal, levels)
    return bin(int("".join(map(str, interval_indices)), 2))




class Task2:
    def __init__(self):
        signal, levels = quantization()
        QuantizationTest2("DSP_Tasks/Task3/Files/Quan2_Out.txt", get_interval_idx(signal, levels), encoded_signal(signal, levels), quantized_signal(signal, levels), quantizated_error(signal, levels))

Task2()
        





# class Task2:
#     def __init__(self):
#         # self.mainColor = '#1C113A'
#         # self.subColor = '#141445'

#         # root = tk.Tk()
#         # root.geometry("1300x563")

#         # main_frame = Frame(root)
#         # # setting background image
#         # image = Image.open("../DSP_Tasks/Photos/sub_background.png")
#         # background_image = ImageTk.PhotoImage(image)
#         # background_label = Label(main_frame, image=background_image)
#        signal=load_file('DSP_Tasks/Task3/Files/Quan2_input.txt')
#        levels=get_levels(3,'level')
#        generate_range(signal,levels)
#        QuantizationTest2("DSP_Tasks/Task3/Files/Quan2_Out.txt",get_interval_idx(signal,levels),encoded_signal(signal,levels),quantized_signal(signal,levels),quantizated_error(signal,levels))
# Task2()