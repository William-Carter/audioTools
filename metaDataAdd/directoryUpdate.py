import os
import addMetadata

# Step 1
# Build an index of all the songs
songsPath = "E:/Music/Horimiya OST"
songsList = []
for root, dirs, files in os.walk(songsPath):
    for file in files:
        if not file.split(".")[-1] in ["mp3","flac"]:
            songsList.append(file)

# Step 2
# Any intermediate steps where info is pulled from the files.
songsUpdated = songsList.copy()

# Step 3
# Iterate through and edit them all
for song in songsUpdated:

    file = songsPath+"/"+song
    #example:
    #addMetadata.addDate(file, "2021")