import os
import spotipy
from spotipy import SpotifyOAuth

from .serializer import *

os.environ['SPOTIPY_CLIENT_ID'] = "e669ed62315040a09ffdb89afa0cf649"
os.environ['SPOTIPY_CLIENT_SECRET'] = "4283d027252045ec8ec81bc2d796349a"
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://example.com/'

scope = "user-library-read user-library-modify playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def synchroniseSpotifyUserPlaylists(u_id):
    # when running playlist subpage, every time synchronise all playlist form spotify to our database
    # DB -> Spotify
    # delete playlists removed in spotify
    user = User.objects.get(pk=u_id)
    spotify_playlists = sp.current_user_playlists(limit=30)
    spotify = []
    user_id = sp.current_user()['id']
    for playlist in spotify_playlists["items"]:
        if playlist["owner"]['id'] == user_id:
            spotify.append(playlist)
    database = PlaylistSerializer(Playlist.objects.filter(user=user).all(), many=True).data

    for playlist in database:
        for spoti in spotify:
            if spoti['id'] == playlist['spotify_id']:
                break
        pl_id = playlist['id']
        pl = Playlist.objects.get(pk=pl_id)
        pl.delete()
    # add/ playlist form spotify + synchronise
    for spoti in spotify:
        for playlist in database:
            if spoti['id'] == playlist['spotify_id']:
                if spoti['description'] != playlist['description'] or spoti['name'] != playlist['name']:
                    playlistData = playlist
                    playlistData['name'] = spoti['name']
                    playlistData['description'] = spoti['description']
                    PlaylistSerializer(Playlist.objects.get(pk=playlistData['id']), data=playlistData).save()
                    break
        data = {'user': user,
        'name': spoti['name'],
        'rating_sum': 0,
        'rating_number': 0,
        'spotify_id': spoti['id'],
        'description': spoti['description']}
        PlaylistSerializer(data=data).save()


