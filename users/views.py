from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from . serializer import *


# fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class UserView(APIView):

    def get(self, request):
        output = [{"username": output.username,
                   "first_name": output.first_name,
                   "last_name": output.last_name,
                   "email": output.email,
                   "password": output.password}
                  for output in User.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

# Create your views here.
def base(request):
    return render(request, 'users/base.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Your are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
