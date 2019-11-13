import spotipy 
import spotipy.util as util
import sys
from spotipy.oauth2 import SpotifyClientCredentials

#needs to be authorized with a token before this will work
'''
scope =''

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    #print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username,scope,client_id='90d2a3cd7ee04a97ac686fd3ffc',client_secret='dbcbbdfcc8004d218e0cdc42e80cbdf3',redirect_uri='http://localhost/')



client_credentials_manager = SpotifyClientCredentials(client_id='90d2a3cd7ee04a97ac686fd3ffc', client_secret='dbcbbdfcc8004d218e0cdc42e80cbdf3')
'''

credentials = SpotifyClientCredentials(
    client_id='90d2a3cd7ee04a97ac686fd3ffcf13f6',
    client_secret='dbcbbdfcc8004d218e0cdc42e80cbdf3')

#Create spotify object
token = credentials.get_access_token()

sp = spotipy.Spotify(auth=token)

searchterm = 'Disarray'

result = sp.search(q=searchterm)

print(result)

