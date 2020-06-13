from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from create_user_app import create_user_api
from create_user_app import views

app_name = 'create_user'

urlpatterns = [
    # /movie_board/
    # Create movies
    path('create_movie/', views.CreateMovie.as_view(), name = 'create_movie'),

    # Registration
    path('register/', views.register, name = 'register')
]
