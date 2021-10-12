from django.urls import include, path
import views #shouldnt be just |import views|?

urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/<str:query>/', views.search_result, name='search_result')
]
