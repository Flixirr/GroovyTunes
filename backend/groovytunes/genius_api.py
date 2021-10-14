import requests


class Genius:
    def __init__(self):
        self._access_token = 'Im7jkUne-i6Tw5IU2gkaEN6vunZGRH-6eOF7X6_wsb4iaOeWq5KB5eTk_fTkWhfc'
        self.search_list = []

    def get_search_response_list(self, search_words):
        res_search = requests.get(f'https://api.genius.com/search?q={search_words}',
                                  headers={'Authorization': f'Bearer {self._access_token}'})

        if res_search.status_code == 200:
            res_json = res_search.json()
            self.search_list = res_json['response']['hits']

    def getArtistData(self):
        artistData = []
        for single_search_data in self.search_list:
            artistData.append({'name': single_search_data['result']['primary_artist']['name'],
                               'url': single_search_data['result']['primary_artist']['url'],
                               'photo_artist': single_search_data['result']['primary_artist']['image_url']})  # are we adding more stuff here?
        return artistData

    def getSongData(self):
        songData = []
        for single_search_data in self.search_list:
            res_song = requests.get(f'https://api.genius.com/songs/{single_search_data["result"]["id"]}',
                                    headers={'Authorization': f'Bearer {self._access_token}'})  # this request is time consuming, we can try later on web scaper
            if res_song.status_code == 200:
                res_json = res_song.json()
                songData.append({'title': res_json['response']['song']['title'],
                                 'photo_song': res_json['response']['song']['song_art_image_thumbnail_url'],
                                 'lyrics': res_json['response']['song']['embed_content'],
                                 'release_date': res_json['response']['song']['release_date'],
                                 'album': res_json['response']['song']['album'],
                                 'featured_artists': res_json['response']['song']['featured_artists'],
                                 'producer_artists': [producer['name'] for producer in
                                                      res_json['response']['song']['producer_artists']]})
        return songData

    def getData(self, words):
        results = []
        self.get_search_response_list(words)
        nr_of_results = len(self.search_list)
        artists = self.getArtistData()
        songs = self.getSongData()
        for final in range(nr_of_results):
            results.append((artists[final], songs[final]))
        return results
