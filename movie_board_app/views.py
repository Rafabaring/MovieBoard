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
        URL = "http://localhost:8000/movie_board/get_movie_list_api/"
        r = requests.get(url = URL)
        # extracting data in json format
        movie_list_data = r.json()

        template = loader.get_template('movie_board_app/home.html')

        # Criando dictionary. Normalmente se chama "context"
        # Essa será a informação que será enviada para o HTML
        context = {
            'movie_list_data': movie_list_data
        }
        # No Response, always pass the request
        return HttpResponse(template.render(context, request))

class UpVoteView(APIView):
    def post(self, request, movie_id):

        data =  {
        "movie_primary_key": movie_id
        }

        print("DATA")
        print(data)
        URL = "http://localhost:8000/movie_board/upvote_movie_api/"
        r = requests.post(url = URL, data = data)


        # Esse é o mesmo código que o get acima. Descobrir como fazer uma versão melhor
        URL = "http://localhost:8000/movie_board/get_movie_list_api/"
        r = requests.get(url = URL)
        # extracting data in json format
        movie_list_data = r.json()

        template = loader.get_template('movie_board_app/home.html')

        # Criando dictionary. Normalmente se chama "context"
        # Essa será a informação que será enviada para o HTML
        context = {
            'movie_list_data': movie_list_data
        }

        return HttpResponse(template.render(context, request))
        # return render(request, 'movie_board_app/up_vote.html')
