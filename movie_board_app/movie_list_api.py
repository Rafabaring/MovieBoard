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
from movie_board_app.serializers import MovieBoardSerializer, UpVoteMovieSerializer, PostMovieBoardSerializer

# List all stocks or create a new one
class MovieBoardList(APIView):
    def get(self, request):
        all_movies        = Movie.objects.all().order_by('-id')
        movies_serializer = MovieBoardSerializer(all_movies, many = True)
        return Response(movies_serializer.data)


    def post(self, request):
        movies_serializer = PostMovieBoardSerializer(data = request.data)

        if movies_serializer.is_valid():
            movies_serializer.save()
            return Response(movies_serializer.data)

        else:
            print('serializer NOT valid')
            print('')
            print('serializer: ')
            print(movies_serializer)
            print('')
            return Response(movies_serializer.errors,
                            status = status.HTTP_400_BAD_REQUEST)





class UpVoteMovie(APIView):
    def post(self, request):
        upvote_serializer = UpVoteMovieSerializer(data = request.data)
        movie_id_to_upvote = request.data['movie_primary_key']
        if upvote_serializer.is_valid():
            print('valid serializer')
            # movie_id_to_upvote = request.data['id']
            movie_to_upvote = Movie.objects.get(pk = movie_id_to_upvote)

            movie_to_upvote.vote_count = movie_to_upvote.vote_count + 1
            movie_to_upvote.save()

            return Response(upvote_serializer.data)





class ThirdPartyRatings(APIView):
    def get_third_party_score(movie_title):
        omdb_api_key = get_omdb_api_key()
        URL = '''http://www.omdbapi.com/?apikey=''' + omdb_api_key + '''&t=''' + movie_title

        r = requests.get(url = URL)
        score_data = r.json()

        # In case the user insert a movie that doesn't exist in OMDBAPI
        # The response will be "False":
        # Here's an example: {'Response': 'False', 'Error': 'Movie not found!'}
        if score_data['Response'] == "False":
            third_party_score = "rodo"
            return third_party_score


        source_dict = {}
        for i in score_data['Ratings']:
            source_dict[i['Source']] = i['Value']

        # Try to get IMDB Score first, if not, Rotten. If not, just get the first one returned
        try:
            third_party_score = source_dict['Internet Movie Database']
            third_party_score = source_dict['Rotten Tomatoes']
        except:
            third_party_score = score_data['Ratings'][0]['Value']


        return third_party_score
