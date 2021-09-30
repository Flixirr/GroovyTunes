from django.shortcuts import render
from django.http import HttpResponse
from .genius_api import Genius

genius_obj = Genius()
# Create your views here.
def search(request):
    return HttpResponse("<html><body>Search main page</body></html>")

def search_result(request, query):
    data = genius_obj.getData(query)
    return HttpResponse(data)
