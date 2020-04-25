from django.contrib import admin

from movie_board_app.models import Movie, Genre
from create_user_app.models import Recommender

admin.site.register(Recommender)
admin.site.register(Movie)
admin.site.register(Genre)
