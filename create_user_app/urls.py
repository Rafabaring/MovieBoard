from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from create_user_app import create_user_api
from create_user_app import views

app_name = 'create_user'

urlpatterns = [
    # /movie_board/
    path('create_user/', views.CreateUser.as_view(), name = 'create_user'),
    path('create_user_api/', create_user_api.UserList.as_view(), name = 'create_user_api'),

    # Create movies
    path('create_movie/', views.CreateMovie.as_view(), name = 'create_movie'),
]
