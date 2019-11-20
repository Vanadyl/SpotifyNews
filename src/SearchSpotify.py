# Spotify Search File

# import Modules

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 

####### Auth Code ########

#credendials for spotify api dev account
credentials = SpotifyClientCredentials(
    client_id='90d2a3cd7ee04a97ac686fd3ffcf13f6',
    client_secret='dbcbbdfcc8004d218e0cdc42e80cbdf3')


# get token
token = credentials.get_access_token()

# Create spotify object
sp = spotipy.Spotify(auth=token)

def getSong(searchterm):
    '''
    parameters: searchterm
    type: string
    description: returns a dict format of a song from spotify
    '''
    # search spotify api for song
    result = sp.search(q=searchterm, limit=1)
    # reformat data
    # Creat dict to store data we want
    # dict stores song name, artist name & a song preview url
    if result == None:
        return 'None'
    else:
        try:
            result = result['tracks']['items'][0]
            songResult = {
            "name":result['name'],
            "artist":result['artists'][0]['name'],
            "url":result['preview_url']
            }
            # return the dict
            return songResult
        except:
            return 'Error'