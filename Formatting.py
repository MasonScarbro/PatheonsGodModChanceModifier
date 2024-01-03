from tkinter import *
import customtkinter as ctk
import re
from customtkinter import filedialog
import os
from pathlib import Path
import shutil

class Formatting:
    def new_label(string, frame):
        return ctk.CTkLabel(
            frame,
            text=string,
            font=ctk.CTkFont(family="", size=15, weight="bold"),
            text_color="#fcf9ff",
        )
    
    def automatedLabelCreation(arrayOfLabelNames, frame):
        for i, labelName in enumerate(arrayOfLabelNames):
            label = Formatting.new_label(labelName, frame)
            print(label)
            label.grid(row=i, column=0, padx=4, pady=4)
