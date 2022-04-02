# Title:        inter_planetary_weights.py
# Author:       Lennox Stampp
# Date:         3/30/2022
# Purpose:      "calculate a person’s weight on the different planets within
#               our solar system by multiplying their mass by the gravity
#               factor on the surface of the planet."

import tkinter as tk
from tkinter import PhotoImage


# Variables
nDICTCNVRSNFCTR = {
    "Mercury" : 0.38,
    "Venus" : 0.91,
    "Moon" : 0.165,
    "Earth" : 1,
    "Mars" : 0.38,
    "Jupiter" : 2.34,
    "Saturn" : 0.93,
    "Uranus" : 0.92,
    "Neptune" : 1.12,
    "Pluto" : 0.066
}

nIntrPlntWt = {}        #hold the current user weight for each planet
aUserInfo = ["", 0]      #index pos 0 = username(sName) | pos 1 = weight(nWeight)

# Functions

#---Test Funcs---
def ckVars(*args):
    for arg in args:
        print(arg)

# Set sName and nEarthWght vars from entry fields
def setNmWtVars(name_entry,wt_entry):
    try:
        aUserInfo[0] = name_entry.get()
        aUserInfo[1] = float(wt_entry.get())
    except:
        #--TODO-- Disallow submit to be pressed if entry invalid
        pass

def calcWeights():
    for key,val in nDICTCNVRSNFCTR.items():
        nIntrPlntWt[key] = val * aUserInfo[1]

#--TODO--#
# Fuction to Clear entries and reset variables

# GUI windows

#--Main/Intro Window
def introWin():
    # Intro main window
    mainWindw = tk.Tk()
    mainWindw.title("Inter Planetary Weights GUI - By Lennox Stampp")
    mainWindw.config(bg="#0d0d0d")      # #0d0d0d color is a shade of black
    #main_win_width = mainWindw.winfo_screenwidth() #useless i think?? if so delete width from frames

    # Frames
    titleFrame = tk.Frame(mainWindw,bg="yellow",relief=tk.RIDGE, borderwidth=5)
    entryFrame = tk.Frame(mainWindw,bg="black",relief=tk.RIDGE, borderwidth=5)
    buttonFrame = tk.Frame(entryFrame, pady=8,bg="black")

    # Title frame widgets
    lblTitle = tk.Label(
        titleFrame,
        text="Inter Planetary Weights\nYour weight throughout the Solar System!",
        fg="yellow",
        bg="#0d0d0d",
        justify="center"
    )

    # Entry frame widgets
    lblNameEntry = tk.Label(entryFrame, text="Enter your name:",
                            fg="yellow", bg="#0d0d0d")
    lblWeightEntry = tk.Label(entryFrame, text="Enter your Earth weight(lbs):",
                              fg="yellow", bg="#0d0d0d")

    # Entry fields
    entNameEntryField = tk.Entry(entryFrame, relief=tk.SUNKEN)
    entWeightEntryField = tk.Entry(entryFrame, relief=tk.SUNKEN)

    # Button frame widgets
    #--Submit button
    btnShowDispWin = tk.Button(buttonFrame,
                               text="Calculate Weights",
                               command=lambda:[setNmWtVars(entNameEntryField,entWeightEntryField),
                                               dispWin(),
                                               ckVars(aUserInfo),
                                               calcWeights(),
                                               mainWindw.destroy()],
                               bg="yellow",
                               fg="black"
                               )

    #--Close button
    btnCloseWin = tk.Button(buttonFrame,
                            text="Exit",
                            command=lambda:mainWindw.destroy(),
                            bg="yellow",
                            fg="black"
                            )

    # Build out window
    titleFrame.pack(fill="both")
    lblTitle.pack()
    entryFrame.pack(fill="both")
    lblNameEntry.pack()
    entNameEntryField.pack()
    lblWeightEntry.pack()
    entWeightEntryField.pack()
    buttonFrame.pack()
    btnShowDispWin.pack(side="left")
    btnCloseWin.pack(side="right")

#--Result/Display windo
def dispWin():
    # Variables
    sPlanetNamesIndxdList = [x for x in nDICTCNVRSNFCTR]
    print(sPlanetNamesIndxdList)
    iIndxCurntPlnt = 0
    sCurrentPlanet = sPlanetNamesIndxdList[iIndxCurntPlnt]
    print(sCurrentPlanet)
    sTitleStr = aUserInfo[0] + " on " + sCurrentPlanet
    # Planet image dict
    imgPlanetImgDict = {"Mercury":"mercury_img_png.png"}
    print(f"path for file = {imgPlanetImgDict[sCurrentPlanet]}")
    #imgCurentImg = tk.PhotoImage(file=imgPlanetImgDict[sCurrentPlanet])
    #imgCurentImg = tk.PhotoImage(imgPlanetImgDict[sCurrentPlanet])

    # Functions
    # Incremennt iIndxCurntPlnt
    def setNextIndx():
        iIndxCurntPlnt += 1

    def setPrevIndx():
        iIndxCurntPlnt -= 1

    # Display window
    dispWin = tk.Tk()
    dispWin.title("Inter Planetary Weights GUI - By Lennox Stampp")
    dispWin.config(bg="#0d0d0d")
    dispWin.geometry("800x800")

    # Frames
    titleFrame = tk.Frame(dispWin, bg="yellow")
    imageFrame = tk.Frame(dispWin, bg="orange")
    dataDispFrame = tk.Frame(dispWin)
    buttonFrame = tk.Frame(dispWin)

    # Title frame widget
    lblHeading = tk.Label(titleFrame,
                          text=sTitleStr, bg="black", fg="yellow")
    # Image frame widget
    lblPlanetImage = tk.Label(imageFrame)
    imgCurentImg = tk.PhotoImage(master=lblPlanetImage,file=imgPlanetImgDict[sCurrentPlanet])
    #imgCurentImg = tk.PhotoImage(master=lblPlanetImage, file="mercury_img_png.png")
    lblPlanetImage.imgCurentImg = imgCurentImg
    lblPlanetImage.config(image=imgCurentImg)

    # Data display frame widget
    txtDispArea = tk.Text(dataDispFrame, bg="yellow", fg="black")

    # Button frame widgets
    btnPrev = tk.Button(buttonFrame, text="Prev")
    btnNext = tk.Button(buttonFrame, text="Next")
    btnList = tk.Button(buttonFrame, text="List All")
    btnExit = tk.Button(buttonFrame, text="Exit", command=lambda:dispWin.destroy())

    # Build window
    titleFrame.pack(fill="both")
    lblHeading.pack()
    imageFrame.pack(fill="both")
    lblPlanetImage.pack(anchor="center")


# Main
def main():
    introWin()
    tk.mainloop()

# Run app
main()