import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from spotipy.oauth2 import SpotifyOAuth
import spotipy


class Spotify:
    def __init__(self):
        self._auth = HTTPBasicAuth("e669ed62315040a09ffdb89afa0cf649", "4283d027252045ec8ec81bc2d796349a")
        # do something with credentials
        client = BackendApplicationClient(client_id="e669ed62315040a09ffdb89afa0cf649")
        self._oauth = OAuth2Session(client=client)
        self.url = "127.0.0.1:8000"
        self.scopes = "playlist-modify-private user-library-modify"
        self._limit = 10  # changeable limit
        self._market = "US"  # changeable market

    def _refresh_token(self):
        self._token_data = self._oauth.fetch_token(token_url='https://accounts.spotify.com/api/token', auth=self._auth)
        self._access_token = self._token_data["access_token"]

    def get_album_name(self, search_words):
        self._refresh_token()
        response_albums = requests.get(
            f'https://api.spotify.com/v1/search?q={search_words}&type=album&limit={self._limit}',
            headers={'Authorization': f'Bearer {self._access_token}'})

        if response_albums.status_code == 200:
            # albums_data is dictionary where keys are albums' names and values are lists fo albums' songs
            # we might add album cover photo to this dictionary
            albums_data = {album['name']: None for album in response_albums.json()['albums']['items']}
            albums_ids = [album['id'] for album in response_albums.json()['albums']['items']]

            for alb_id, alb_name in zip(albums_ids, albums_data.keys()):
                response_songs_in_album = requests.get(f'https://api.spotify.com/v1/albums/{alb_id}',  # it is possible to add market here too
                                                        headers={'Authorization': f'Bearer {self._access_token}'})

                if response_songs_in_album.status_code == 200:
                    album_songs_names = [song['name'] for song in response_songs_in_album.json()['tracks']['items']]
                    albums_data[alb_name] = album_songs_names
            return albums_data

        else:
            return 404  # what do we do if we get an error

    def get_artist_name(self, search_words):
        self._refresh_token()
        response_artists = requests.get(
            f'https://api.spotify.com/v1/search?q={search_words}&type=artist&limit={self._limit}',
            headers={'Authorization': f'Bearer {self._access_token}'})

        if response_artists.status_code == 200:
            # artists_data is dictionary where keys are artists' names and values are their the most popular songs
            # we might add artist photo to this dictionary
            artists_data = {artist['name']: None for artist in response_artists.json()['artists']['items']}
            artists_ids = [artist['id'] for artist in response_artists.json()['artists']['items']]

            for art_id, art_name in zip(artists_ids, artists_data.keys()):
                response_top_artist_songs = requests.get(f'https://api.spotify.com/v1/artists/{art_id}/top-tracks?market={self._market}', # Are we changing the market we are searching in?
                                                         headers={'Authorization': f'Bearer {self._access_token}'})

                if response_top_artist_songs.status_code == 200:
                    artists_top_songs = [song['name'] for song in response_top_artist_songs.json()['tracks']]
                    artists_data[art_name] = artists_top_songs
            return artists_data

        else:
            return 404  # what do we do if we get an error

    def userAuthentication(self,scope):
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        results = sp.current_user_saved_tracks()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])