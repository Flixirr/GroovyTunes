
# functions for playlist creation
import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


os.environ['SPOTIPY_CLIENT_ID'] = "e669ed62315040a09ffdb89afa0cf649"
os.environ['SPOTIPY_CLIENT_SECRET'] = "4283d027252045ec8ec81bc2d796349a"
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://example.com/'
def createNewPlaylist(name):
    # adding to database and by request to spotify
    pass

def changePlalistData():
    # change data in database and request to spotify
    pass

def confirmAction():
    # assuring user is sure to perform this irreversable action
    pass

def deletePlaylist():
    # delete playlist in database and by spotify request
    if confirmAction():
        pass

def userAuthentication(scope):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

#scopes = "playlist-modify-private user-library-modify"
scopes = "user-library-read"

userAuthentication(scopes)

