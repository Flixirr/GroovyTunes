from django.urls import include, path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/<str:query>/', views.search_result, name='search_result'),
    path('api/playlist', views.playlist_list, name='api/playlist_list'),
    path('api/playlist/<int:id>', views.playlist_details, name='api/playlist_details'),
    path('api/playlist/<int:id>/songs', views.songs_menagment, name ='api/playlist_content')
]
