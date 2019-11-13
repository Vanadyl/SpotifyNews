#Spotify Search File

#import Modules

import spotipy 

#needs to be authorized with a token before this will work

#Create spotify object
spotify = spotipy.Spotify()

def GetSong :(searchterm)
    result = spotify.search(q=searchterm)

    return result