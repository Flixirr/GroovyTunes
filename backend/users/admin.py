from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import GroovyUserChangeForm, GroovyUserCreationForm
from .models import GroovyUser

# Register your models here.
class GroovyUserAdmin(UserAdmin):
    add_form = GroovyUserCreationForm
    form = GroovyUserChangeForm
    model = GroovyUser
    list_display = ['email']

admin.site.register(GroovyUser, GroovyUserAdmin)
