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




class MovieBoardView(APIView):

    def get(self, request):
        URL = "http://localhost:8000/movie_list_api/"
        r = requests.get(url = URL)

        # extracting data in json format
        movie_list_data = r.json()
        template = loader.get_template('movie_board_app/home.html')

        context = {
            'movie_list_data': movie_list_data
        }
        # No Response, always pass the request
        return HttpResponse(template.render(context, request))

class UpVoteView(APIView):
    # update ou patch
    def post(self, request, movie_id):

        data =  {
        "movie_primary_key": movie_id
        }

        URL = "http://localhost:8000/upvote_movie_api/"
        r = requests.post(url = URL, data = data)

        return MovieBoardView().get(request)
