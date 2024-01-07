from tkinter import *
import customtkinter as ctk
import re
from customtkinter import CTkTabview
import os
from pathlib import Path
import shutil
from Formatting import Formatting


root = ctk.CTk(fg_color="#101519")
root.geometry("650x700")
root.title("Value Editor")

tabview = ctk.CTkTabview(master=root)
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
tabview.grid(row=0, column=0, padx=20, pady=20, sticky=NSEW)

##################################### Tab Vars #########################################
knowTab = tabview.add("Knowledge God")
darkTab = tabview.add("Dark God")
starTab = tabview.add("God Of Stars")
sunTab = tabview.add("God Of Light")
warTab = tabview.add("God Of War")
earthTab = tabview.add("God Of Earth")
chaosTab = tabview.add("God Of Chaos")

##################################### ######## #########################################

######################################### Entry Dictonaries #########################################
knowledge_pwrs = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["randomMagic", "curse", "freeze", "shield", "teleport", "lightning", "meteorite", "fireball", "pages"], frame=knowTab, column=1, default_values=[20, 1, 1, 5, 4, 2, 0.5, 1, 9], generate_percentage=[True, 3])
Formatting.Labels.automatedLabelCreation(arrayOfLabelNames=["randomMagic", "curse", "freeze", "shield", "teleport", "lightning", "meteorite", "fireball", "pages"], frame=knowTab, column=0)

dark_pwrs = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["darkExpansion", "blackHole", "darkDaggers", "smokeFlash"], frame=darkTab, column=1, default_values=[0.01, 2, 20, 1])
Formatting.Labels.automatedLabelCreation(arrayOfLabelNames=["Dark Expansion", "Black Hole", "Dark Daggers", "Smoke Flash"], frame=darkTab, column=0)

stars_pwrs = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["moonFall", "cometAzure", "cometShower"], frame=starTab, column=1, default_values=[0.05, 2, 0.5])
Formatting.Labels.automatedLabelCreation(arrayOfLabelNames=["Moon Fall", "Comet Azure", "Comet Shower"], frame=starTab, column=0)

sun_pwrs = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["flashBulb", "lightBeam", "flashOfSpeed", "lightBallz"], frame=sunTab, column=1, default_values=[0.5, 0.8, 2, 0.5, 0.01])
Formatting.Labels.automatedLabelCreation(arrayOfLabelNames=["Flash Bulb", "Light Beam", "Flash Of Speed", "Light Ballz"], frame=sunTab, column=0)

war_pwrs = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["warGodsCry", "axeThrow"], frame=warTab, column=1, default_values=[1, 3])
Formatting.Labels.automatedLabelCreation(arrayOfLabelNames=["War Gods Cry", "Throw Axe"], frame=warTab, column=0)

earth_pwrs = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["earthquake", "clouds", "boulder"], frame=earthTab, column=1, default_values=[5, 10, 2])
Formatting.Labels.automatedLabelCreation(arrayOfLabelNames=["earthquake", "clouds", "boulder"], frame=earthTab, column=0)

chaos_pwrs = Formatting.Entrys.automatedEntryCreate(arrayOfVarNames=["boneFire", "fireball"], frame=chaosTab, column=1, default_values=[1, 2])
Formatting.Labels.automatedLabelCreation(arrayOfLabelNames=["Bone Fire", "FireBall"], frame=chaosTab, column=0)

######################################### ################ #########################################


def testbtnCmd():
    print(stars_pwrs["moonFall"].get())

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