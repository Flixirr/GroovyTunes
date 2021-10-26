from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .genius_api import Genius
from .playlistf import *
from .serializer import *
from .spotify_api import Spotify

genius_obj = Genius()
spotify_obj = Spotify()


def search(request):
    pass


def search_result(request, query):
    data = genius_obj.getData(query)
    return JsonResponse(data)



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

@api_view(['GET', 'POST', 'DELETE'])
def comment_list(request):
    if request.method == 'GET':
        comment = Comment.objects.all()
        comment_serializer = CommentSerializer(comment, many=True)
        return JsonResponse(comment_serializer.data, safe=False)
 
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Comment.objects.all().delete()
        return JsonResponse({'message': '{} Comments were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_details(request, id):
    try: 
        comment = Comment.objects.get(pk=id) 
    except Comment.DoesNotExist: 
        return JsonResponse({'message': 'The Comment does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        comment_serializer = CommentSerializer(comment) 
        return JsonResponse(comment_serializer.data) 
 
    elif request.method == 'PUT': 
        commentData = JSONParser().parse(request) 
        comment_serializer = CommentSerializer(comment, data=commentData) 
        if comment_serializer.is_valid(): 
            comment_serializer.save() 
            return JsonResponse(comment_serializer.data) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        comment.delete() 
        return JsonResponse({'message': 'Comment was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'DELETE'])
def playlist_comments(request, p_id):
    if request.method == 'GET': 
        try:
            playlist = Playlist.objects.get(pk=p_id)
            comment = Comment.objects.filter(playlist=playlist).all()
            comment_serializer = CommentSerializer(comment, many=True)
            return JsonResponse(data=comment_serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'message': 'The Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE': 
        try:
            playlist = Playlist.objects.get(pk=p_id)
            count = Comment.objects.filter(playlist=playlist).all().delete()

            return JsonResponse({'message': '{} Comments were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'message': 'The Comment does not exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def rate_playlist(request):
    if request.method == 'POST': 
        rating_data = JSONParser().parse(request)
        rating_serializer = RatingSerializer(data=rating_data)
        user_id = rating_data['user']
        playlist_id = rating_data['playlist']
        try: 
            u_id = rating_data['user']
            p_id = rating_data['playlist']
            old_rating = Rated.objects.filter(user_id = u_id, playlist_id = p_id).get()
            rating_id = old_rating.id
            
            rating = Rated.objects.get(pk=rating_id)
            rating_serializer = RatingSerializer(rating, data=rating_data)
            if rating_serializer.is_valid(): 
                rating_serializer.save() 

                playlist = Playlist.objects.get(pk=p_id)
                new_rating = playlist.rating_sum - old_rating.rating + rating.rating
                print('new_rating' + str(new_rating))
                print('old_rating' + str(old_rating.rating))
                print('rating' + str(rating.rating))
                playlist.rating_sum = new_rating
                playlist.save()

                return JsonResponse(rating_serializer.data) 
            else :
                return JsonResponse(rating_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Rated.DoesNotExist as e: 
            rating_serializer = RatingSerializer(data=rating_data)
            if rating_serializer.is_valid():
                rating_serializer.save()

                p_id = rating_data['playlist']
                playlist = Playlist.objects.get(pk=p_id)
                playlist.rating_sum = playlist.rating_sum + rating_data['rating']
                playlist.rating_number = playlist.rating_number + 1
                playlist.save()

                return JsonResponse(rating_serializer.data, status=status.HTTP_201_CREATED) 
            return JsonResponse(rating_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)

@api_view(['GET'])
def playlist_rating(request, p_id, u_id):
    if request.method == 'GET': 
        try: 
            rating = Rated.objects.get(user = u_id, playlist = p_id) 
            rating_serializer = RatingSerializer(rating)
            return JsonResponse(rating_serializer.data, safe=False) 
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The Rating does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def user_playlists(request, u_id):
    if request.method == 'GET': 
        try:
            user = User.objects.get(pk=u_id)
            playlists = Playlist.objects.filter(user=user).all()
            playlist_serializer = PlaylistSerializer(playlists, many=True)
            return JsonResponse(data=playlist_serializer.data, safe=False)
        except Exception as e:
            return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)
     
    
 
