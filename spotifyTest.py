import spotipy 

#needs to be authorized with a token before this will work

#Create spotify object
spotify = spotipy.Spotify()

searchterm = 'Hello'

result = spotify.search(q=searchterm)

print(result)

