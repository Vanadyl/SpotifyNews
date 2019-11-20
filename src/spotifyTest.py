import spotipy 
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import json

credentials = SpotifyClientCredentials(
    client_id='90d2a3cd7ee04a97ac686fd3ffcf13f6',
    client_secret='dbcbbdfcc8004d218e0cdc42e80cbdf3')

# Create spotify object
token = credentials.get_access_token()

sp = spotipy.Spotify(auth=token)

searchterm = 'Hello'

result = sp.search(q=searchterm, limit=1)

result = result['tracks']['items']

songResult = {
        "name":result['name'],
        "artist":result['artists'][0]['name'],
        "url":result['preview_url']
    }

#result2 = json.dumps(result)

# print(result)

#print(songResult)