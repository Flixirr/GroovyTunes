from rest_framework import serializers 
from .models import *
		 

class PlaylistSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Playlist
        fields = '__all__'