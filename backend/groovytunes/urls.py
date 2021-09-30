from django.urls import include, path
from groovytunes import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/<str:query>/', views.search_result, name='search_result')
]
