from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .genius_api import Genius
from .models import *
from .serializer import *
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from .spotify_api import Spotify
from .playlistf import *
from .synch import synchroniseSpotifyUserPlaylists


genius_obj = Genius()
spotify_obj = Spotify()


def search(request):
    pass


def search_result(request, query):
    data = genius_obj.getData(query)
    return HttpResponse(data)



@api_view(['GET', 'POST', 'DELETE'])
def playlist_list(request):
    # gives you list of playlists, creates new ones or deletes some
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        playlist_serializer = PlaylistSerializer(playlists, many=True)
        return JsonResponse(playlist_serializer.data, safe=False)

    elif request.method == 'POST':
        playlist_data = JSONParser().parse(request)
        # create spotify playlist
        playlist_data['spotify_id'] = PlaylistManager().createNewPlaylist(data=playlist_data)
        playlist_serializer = PlaylistSerializer(data=playlist_data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return JsonResponse(playlist_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Playlist.objects.all().delete()
        return JsonResponse({'message': '{} Playlists were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def playlist_details(request, id):  # how to implement description in databases
    # info about certain playlist, change info in there or delete this playlist
    try:
        playlist = Playlist.objects.get(pk=id)
    except Playlist.DoesNotExist:
        return JsonResponse({'message': 'The playlist does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        playlist_serializer = PlaylistSerializer(playlist)
        return JsonResponse(playlist_serializer.data)

    elif request.method == 'PUT':
        playlistData = JSONParser().parse(request)
        # change data on spotify playlist
        spotify_id = playlistData['spotify_id']
        name = playlistData['name']
        description = playlistData['description']
        PlaylistManager().changePlaylistData(playlist_id=spotify_id, name=name, description=description)
        playlist_serializer = PlaylistSerializer(playlist, data=playlistData)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return JsonResponse(playlist_serializer.data)
        return JsonResponse(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # plus delete on spotify
        PlaylistManager().deletePlaylist(playlist.spotify_id)
        playlist.delete()
        return JsonResponse({'message': 'Playlist was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
 
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} Users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, id):
    try: 
        user = User.objects.get(pk=id) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        user_serializer = UserSerializer(user) 
        return JsonResponse(user_serializer.data) 
 
    elif request.method == 'PUT': 
        userData = JSONParser().parse(request) 
        user_serializer = UserSerializer(user, data=userData) 
        if user_serializer.is_valid(): 
            user_serializer.save() 
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        user.delete() 
        return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
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

@api_view(['GET', 'PUT', 'DELETE'])
def songs_menagment(request, pl_id, song_id=None):
    if request.method == 'GET':
        return PlaylistManager().listOfSongs(playlist=pl_id)
    if request.method == 'PUT':
        PlaylistManager().addToPlaylist(playlist=pl_id, song_id=song_id)
    if request.method == 'DELETE':
        PlaylistManager().removeFormPlyalist(playlist=pl_id, song_id=song_id)
