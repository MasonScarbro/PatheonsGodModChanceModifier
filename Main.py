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
#label_names = ["Mason", "Poop", "Fart"]
#Formatting.Labels.automatedLabelCreation(label_names, root)
#Formatting.Entrys.automatedEntryWrite("Test", arrOfVarNames=["powerOfSun", "starsPower", "lightBallzPower"], frameAsString='root')

Entry_List1 = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["Entry1", "Entry2", "Entry3"], frame=root) # TESTING

def testbtnCmd():
    print(Entry_List1["Entry2"].get())

testbtn = Formatting.Buttons.new_button(cmd=testbtnCmd, string="TEST", frame=root)
testbtn.grid(row=4, column=0, padx=2, pady=4)

# This is It this is all you need to replace the chances just change the mod code to have a variable
# for each powers chance and then rewrite each assignment/initialization to the users value instead of yours
# then just rewrite to that file... You can put the tool in the mod folder if that works but 
# otherwise use the same code before to locate the file!

'''with open(Path("C:\Program Files (x86)\Steam\steamapps\common\worldbox\Mods\Pantheon Mod\Code\Traits.cs")) as f:
    lines = f.read()
with open(Path(os.getcwd()) / "test.cs", 'w') as f:
    f.write(lines)'''
    

root.mainloop() #Main Loops