import addMetadata

audioFile = ""
coverArt = ""
title = ""
artist = ""
album = ""

if coverArt:
    addMetadata.addArt(audioFile, coverArt)

if title:
    addMetadata.addTitle(audioFile, title)

if artist:
    addMetadata.addArtist(audioFile, artist)

if album:
    addMetadata.addAlbum(audioFile, album)
