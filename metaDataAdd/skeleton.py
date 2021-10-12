import os


def getTempName(originalName):
    outputNameList = originalName.split(".")
    outputNameList[-2] = outputNameList[-2]+"_temp"
    outputName = ""
    for item in outputNameList:
        outputName = outputName + item + "."
    outputName = outputName[:len(outputName)-1]
    if os.path.isfile(outputName):
        os.remove(outputName)
    return outputName


def consolidateCopy(originalName, tempName):
    if os.path.isfile(tempName):
        os.remove(originalName)
        os.rename(tempName, originalName)


def addMetadata(mp3Path, metadata, command):
    # Adds metadata to the audio file at mp3Path using id3v2

    # ffpmeg can't edit the file it's working on, so we have to create a new file, delete the original and rename the new one
    outputName = getTempName(mp3Path)

    # The actual ffmpeg command
    # Limited to only 1 metadata input at a time, but I cba to dynamically assemble an ffmpeg command based on what inputs come in
    os.system(
        command % (mp3Path, metadata, outputName)
    )

    # Only delete the original if the modified version exists, in case the ffmpeg command failed
    consolidateCopy(mp3Path, outputName)
