# functions for playlist creation
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

os.environ['SPOTIPY_CLIENT_ID'] = "e669ed62315040a09ffdb89afa0cf649"
os.environ['SPOTIPY_CLIENT_SECRET'] = "4283d027252045ec8ec81bc2d796349a"
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://example.com/'


class PlaylistManager:
    def __init__(self, scope="user-library-read user-library-modify playlist-modify-public"):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def createNewPlaylist(self, data):
        # spotify
        name = data['name']
        description = data['description']
        user_id = self.sp.current_user()['id']
        self.sp.user_playlist_create(user=user_id, name=name, public=True, collaborative=False, description=description)
        our_playlist = self.sp.user_playlists(user_id,
                                              1)  # takes info about newest created playlist, so just created one
        spotify_playlist_id = our_playlist['items'][0]['id']
        return spotify_playlist_id

    def changePlaylistData(self, playlist_id, name=None, description=None):
        if name == None or description == None:
            return "Name or description are not valid or not given"
        # spotify and database
        self.sp.playlist_change_details(playlist_id=playlist_id, name=name, description=description)

    def deletePlaylist(self, playlist_id):
        # spotify # possible to add image later with 1 function playlist_cover_image
        self.sp.current_user_unfollow_playlist(playlist_id)
        # database

    def addToPlaylist(self,playlist, song_id):
        # spotify
        playlist_id= playlist['spotify_id']
        self.sp.playlist_add_items(playlist_id=playlist_id, items=[song_id])
        # no implementation for database

    def removeFormPlyalist(self, playlist, song_id):
        # spotify
        playlist_id = playlist['spotify_id']
        self.sp.playlist_remove_all_occurrences_of_items(playlist_id=playlist_id, items=[song_id])
        # no implementation for database

#PlaylistManager(scopes).createNewPlaylist(user= GroovyUser,name='Nowa plejka2', description="***** pis i konfederacje")
#PlaylistManager(scopes).changePlaylistData(playlist_id="7fc1H5jwSd1AldJIfP6qtd", description="jednak pis i konfe")
#PlaylistManager(scopes).deletePlaylist(playlist_id='1aazvT5Hpruab2ui7DkxPA')
#PlaylistManager(scopes).getSpotifyUserPlaylists()
