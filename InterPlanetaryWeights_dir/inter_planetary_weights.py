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
    "Mercury": 0.38,
    "Venus": 0.91,
    "Moon": 0.165,
    "Earth": 1.0,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 0.93,
    "Uranus": 0.92,
    "Neptune": 1.12,
    "Pluto": 0.066
}

nIntrPlntWtDict = {}  # hold the current user weight for each planet
aUserInfo = ["", 0]  # index pos 0 = username | pos 1 = weight


# Functions

# ---Test Funcs---
def ckVars(*args):
    for arg in args:
        print(arg)


# Set sName and nEarthWght vars from entry fields
def setNmWtVars(name_entry, wt_entry):
    try:
        aUserInfo[0] = name_entry.get()
        aUserInfo[1] = float(wt_entry.get())
    except:
        # --TODO-- Disallow submit to be pressed if entry invalid
        pass


def calcWeights():
    for key, val in nDICTCNVRSNFCTR.items():
        nIntrPlntWtDict[key] = val * aUserInfo[1]


# --TODO--#
# Fuction to Clear entries and reset variables

# GUI windows

# --Main/Intro Window
def introWin():
    # Intro main window
    mainWindw = tk.Tk()
    mainWindw.title("Inter Planetary Weights GUI - By Lennox Stampp")
    mainWindw.config(bg="black")  # #0d0d0d color is a shade of black
    # main_win_width = mainWindw.winfo_screenwidth() #useless i think?? if so delete width from frames

    # Frames
    titleFrame = tk.Frame(mainWindw, bg="yellow", relief=tk.RIDGE, borderwidth=5)
    entryFrame = tk.Frame(mainWindw, bg="black", relief=tk.RIDGE, borderwidth=5)
    buttonFrame = tk.Frame(entryFrame, pady=8, bg="black")

    # Title frame widgets
    lblTitle = tk.Label(
        titleFrame,
        text="Inter Planetary Weights\nYour weight throughout the Solar System!",
        fg="yellow",
        bg="black",
        justify="center"
    )

    # Entry frame widgets
    lblNameEntry = tk.Label(entryFrame, text="Enter your name:",
                            fg="yellow", bg="black")
    lblWeightEntry = tk.Label(entryFrame, text="Enter your Earth weight(lbs):",
                              fg="yellow", bg="black")

    # Entry fields
    entNameEntryField = tk.Entry(entryFrame, relief=tk.SUNKEN)
    entWeightEntryField = tk.Entry(entryFrame, relief=tk.SUNKEN)

    # Button frame widgets
    # --Submit button
    btnShowDispWin = tk.Button(buttonFrame,
                               text="Calculate Weights",
                               command=lambda: [setNmWtVars(entNameEntryField, entWeightEntryField),
                                                calcWeights(),
                                                dispWin(),
                                                ckVars(aUserInfo),
                                                mainWindw.destroy()],
                               bg="yellow",
                               fg="black",
                               activebackground="black",
                               activeforeground="yellow"
                               )

    # --Close button
    btnCloseWin = tk.Button(buttonFrame,
                            text="Exit",
                            command=lambda: mainWindw.destroy(),
                            bg="yellow",
                            fg="black",
                            activebackground="black",
                            activeforeground="yellow"
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


# --Result/Display windo
def dispWin():
    # Variables
    sPlanetNamesIndxdList = [x for x in nDICTCNVRSNFCTR]
    print(sPlanetNamesIndxdList)
    iIndxCurntPlnt = tk.IntVar()
    intIndxCurntPlnt = int(iIndxCurntPlnt.get())
    # sCurrentPlanet = sPlanetNamesIndxdList[intIndxCurntPlnt]
    sCurrentPlanet = tk.StringVar()
    sCurrentPlanet.set(sPlanetNamesIndxdList[intIndxCurntPlnt])
    print(sCurrentPlanet)
    sTitleStr = aUserInfo[0] + " on " + sCurrentPlanet.get()

    # Planet image dict
    imgPlanetImgDict = {"Mercury": "mercury_img2.png",
                        "Venus": "venus_img2.png",
                        "Moon": "moon_img2.png",
                        "Earth": "earth_img2.png",
                        "Mars": "mars_img2.png",
                        "Jupiter": "jupiter_img2.png",
                        "Saturn": "saturn_img2.png",
                        "Neptune": "neptune_img2.png",
                        "Uranus": "uranus_img2.png",
                        "Pluto" : "pluto_img2.png"
                        }
    print(f"path for file = {imgPlanetImgDict[sCurrentPlanet.get()]}")

    # imgCurentImg = tk.PhotoImage(file=imgPlanetImgDict[sCurrentPlanet])
    # imgCurentImg = tk.PhotoImage(imgPlanetImgDict[sCurrentPlanet])

    # Functions

    # Incremennt iIndxCurntPlnt
    def setNextIndx(event=None):
        if iIndxCurntPlnt.get() == 9:
            iIndxCurntPlnt.set(0)
        else:
            iIndxCurntPlnt.set(iIndxCurntPlnt.get() + 1)
        sCurrentPlanet.set(sPlanetNamesIndxdList[iIndxCurntPlnt.get()])
        sTitleStr = aUserInfo[0] + " on " + sCurrentPlanet.get()
        lblHeading.config(text=sTitleStr)
        sDispData = f"{sTitleStr}:\nWeight on {sCurrentPlanet.get():<8}:{' . ' * 9:^12}{nIntrPlntWtDict[sCurrentPlanet.get()]:>10,.{2}f}lbs."
        txtDispArea.delete("1.0", tk.END)
        txtDispArea.insert(tk.END, sDispData)
        # txtDispArea.insert(tk.END, sCurrentPlanet.get())
        nextImg = tk.PhotoImage(master=lblPlanetImage, file=imgPlanetImgDict[sCurrentPlanet.get()])
        lblPlanetImage.image = nextImg
        lblPlanetImage.config(image=nextImg)

    def setPrevIndx(event=None):
        iIndxCurntPlnt.set(iIndxCurntPlnt.get() - 1)
        sCurrentPlanet.set(sPlanetNamesIndxdList[iIndxCurntPlnt.get()])
        sTitleStr = aUserInfo[0] + " on " + sCurrentPlanet.get()
        lblHeading.config(text=sTitleStr)
        sDispData = f"{sTitleStr}:\nWeight on {sCurrentPlanet.get():<8}:{' . ' * 9:^12}{nIntrPlntWtDict[sCurrentPlanet.get()]:>10,.{2}f}lbs."
        txtDispArea.delete("1.0", tk.END)
        txtDispArea.insert(tk.END, sDispData)
        nextImg = tk.PhotoImage(master=lblPlanetImage, file=imgPlanetImgDict[sCurrentPlanet.get()])

        lblPlanetImage.image = nextImg
        lblPlanetImage.config(image=nextImg)

    def listAllData(event=None):
        sHeading = f"{aUserInfo[0]}, here are your weights\non our Solar System's planets"
        lblHeading.config(text=sHeading)
        nextImg = tk.PhotoImage(master=lblPlanetImage, file="solar_system_img2.png")
        lblPlanetImage.image = nextImg
        lblPlanetImage.config(image=nextImg)
        txtDispArea.delete("1.0", tk.END)
        sLine1 = f"{aUserInfo[0]}'s weight on:\n"
        txtDispArea.insert(tk.END, sLine1)
        for key, val in nIntrPlntWtDict.items():
            data = f"\n\t{key:<8}:{' . ' * 5:^12}{val:>8,.{2}f}lbs.\n"
            txtDispArea.insert(tk.END, data)

    # Display window
    dispWinw = tk.Tk()
    dispWinw.title("Inter Planetary Weights GUI - By Lennox Stampp")
    dispWinw.config(bg="yellow", highlightbackground="yellow", highlightcolor="yellow", highlightthickness=10)
    #dispWin.geometry('1000x1000')
    winWidth = dispWinw.winfo_screenwidth()
    winHeight = dispWinw.winfo_screenheight()
    # nWidth = int(winWidth/10)
    nWidth = 42
    nheight = 10

    # Frames
    titleFrame = tk.Frame(dispWinw, bg="black", width=nWidth, highlightbackground="yellow", highlightcolor="yellow",
                          highlightthickness=5)
    imageFrame = tk.Frame(dispWinw, bg="black", width=nWidth, highlightbackground="yellow", highlightcolor="yellow",
                          highlightthickness=5)
    dataDispFrame = tk.Frame(dispWinw, height=nheight, width=nWidth, highlightbackground="yellow",
                             highlightcolor="yellow", highlightthickness=5, pady=2)
    buttonFrame = tk.Frame(dispWinw, width=nWidth, bg="black")

    # Title frame widget
    lblHeading = tk.Label(titleFrame,
                          text=sTitleStr, bg="black", fg="yellow", width=nWidth)

    # Image frame widget
    lblPlanetImage = tk.Label(imageFrame)
    # --TODO-- add try/escape for loading image. in escape, if image doesn't load, just add text of plnt name'
    imgCurentImg = tk.PhotoImage(master=lblPlanetImage, file=imgPlanetImgDict[sCurrentPlanet.get()])
    # imgCurentImg = tk.PhotoImage(master=lblPlanetImage, file="mercury_img_png.png")
    lblPlanetImage.image = imgCurentImg
    lblPlanetImage.config(image=imgCurentImg)

    # Data display frame widget
    sDispData = f"{sTitleStr}:\nWeight on {sCurrentPlanet.get():<8}:{'. ' * 9:^12}{nIntrPlntWtDict[sCurrentPlanet.get()]:>10,.{2}f}lbs."
    txtDispArea = tk.Text(dataDispFrame, bg="black", fg="yellow", width=nWidth, height=nheight)
    txtDispArea.insert(tk.END, sDispData)

    # Button frame widgets
    btnPrev = tk.Button(buttonFrame, text="Prev",fg="black", bg="yellow",
                        activebackground="black", activeforeground="yellow")
    btnPrev.bind('<ButtonPress>', lambda event: setPrevIndx(event))
    btnNext = tk.Button(buttonFrame, text="Next",fg="black", bg="yellow",
                        activebackground="black", activeforeground="yellow")
    btnNext.bind('<ButtonPress>', lambda event: setNextIndx(event))
    btnList = tk.Button(buttonFrame, text="List All",fg="black", bg="yellow",
                        activebackground="black", activeforeground="yellow")
    btnList.bind('<ButtonPress>', lambda event: listAllData(event))
    btnExit = tk.Button(buttonFrame, text="Exit", command=lambda: dispWinw.destroy(),fg="black", bg="yellow",
                        activebackground="black", activeforeground="yellow")

    # Build window
    buttonFrame.pack(side="bottom", fill="both", pady=5)
    titleFrame.pack(fill="both")
    lblHeading.pack()
    imageFrame.pack(fill="x")
    lblPlanetImage.pack()
    dataDispFrame.pack(fill="both")
    txtDispArea.pack(fill="x")
    btnPrev.pack(side="left")
    btnNext.pack(side="left")
    btnList.pack(side="left")
    btnExit.pack(side="right")


# Main
def main():
    introWin()
    tk.mainloop()


# Run app
main()