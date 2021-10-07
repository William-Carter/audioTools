def createNightcore(inputFilePath, speed, pitchup):
    """Takes the input file path, and creates the adjusted file next to it based on the speed and pitchup values."""
    outputNameList = inputFilePath.split(".")
    outputNameList[-2] = outputNameList[-2]+"_ADJ"
    outputName = ""
    for item in outputNameList:
        outputName = outputName + item + "."

    outputName = outputName[:-1]
    f = mutagen.File(inputFilePath)
    samplerate = f.info.sample_rate
    tempoMult = speed/pitchup
    if os.path.isfile(outputName):
        os.remove(outputName)
    os.system(
        f"ffmpeg -i \"{inputFilePath}\" -af \"atempo={tempoMult}, asetrate={samplerate}*{pitchup}\" -ar {samplerate} \"{outputName}\"")