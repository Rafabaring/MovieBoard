from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from create_user_app import create_user_api

app_name = 'create_user'

urlpatterns = [
    # /movie_board/
    # path('',            views.MusicView.as_view(), name = 'index'),
    path('create_user_api/', create_user_api.UserList.as_view(), name = 'create_user'), # call the API
    # path('create_user_api/api/', movie_list_api.MovieBoardList.as_view(), name = 'movie_board'), # call the API
    # path('add_album/',  views.MusicView.as_view(), name = 'add_album'),
    # path('add_album/',  views.add_album, name = 'add_album'),
]
