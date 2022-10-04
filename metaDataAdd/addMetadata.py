import skeleton


def addArtist(mp3Path, artist):
    skeleton.addMetadata(
        mp3Path, artist, "ffmpeg -i \"%s\" -map 0 -c copy -id3v2_version 3 -write_id3v2 1 -metadata \"artist=%s\" \"%s\""
    )


def addAlbum(mp3Path, album):
    skeleton.addMetadata(
        mp3Path, album, "ffmpeg -i \"%s\" -map 0 -c copy -id3v2_version 3 -write_id3v2 1 -metadata \"album=%s\" \"%s\""
    )


def addTitle(mp3Path, title):
    skeleton.addMetadata(
        mp3Path, title, "ffmpeg -i \"%s\" -map 0 -c copy -id3v2_version 3 -write_id3v2 1 -metadata \"title=%s\" \"%s\""
    )


def addArt(mp3Path, artPath):
    skeleton.addMetadata(
        mp3Path, artPath, "ffmpeg -i \"%s\" -i \"%s\" -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v title=\"Album cover\" -metadata:s:v comment=\"Cover(front)\" \"%s\""
    )

def addDiscNumber(mp3Path, cdNumber):
    skeleton.addMetadata(
        mp3Path, cdNumber, "ffmpeg -i \"%s\" -map 0 -c copy -id3v2_version 3 -write_id3v2 1 -metadata \"discNumber=%s\" \"%s\""
    )

def addAlbumArtist(mp3Path, artist):
    skeleton.addMetadata(
        mp3Path, artist, "ffmpeg -i \"%s\" -map 0 -c copy -id3v2_version 3 -write_id3v2 1 -metadata \"albumArtist=%s\" \"%s\""
    )