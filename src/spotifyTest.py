import spotipy 
import sys
from spotipy.oauth2 import SpotifyClientCredentials
import json

credentials = SpotifyClientCredentials(
    client_id='90d2a3cd7ee04a97ac686fd3ffcf13f6',
    client_secret='dbcbbdfcc8004d218e0cdc42e80cbdf3')

#Create spotify object
token = credentials.get_access_token()

sp = spotipy.Spotify(auth=token)

searchterm = 'Hello'

result = sp.search(q=searchterm, limit=1)

#result2 = json.load(result)

print(result)

#print(result2.get("popularity"))
#print(result.get("items"))


