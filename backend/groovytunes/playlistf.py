# functions for playlist creation
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

os.environ['SPOTIPY_CLIENT_ID'] = "e669ed62315040a09ffdb89afa0cf649"
os.environ['SPOTIPY_CLIENT_SECRET'] = "4283d027252045ec8ec81bc2d796349a"
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://127.0.0.1:8000/'


class Playlist:
    def __init__(self, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        results = self.sp.current_user_saved_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])

    def createNewPlaylist(self, name):
        # adding to database and by request to spotify
        pass

    def changePlalistData(self):
        # change data in database and request to spotify
        pass

    def deletePlaylist(self):
        # delete playlist in database and by spotify request
        pass


scopes = "playlist-modify-private user-library-modify"
Playlist(scopes)
