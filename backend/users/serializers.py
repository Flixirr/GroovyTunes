from rest_framework.serializers import ModelSerializer

from .models import GroovyUser

class UserSerializer(ModelSerializer):
    class Meta:
        model = GroovyUser
        fields = ('email', 'username', 'profile_name', 'password')