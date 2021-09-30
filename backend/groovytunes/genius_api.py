import json

import requests


class Genius:
    def __init__(self):
        self._access_token = 'Im7jkUne-i6Tw5IU2gkaEN6vunZGRH-6eOF7X6_wsb4iaOeWq5KB5eTk_fTkWhfc'

    def getIdsFromSong(self, search_words):
        r = requests.get(f'https://api.genius.com/search?q={search_words}',
                         headers={'Authorization': f'Bearer {self._access_token}'})

        if r.status_code == 200:
            rj = r.json()
            max = len(rj["response"]['hits'])
            if max > 5:
                max = 5
            return [(rj["response"]['hits'][q]['result']['primary_artist']['id'],
                     rj["response"]['hits'][q]['result']['id'])
            for q in range(max)]
            pass  # return some kind of error

    def getArtistData(self,words):
        artistData = []
        IDs = self.getIdsFromSong(words)
        for artist in IDs:
            r = requests.get(f'https://api.genius.com/artists/{artist[0]}',
                         headers={'Authorization': f'Bearer {self._access_token}'})
            if r.status_code == 200:
                artistData.append((r.json()['response']['artist']['name'],r.json()['response']['artist']['url']))
            else:
                pass # return some kind of error
        return artistData

    def getSongData(self,words):
        IDs = self.getIdsFromSong(words)
        songData = []
        for song in IDs:
            r = requests.get(f'https://api.genius.com/songs/{song[1]}',
                             headers={'Authorization': f'Bearer {self._access_token}'})
            if r.status_code == 200:
                onesongData = [r.json()['response']['song']['title'],r.json()['response']['song']['url'],
                               r.json()['response']['song']['release_date']]
                artlist = []
                for artist in r.json()['response']['song']['featured_artists']:
                    artlist.append((artist['name'],artist['url']))
                onesongData.append(artlist)
                prodlist = []
                for producer in r.json()['response']['song']['producer_artists']:
                    prodlist.append((producer['name'],producer['url']))
                onesongData.append(prodlist)
                songData.append(onesongData)
            else:
                pass  # return some kind of error
        return songData

    def getData(self,words):
        resaults = []
        nrOfResaults = len(self.getIdsFromSong(words))
        artists = self.getArtistData(words)
        songs = self.getSongData(words)
        for final in range(nrOfResaults):
            resaults.append((artists[final],songs[final]))
        return json.dumps(resaults)
