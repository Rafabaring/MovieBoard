from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

import requests

# to work with HTML template
from django.template import loader

# Importing rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from create_user_app.create_user_api import UserList,GenreList
from movie_board_app.views import MovieBoardView

# ThirdParty Scoring
from movie_board_app.movie_list_api import ThirdPartyRatings


class CreateUser(APIView):

    def get(self, request):
        all_genre = GenreList.get_genre_list()

        template = loader.get_template('create_user_app/create_user.html')
        genre_context = {
            "genre_list": all_genre
        }

        # return render(request, 'create_user_app/create_user.html')
        return HttpResponse(template.render(genre_context, request))


    def post(self, request):
        data =  {
        "first_name": request.data['first_name'],
        "last_name":  request.data['last_name'],
        }

        # create_user_api.UserList
        URL = "http://localhost:8000/movie_board/create_user_api/"
        r = requests.post(url = URL, data = data)


        return render(request, 'create_user_app/create_user.html')

class CreateMovie(APIView):
    def post(self, request):

        # Getting the ID of the last user created
        # Hopefully is the one recently created
        last_created_id, last_created_first_name, last_created_last_name = UserList.get_last_created_id()

        create_movie_requested = request.data # json format

        # Adding the ThirdParty ratings
        third_party_score = ThirdPartyRatings.get_third_party_score(request.data['movie_title'])

        create_movie_data =  {
        "movie_title":            request.data['movie_title'],
        "youtube_trailer_link":   request.data['youtube_trailer_link'],
        "recommendee_first_name": request.data['recommendee_first_name'],
        "recommendee_last_name":  request.data['recommendee_last_name'],
        "vote_count":             0, # start with 0 votes
        "imdb_score":             third_party_score,
        "recommender":            last_created_id,
        "genre":                  request.data['genre']

        }


        URL = "http://127.0.0.1:8000/movie_board/movie_list_api/"
        r = requests.post(url = URL, data = create_movie_data)

        # After creating a movie, goes to the movieboard list / home
        return MovieBoardView().get(request)
