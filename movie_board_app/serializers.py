from rest_framework import serializers
from movie_board_app.models import Genre, Movie


class MovieBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class UpVoteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movie_title')
