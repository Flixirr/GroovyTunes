from django.shortcuts import render
from django.http import HttpResponse
from .genius_api import Genius
from .models import *
from .serializer import *
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

genius_obj = Genius()
# Create your views here.
def search(request):
    return HttpResponse("<html><body>Search main page</body></html>")

def search_result(request, query):
    data = genius_obj.getData(query)
    return HttpResponse(data)


@api_view(['GET', 'POST', 'DELETE'])
def playlist_list(request):
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        playlist_serializer = PlaylistSerializer(playlists, many=True)
        return JsonResponse(playlist_serializer.data, safe=False)
 
    elif request.method == 'POST':
        playlist_data = JSONParser().parse(request)
        playlist_serializer = PlaylistSerializer(data=playlist_data)
        if playlist_serializer.is_valid():
            playlist_serializer.save()
            return JsonResponse(playlist_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Playlist.objects.all().delete()
        return JsonResponse({'message': '{} Playlists were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def playlist_details(request, id):
    try: 
        playlist = Playlist.objects.get(pk=id) 
    except Playlist.DoesNotExist: 
        return JsonResponse({'message': 'The playlist does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        playlist_serializer = PlaylistSerializer(playlist) 
        return JsonResponse(playlist_serializer.data) 
 
    elif request.method == 'PUT': 
        playlistData = JSONParser().parse(request) 
        playlist_serializer = PlaylistSerializer(playlist, data=playlistData) 
        if playlist_serializer.is_valid(): 
            playlist_serializer.save() 
            return JsonResponse(playlist_serializer.data) 
        return JsonResponse(playlist_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
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