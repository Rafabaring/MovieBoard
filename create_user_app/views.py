from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect

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

# Login and registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login



def index(request):
    return render(request, 'create_user_app/index.html')


def register(request):
    if request.method == 'POST':
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save() # save the new user to the database

             # authenticating the user
            username = registration_form.cleaned_data['username']
            password = registration_form.cleaned_data['password1'] # password1 is the first password field

            user = authenticate(username = username, password = password)
            # After authenticate, login the recently created user
            login(request, user)
            # Once loggedin, send to home page
            return MovieBoardView().get(request)
    else:
        registration_form = UserCreationForm()
    context = {
        'registration_form': registration_form
    }

    return render(request, 'registration/register.html', context)




class CreateMovie(APIView):
    def get(self, request):

        # If the user is authenticade, they can create a movie
        current_user = request.user
        if current_user.is_authenticated:
            all_genre = GenreList.get_genre_list()

            template = loader.get_template('create_user_app/create_movie.html')
            genre_context = {
                "genre_list": all_genre
            }

            # return render(request, 'create_user_app/create_user.html')
            return HttpResponse(template.render(genre_context, request))
        else:
            return register(request)


    def post(self, request):

        create_movie_requested = request.data # json format

        # Adding the ThirdParty ratings
        third_party_score = ThirdPartyRatings.get_third_party_score(request.data['movie_title'])

        # Getting the authenticated current user information
        # Will be used as recommender
        current_user = request.user
        if current_user.is_authenticated:
            print('user IS Autenticated')
            print(current_user)
        else:
            print('Usuario não autenticado')

        create_movie_data =  {
        "movie_title":            request.data['movie_title'],
        "youtube_trailer_link":   request.data['youtube_trailer_link'],
        "recommendee_first_name": request.data['recommendee_first_name'],
        "recommendee_last_name":  request.data['recommendee_last_name'],
        "vote_count":             0, # start with 0 votes
        "imdb_score":             third_party_score,
        "recommender":            current_user.id,
        "genre":                  request.data['genre']

        }


        URL = "http://127.0.0.1:8000/movie_board/movie_list_api/"
        r = requests.post(url = URL, data = create_movie_data)

        # After creating a movie, goes to the movieboard list / home
        return MovieBoardView().get(request)
