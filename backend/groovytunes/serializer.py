from rest_framework import serializers 
from .models import *
		 

class PlaylistSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Playlist
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Rated
        fields = '__all__'