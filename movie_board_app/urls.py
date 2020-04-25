from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from movie_board_app import movie_list_api # importing API
from movie_board_app import views # importing views

app_name = 'movie_board'

urlpatterns = [
    # /movie_board/
    path('',                    views.MovieBoardView.as_view(), name = 'home'),
    path('get_movie_list_api/', movie_list_api.MovieBoardList.as_view(), name = 'movie_board'), # call the API

    # UpVote
    path('upvote_movie/',     views.UpVoteView.as_view(), name = 'upvote_movie'), # call the API
    path('upvote_movie_api/', movie_list_api.UpVoteMovie.as_view(), name = 'upvote_movie'), # call the API
]
