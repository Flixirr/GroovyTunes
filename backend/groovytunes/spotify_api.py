import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session


class Spotify:
    def __init__(self):
        self._auth = HTTPBasicAuth("e669ed62315040a09ffdb89afa0cf649", "4283d027252045ec8ec81bc2d796349a")
        # do something with credentials
        client = BackendApplicationClient(client_id="e669ed62315040a09ffdb89afa0cf649")
        self._oauth = OAuth2Session(client=client)
        self._limit = 1
        self._market = "US"

    def _refresh_token(self):
        self._token_data = self._oauth.fetch_token(token_url='https://accounts.spotify.com/api/token', auth=self._auth)
        self._access_token = self._token_data["access_token"]

    def get_song_id(self, search_words):
        self._refresh_token()
        res_songs = requests.get(
            f'https://api.spotify.com/v1/search?q={search_words}&type=track&limit={self._limit}',
            headers={'Authorization': f'Bearer {self._access_token}'})

        if res_songs.status_code == 200:
            if len(res_songs.json()['tracks']['items']):
                return {'id_spotify': res_songs.json()['tracks']['items'][0]['id'],
                        'sample': res_songs.json()['tracks']['items'][0]['preview_url']}
            else:
                return {}
        else:
            return {}
