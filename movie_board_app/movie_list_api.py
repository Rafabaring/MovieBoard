# Importing rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

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
        print('joe')
        print(upvote_serializer)
        # print(request.data)
        # print(request.data['id'])

        if upvote_serializer.is_valid():
            movie_id_to_upvote = request.data['id']
            movie_to_upvote = Movie.objects.get(pk = movie_id_to_upvote)

            print('BEFORE CHANGE')
            print(movie_to_upvote)
            print(movie_to_upvote.vote_count)
            print('')
            movie_to_upvote.vote_count = movie_to_upvote.vote_count + 1

            print('AFTER CHANGE')
            print(movie_to_upvote)
            print(movie_to_upvote.vote_count)
            print('')
            movie_to_upvote.save()

            return Response(upvote_serializer.data)
