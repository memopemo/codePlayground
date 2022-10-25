from io import TextIOWrapper
import tkinter as tk
from tkinter import filedialog
import os
import shutil

root = tk.Tk()
root.withdraw()

#TODO:
#   txt file of file locations, such as RetroArch Save Locations, SD card drive save, etc.
#   file dialog of configuring these files to the txt file

RASavs = "C:/RetroArch-Win64/saves"
GBSavs = "D:/EDGB/SAVE"
RABKSavs = "C:/Users/R T/Desktop/GBRABackups/Retroarch"
GBBKSavs = "C:/Users/R T/Desktop/GBRABackups/Gameboy"
print("Hello! Select An Option:")
print("[1] Retroarch to Gameboy")
print("[2] Gameboy to Retroarch")
print("[3] Revive Previous Save")
choice = input();
if(choice == "1"):
    RABaseName = os.path.basename(filedialog.askopenfilename(title="Select Retroarch Save...",initialdir=RASavs))
    RaSaveFilePath = RASavs + "/" + RABaseName
    GBSaveFilePath = GBSavs + "/" + RABaseName
    shutil.copy(GBSaveFilePath, GBBKSavs)
    RaSvF = open(RaSaveFilePath,'rb')
    GbSvF = open(GBSaveFilePath,'wb')
    GbSvF.write(RaSvF.read())
if(choice == "2"):
    GBBaseName = os.path.basename(filedialog.askopenfilename(title="Select Gameboy Save...",initialdir=GBSavs))
    RaSaveFilePath = RASavs + "/" + GBBaseName
    GBSaveFilePath = GBSavs + "/" + GBBaseName
    shutil.copy(RaSaveFilePath, RABKSavs)
    RaSvF = open(RaSaveFilePath,'wb')
    GbSvF = open(GBSaveFilePath,'rb')
    RaSvF.write(GbSvF.read())
RaSvF.close()
GbSvF.close()
print("Save Sucessful! :)")


    
    

