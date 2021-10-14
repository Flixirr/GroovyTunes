# functions for playlist creation
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from django.apps import apps
os.environ['SPOTIPY_CLIENT_ID'] = "e669ed62315040a09ffdb89afa0cf649"
os.environ['SPOTIPY_CLIENT_SECRET'] = "4283d027252045ec8ec81bc2d796349a"
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://example.com/'


class PlaylistManager:
    def __init__(self, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    def createNewPlaylist(self,user, name, description):
        # spotify
        user_id = self.sp.current_user()['id']
        self.sp.user_playlist_create(user=user_id, name=name, public=True, collaborative=False, description=description)
        our_playlist = self.sp.user_playlists(user_id,
                                              1)  # takes info about newest created playlist, so just created one
        spotify_playlist_id = our_playlist['items'][0]['id']
        # database not working while importing models
        # user needed form Hendrik GroovyUser
        #p = apps.get_model('users','Playlist')
        return "Sucessfuly created playlist"
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
        # spotify # possible to add image later with 1 function playlist_cover_image
        self.sp.current_user_unfollow_playlist(playlist_id)
        # database
        #p = Playlist
        pass

    def getSpotifyUserPlaylists(self):
        # when running page, every time update all playlist form spotify to our database
        spotify_playlists = self.sp.current_user_playlists(limit=20)
        user_id = self.sp.current_user()['id']
        own_playlist = []
        for playlist in spotify_playlists["items"]:
            if playlist["owner"]['id'] == user_id:
                own_playlist.append(playlist)
        return own_playlist

    def addToPlaylist(self,playlist_id, song_id):
        # spotify
        self.sp.playlist_add_items(playlist_id=playlist_id, items=[song_id])
        # database

    def removeFormPlyalist(self, playlist_id, song_id):
        # spotify
        self.sp.playlist_remove_all_occurrences_of_items(playlist_id=playlist_id, items=[song_id])
        # database

scopes = "user-library-read user-library-modify playlist-modify-public"
#PlaylistManager(scopes).createNewPlaylist(user= GroovyUser,name='Nowa plejka2', description="***** pis i konfederacje")
#PlaylistManager(scopes).changePlaylistData(playlist_id="7fc1H5jwSd1AldJIfP6qtd", description="jednak pis i konfe")
#PlaylistManager(scopes).deletePlaylist(playlist_id='1aazvT5Hpruab2ui7DkxPA')
#PlaylistManager(scopes).getSpotifyUserPlaylists()
