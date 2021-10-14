from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .genius_api import Genius
from .spotify_api import Spotify

genius_obj = Genius()
spotify_obj = Spotify()


def search(request):
    pass


def search_result(request, query):
    data_genius = genius_obj.getData(query)
    data_spotify = []
    delete = []
    results = {'results': []}

    for data1 in data_genius:
        song = spotify_obj.get_song_id(data1[1]['title'])
        if song == {}:
            delete.append(data1)
        else:
            data_spotify.append(song)

    for del_item in delete:
        data_genius.remove(del_item)

    for spoti, gen in zip(data_spotify, data_genius):
        results['results'].append({**spoti, **gen[0], **gen[1]})
    return JsonResponse(results)
