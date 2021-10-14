from django.shortcuts import render
from django.http import HttpResponse
from .genius_api import Genius
import json
from .playlistf import PlaylistManager
genius_obj = Genius()
# Create your views here.
def search(request):
    return HttpResponse("<html><body>Search main page</body></html>")

def search_result(request, query):
    data = genius_obj.getData(query)
    return HttpResponse(data)

def create_playlist(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)  # request.raw_post_data w/ Django < 1.4
        try:
            name = json_data['name']
            description = json_data['description']
        except KeyError:
            HttpResponse("Malformed data!")
        return HttpResponse(PlaylistManager.createNewPlaylist(name,description))