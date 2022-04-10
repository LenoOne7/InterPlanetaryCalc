# Title:        inter_planetary_weights.py
# Author:       Lennox Stampp
# Date:         3/30/2022
# Purpose:      "calculate a person’s weight on the different planets within
#               our solar system by multiplying their mass by the gravity
#               factor on the surface of the planet."

import tkinter as tk
from tkinter import PhotoImage, messagebox

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

# Set sName and nEarthWght vars from entry fields
def setNmWtVars(name_entry, wt_entry):
    try:
        aUserInfo[0] = name_entry.get()
        aUserInfo[1] = float(wt_entry.get())
    except:
        # --TODO-- Disallow submit to be pressed if entry invalid
        tk.messagebox.showinfo("Bad entry data", "Please exit program and reopen. Enter numbers only for weight.")


def calcWeights():
    for key, val in nDICTCNVRSNFCTR.items():
        nIntrPlntWtDict[key] = val * aUserInfo[1]


# --TODO--#
# Fuction to Clear entries and reset variables to allow for retentry of data on intro window

# GUI windows

# --Main/Intro Window
def introWin():
    # Intro/main window
    mainWindw = tk.Tk()
    mainWindw.title("Inter Planetary Weights GUI - By Lennox Stampp")
    mainWindw.config(bg="black")

    # Frames
    titleFrame = tk.Frame(mainWindw, bg="yellow", relief=tk.RIDGE, borderwidth=5)
    entryFrame = tk.Frame(mainWindw, bg="black", relief=tk.RIDGE, borderwidth=5)
    buttonFrame = tk.Frame(entryFrame, pady=8, bg="black")

    # Title frame widgets
    lblTitle = tk.Label(
        titleFrame,
        font="bold",
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
                               command=lambda: [setNmWtVars(entNameEntryField,entWeightEntryField),
                                                calcWeights(),
                                                dispWin(),
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


# --Result/Display window
def dispWin():
    # Variables
    sPlanetNamesIndxdList = [x for x in nDICTCNVRSNFCTR]
    iIndxCurntPlnt = tk.IntVar()
    intIndxCurntPlnt = int(iIndxCurntPlnt.get())
    sCurrentPlanet = tk.StringVar()
    sCurrentPlanet.set(sPlanetNamesIndxdList[intIndxCurntPlnt])
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

    # dispWin Functions

    # Incremennt iIndxCurntPlnt and update screen
    def setNextIndx(event=None):
        # If last image, go to first
        if iIndxCurntPlnt.get() == 9:
            iIndxCurntPlnt.set(0)
        else:
            iIndxCurntPlnt.set(iIndxCurntPlnt.get() + 1)
        # Update variables and widgets
        sCurrentPlanet.set(sPlanetNamesIndxdList[iIndxCurntPlnt.get()])
        # Heading
        sTitleStr = aUserInfo[0] + " on " + sCurrentPlanet.get()
        lblHeading.config(text=sTitleStr)
        # Display data
        sDispData = f"{sTitleStr}:\nWeight on {sCurrentPlanet.get():<8}:{' . ' * 9:^12}{nIntrPlntWtDict[sCurrentPlanet.get()]:>10,.{2}f} lbs."
        txtDispArea.delete("1.0", tk.END)
        txtDispArea.insert(tk.END, sDispData)
        # Create and update new image
        nextImg = tk.PhotoImage(master=lblPlanetImage, file=imgPlanetImgDict[sCurrentPlanet.get()])
        lblPlanetImage.image = nextImg
        lblPlanetImage.config(image=nextImg)

    # Decrement iIndxCurntPlnt and update screen
    def setPrevIndx(event=None):
        # Update variables and widgets
        iIndxCurntPlnt.set(iIndxCurntPlnt.get() - 1)
        sCurrentPlanet.set(sPlanetNamesIndxdList[iIndxCurntPlnt.get()])
        # Heading
        sTitleStr = aUserInfo[0] + " on " + sCurrentPlanet.get()
        lblHeading.config(text=sTitleStr)
        # Display data
        sDispData = f"{sTitleStr}:\nWeight on {sCurrentPlanet.get():<8}:{' . ' * 9:^12}{nIntrPlntWtDict[sCurrentPlanet.get()]:>10,.{2}f} lbs."
        txtDispArea.delete("1.0", tk.END)
        txtDispArea.insert(tk.END, sDispData)
        # Create and update new image
        nextImg = tk.PhotoImage(master=lblPlanetImage, file=imgPlanetImgDict[sCurrentPlanet.get()])
        lblPlanetImage.image = nextImg
        lblPlanetImage.config(image=nextImg)

    # Show all weight and planets on one screen
    def listAllData(event=None):
        # Heading
        sHeading = f"{aUserInfo[0]}, here are your weights\non our Solar System's planets"
        lblHeading.config(text=sHeading)
        # Create and update new image
        nextImg = tk.PhotoImage(master=lblPlanetImage, file="solar_system_img2.png")
        lblPlanetImage.image = nextImg
        lblPlanetImage.config(image=nextImg)
        # Display data
        txtDispArea.delete("1.0", tk.END)
        sLine1 = f"{aUserInfo[0]}'s weight on (scroll to view all):\n"
        txtDispArea.insert(tk.END, sLine1)
        for key, val in nIntrPlntWtDict.items():
            data = f"\n\t{key:<8}:{' . ' * 5:^12}{val:>8,.{2}f} lbs.\n"
            txtDispArea.insert(tk.END, data)

    # Display window
    dispWinw = tk.Tk()
    dispWinw.title("Inter Planetary Weights GUI - By Lennox Stampp")
    dispWinw.config(bg="yellow", highlightbackground="yellow", highlightcolor="yellow", highlightthickness=10)
    winWidth = dispWinw.winfo_screenwidth()
    winHeight = dispWinw.winfo_screenheight()
    nWidth = 42     # Use for setting screen/widget width
    nheight = 10    # Use for setting screen/widget height

    # Frames
    titleFrame = tk.Frame(dispWinw, bg="black", width=nWidth, highlightbackground="yellow", highlightcolor="yellow",
                          highlightthickness=5)
    imageFrame = tk.Frame(dispWinw, bg="black", width=nWidth, highlightbackground="yellow", highlightcolor="yellow",
                          highlightthickness=5)
    dataDispFrame = tk.Frame(dispWinw, height=nheight, width=nWidth, highlightbackground="yellow",
                             highlightcolor="yellow", highlightthickness=5, pady=2)
    buttonFrame = tk.Frame(dispWinw, width=nWidth, bg="black")

    # Title frame widget
    lblHeading = tk.Label(titleFrame,font="bold", text=sTitleStr, bg="black", fg="yellow", width=nWidth)

    # Image frame widget
    lblPlanetImage = tk.Label(imageFrame)
    # --TODO-- add try/except for loading image. In except block, if image doesn't load, just add text of plnt name'
    imgCurentImg = tk.PhotoImage(master=lblPlanetImage, file=imgPlanetImgDict[sCurrentPlanet.get()])
    lblPlanetImage.image = imgCurentImg
    lblPlanetImage.config(image=imgCurentImg)

    # Data display frame widget
    sDispData = f"{sTitleStr}:\nWeight on {sCurrentPlanet.get():<8}:{'. ' * 9:^12}{nIntrPlntWtDict[sCurrentPlanet.get()]:>10,.{2}f} lbs."
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