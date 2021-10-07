import os


def addArt(mp3Path, artPath):
    # Adds the image at artPath to the audio file at mp3Path using id3v2
    outputNameList = mp3Path.split(".")
    outputNameList[-2] = outputNameList[-2]+"_temp"
    outputName = ""
    for item in outputNameList:
        outputName = outputName + item + "."

    outputName = outputName[:len(outputName)-1]
    if os.path.isfile(outputName):
        os.remove(outputName)
    os.system(
        f"ffmpeg -i \"{mp3Path}\" -i \"{artPath}\" -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title=\"Album cover\" -metadata:s:v comment=\"Cover(front)\" \"{outputName}\""
    )
    if os.path.isfile(outputName):
        os.remove(mp3Path)
    os.rename(outputName, mp3Path)
