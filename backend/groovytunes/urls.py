from django.urls import include, path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/<str:query>/', views.search_result, name='search_result'),
    path('api/playlist_list', views.playlist_list, name='api/playlist_list'),
    path('api/playlist_details<int:id>', views.playlist_detail, name='api/playlist_details'),
]
