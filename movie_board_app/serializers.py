from rest_framework import serializers
from movie_board_app.models import Genre, Movie
from create_user_app.models import Recommender

# This serializer is used to post new movies
class PostMovieBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

# This serializer is used to get all movies and display on the homepage
class MovieBoardSerializer(serializers.ModelSerializer):

    # recommender follows the format set in the model file
    recommender = serializers.StringRelatedField(many=False)
    #
    genre = serializers.SlugRelatedField(many=False,
                                         read_only = True,
                                         slug_field = 'genre_type')

    class Meta:
        model = Movie
        fields = (
            'id',
            'movie_title',
            'youtube_trailer_link',
            'recommendee_first_name',
            'recommendee_last_name',
            'vote_count',
            'imdb_score',
            'recommender',
            'genre'

        )


        # fields = '__all__'

class UpVoteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'movie_title')
