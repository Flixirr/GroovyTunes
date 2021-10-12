# functions for playlist creation
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
#from backend.users.models import Playlist
os.environ['SPOTIPY_CLIENT_ID'] = "e669ed62315040a09ffdb89afa0cf649"
os.environ['SPOTIPY_CLIENT_SECRET'] = "4283d027252045ec8ec81bc2d796349a"
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://example.com/'


class PlaylistMeneger:
    def __init__(self, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    def createNewPlaylist(self, name, description):
        # spotify
        user_id = self.sp.current_user()['id']
        self.sp.user_playlist_create(user=user_id, name=name, public=True, collaborative=False, description=description)
        our_playlist = self.sp.user_playlists(user_id,
                                              1)  # takes info about newest created playlist, so just created one
        spotify_playlist_id = our_playlist['items'][0]['id']
        print(spotify_playlist_id)
        # database not working while importing models
        #p = Playlist(user=user_id, name=name, description=description, spotify_id=spotify_playlist_id)
        #p.save()

    def changePlaylistData(self, playlist_id, name=None, description=None):
        # if we give empty brackets, if we fill data about playlist for customer when he opens change panel
        # spotify and database
        if name == None and description == None:
            pass
        elif name == None and description != None:
            self.sp.playlist_change_details(playlist_id=playlist_id, description=description)
        elif name != None and description == None:
            self.sp.playlist_change_details(playlist_id=playlist_id, name=name)
        elif name != None and description != None:
            self.sp.playlist_change_details(playlist_id=playlist_id, name=name, description=description)

    def deletePlaylist(self, playlist_id):
        # spotify
        self.sp.current_user_unfollow_playlist(playlist_id)
        # database
        pass

    def getSpotifyUserPlaylists(self):
        # when running page, every time update all playlist form spotify to our database
        spotify_playlists = self.sp.current_user_playlists(limit=20)
        user_id = self.sp.current_user()['id']
        own_playlist = []
        for playlist in spotify_playlists["items"]:
            if playlist["owner"]['id'] == user_id:
                own_playlist.append(playlist)
        print(own_playlist)


scopes = "user-library-read user-library-modify playlist-modify-public"
#PlaylistMeneger(scopes).createNewPlaylist('Nowa plejka2', "***** pis i konfederacje")
#PlaylistMeneger(scopes).changePlaylistData(playlist_id="7fc1H5jwSd1AldJIfP6qtd", description="jednak pis i konfe")
#PlaylistMeneger(scopes).deletePlaylist(playlist_id='4giBrWulaNhEsxjPcC7U6R')
PlaylistMeneger(scopes).getSpotifyUserPlaylists()
