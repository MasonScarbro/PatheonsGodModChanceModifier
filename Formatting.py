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
        global all_entrys
        all_entrys = []
        
        def new_entry(frame):
            return ctk.CTkEntry(
                frame,
                border_color="#1D3142",
                fg_color="#203547",
                text_color="#D0D0E1",
            )


        #WORK NEEDED!
        def automatedEntryCreate(numOfEntries, frame, column=0):
            for i in  range(numOfEntries):
                base_entry = Formatting.Entrys.new_entry(frame)
                base_entry.grid(row=i, column=column, padx=8, pady=8)
                all_entrys.append(base_entry.get())


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
                    string += enumeratedName + str(i) + " = " + "new_entry" + "(" + frameAsString + ")" + '\n'
                    #print(string)
                else:
                    print(string)
                    string += arrOfVarNames[i] + " = " + "new_entry" + "(" + frameAsString + ")" + '\n'
                
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