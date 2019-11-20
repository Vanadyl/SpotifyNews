#Spotify Search File

#import Modules

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 

#Auth Code

#credendials for spotify api dev account
credentials = SpotifyClientCredentials(
    client_id='90d2a3cd7ee04a97ac686fd3ffcf13f6',
    client_secret='dbcbbdfcc8004d218e0cdc42e80cbdf3')


#get token
token = credentials.get_access_token()

#Create spotify object
sp = spotipy.Spotify(auth=token)

def getSong :(searchterm)
    result = sp.search(q=searchterm, limit=1)

    return result