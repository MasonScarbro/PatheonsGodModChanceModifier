from tkinter import *
import customtkinter as ctk
import re
from customtkinter import filedialog
import os
from pathlib import Path
import shutil
from Formatting import Formatting


root = ctk.CTk(fg_color="#101519")

root.geometry("1800x900")
root.title("Value Editor")
label_names = ["Mason", "Poop", "Fart"]
Formatting.Labels.automatedLabelCreation(label_names, root)
Formatting.Entrys.automatedEntryWrite("Test", arrOfVarNames=["powerOfSun", "starsPower", "lightBallzPower"], frameAsString='root')
root.mainloop() #Main Loops