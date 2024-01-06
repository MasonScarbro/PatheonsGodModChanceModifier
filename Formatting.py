from tkinter import *
import customtkinter as ctk
import re
from customtkinter import filedialog
import os
from pathlib import Path
import shutil

class Formatting:

    # Label funcs #
    class Labels:

        def new_label(string, frame):
            return ctk.CTkLabel(
                frame,
                text=string,
                font=ctk.CTkFont(family="", size=15, weight="bold"),
                text_color="#fcf9ff",
            )
    

        def automatedLabelCreation(arrayOfLabelNames, frame, column=0):
            for i, labelName in enumerate(arrayOfLabelNames):
                label = Formatting.Labels.new_label(labelName, frame)
                print(label)
                label.grid(row=i, column=column, padx=4, pady=4)
    
    class Entrys:
        
        
        def new_entry(frame):
            return ctk.CTkEntry(
                frame,
                border_color="#1D3142",
                fg_color="#203547",
                text_color="#D0D0E1",
            )


        
        def automatedEntryCreate(arrayOfVarNames, frame, column=0):
            all_entrys = {}
            for i in range(len(arrayOfVarNames)):
                base_entry = Formatting.Entrys.new_entry(frame)
                base_entry.grid(row=i, column=column, padx=8, pady=8)
                all_entrys[arrayOfVarNames[i]] = base_entry
            print(all_entrys)
            return all_entrys


        def format_entry_util(entryArr, column):
            for i, entryArr in enumerate(entryArr):
                entryArr.grid(row=i, column=column, padx=2, pady=4)


        def automatedEntryWrite(enumeratedName, numOfEntries=0, arrOfVarNames=[], frameAsString='root', path=os.getcwd(), formmatted=True, column=0, fileName="WritedFile", append=True):
            global string
            string = ""
            #print(numOfEntries == 0)
            
            if numOfEntries == 0: numOfEntries = len(arrOfVarNames)
            print(" And the Arr is: " + str(len(arrOfVarNames)))
            for i in range(numOfEntries):
                if len(arrOfVarNames) == 0:
                    string += enumeratedName + str(i) + " = " + "Formatting.Entrys.new_entry" + "(" + frameAsString + ")" + '\n'
                    #print(string)
                else:
                    print(string)
                    string += arrOfVarNames[i] + " = " + "Formatting.Entrys.new_entry" + "(" + frameAsString + ")" + '\n'
                
            if formmatted == True:
                string += enumeratedName + "Arr" + " = " + "[\n" 
                for i in  range(numOfEntries):
                    if len(arrOfVarNames) == 0:
                        string += enumeratedName + str(i) + "," + "\n"
                        #print(string)
                    else:
                        string += arrOfVarNames[i] + "," + "\n"
                string += "\n]\n"
                string += "Formatting.Entrys.format_entry_util(" + enumeratedName + ", " + str(column) + ")"
                if append:
                    with open(Path(path) / Path(fileName + ".py"), 'a') as f:
                        f.write(string)
                else:
                    with open(Path(path) / Path(fileName + ".py"), 'w') as f:
                        f.write(string)
    
    class Buttons:
        def new_button(string, cmd, frame): 
            return ctk.CTkButton(frame, text=string, width=100, fg_color="#fcf9ff", text_color="#101519", corner_radius=5, command=cmd)