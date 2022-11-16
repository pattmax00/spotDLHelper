import os

def __spotdlHelper():
    path = "/path/to/your/music/folder"
    format = "mp3"
    config = '--path-template "' + path + '/{artist}/{album}/{title} - {artist}.{ext}" --output-format ' + format

    cmd = 'spotdl'

    spotify = [
        'https://open.spotify.com/artist/exampleurl',
        'https://open.spotify.com/artist/exampleurl',
    ]

    if not spotify:
        print('The spotify array is empty! Edit spotDLHelper.py and add your urls.')

    for url in spotify:
        os.system(cmd + " " + url + " " + config)

if __name__ == "__main__":
    __spotdlHelper()
    