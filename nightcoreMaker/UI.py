# UI based app
# Effectively mimics the doubletime/nightcore mod from osu!
# Uses ffmpeg to speed up (or slow down) audio files.
# Pitch and speed are handled independently.

import tkinter as tk
from tkinter.constants import HORIZONTAL
import tkinter.filedialog as fd
import os
from createNightcore import createNightcore
dirPath = os.path.dirname(os.path.realpath(__file__))
root = tk.Tk()
root.title("Nightcore Creator")
root.geometry("600x300")
root.grid_columnconfigure(0, weight=2)
for i in range(6):
    root.grid_rowconfigure(i, weight=2)


root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(4, weight=1)


musicPath = ""
musicPathVar = tk.StringVar(value=musicPath)


def openFile():
    global musicPath
    musicPath = fd.askopenfilename()
    musicPathVar.set(musicPath)


openButton = tk.Button(root, text="Open File", command=openFile)
openButton.grid(row=0, column=0)
fileLabel = tk.Label(textvariable=musicPathVar)
fileLabel.grid(row=1)
speedLabel = tk.Label(root, text="Speed increase (multiplier)")
speedSlider = tk.Scale(root, from_=0.1, to=2,
                       orient=tk.HORIZONTAL, resolution=0.1)

pitchLabel = tk.Label(root, text="Pitch increase (multiplier)")
pitchSlider = tk.Scale(root, from_=0.1, to=2,
                       orient=tk.HORIZONTAL, resolution=0.1)
speedSlider.set(1)
pitchSlider.set(1)
speedLabel.grid(row=2, sticky=tk.S)
speedSlider.grid(row=3, column=0, sticky=tk.N)
pitchLabel.grid(row=4, sticky=tk.S)
pitchSlider.grid(row=5, column=0, sticky=tk.N)

openButton = tk.Button(root, text="Go", command=lambda: createNightcore(
    musicPath, speedSlider.get(), pitchSlider.get()))
openButton.grid(row=6, column=0)
root.mainloop()
