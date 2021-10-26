from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import GroovyUser


class GroovyUserCreationForm(UserCreationForm):
    class Meta:
        model = GroovyUser
        fields = ('email', )

class GroovyUserChangeForm(UserChangeForm):
    class Meta:
        model = GroovyUser
        fields = UserChangeForm.Meta.fields