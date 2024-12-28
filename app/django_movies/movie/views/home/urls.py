from django.urls import path

from .views import Home, Details, Search

app_name = 'movies'

urlpatterns = [
    path('', Home, name='Home'),
    path('Search', Search, name='Search'),
    path('Views/<int:movies_id>', Details, name='Details')
]

