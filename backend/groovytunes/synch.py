import spotipy
from spotipy import SpotifyOAuth
import os

os.environ['SPOTIPY_CLIENT_ID'] = "e669ed62315040a09ffdb89afa0cf649"
os.environ['SPOTIPY_CLIENT_SECRET'] = "4283d027252045ec8ec81bc2d796349a"
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://example.com/'

scope= "user-library-read user-library-modify playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def synchroniseSpotifyUserPlaylists():
    # when running playlist subpage, every time synchronise all playlist form spotify to our database
    # DB -> Spotify
    # get playlists as variable database
    spotify_playlists = sp.current_user_playlists(limit=30)
    own_playlist = []
    user_id = sp.current_user()['id']
    for playlist in spotify_playlists["items"]:
        if playlist["owner"]['id'] == user_id:
            own_playlist.append(playlist)
    database = []  # taken with get view
    # also for delete and changes done on spotify