# Importing rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

import requests

#Third party score key
from MovieBoard.third_party_score_key import get_omdb_api_key

# Importing models
from movie_board_app.models import Genre, Movie

# Importing serializer
from movie_board_app.serializers import MovieBoardSerializer, UpVoteMovieSerializer

# List all stocks or create a new one
class MovieBoardList(APIView):

    def get(self, request):
        all_movies = Movie.objects.all()
        movies_serializer = MovieBoardSerializer(all_movies, many = True)

        return Response(movies_serializer.data)


    def post(self, request):
        movies_serializer = MovieBoardSerializer(data = request.data)


        if movies_serializer.is_valid():

            movies_serializer.save()
            return Response(movies_serializer.data)


        else:
            return Response(
                    movies_serializer.errors,
                    status = status.HTTP_400_BAD_REQUEST
                )



class UpVoteMovie(APIView):

    def post(self, request):
        upvote_serializer = UpVoteMovieSerializer(data = request.data)
        print("UPVOTE SERIALIZER")
        print(upvote_serializer)
        print('----')
        print(request.data)
        print(request.data['movie_primary_key'])
        movie_id_to_upvote = request.data['movie_primary_key']
        if upvote_serializer.is_valid():
            print('valid serializer')
            # movie_id_to_upvote = request.data['id']
            movie_to_upvote = Movie.objects.get(pk = movie_id_to_upvote)

            movie_to_upvote.vote_count = movie_to_upvote.vote_count + 1
            movie_to_upvote.save()

            return Response(upvote_serializer.data)


class ThirdPartyRatings(APIView):
    def get(self, request):
        omdb_api_key = get_omdb_api_key()
        URL = '''http://www.omdbapi.com/?apikey=''' + omdb_api_key + '''&t=the+matrix'''

        r = requests.get(url = URL)
        score_data = r.json()

        print(score_data['Ratings'])

        return Response(score_data['Ratings'])
