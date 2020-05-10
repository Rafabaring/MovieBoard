from django.db import models
from create_user_app import models as create_user_app_models


class Genre(models.Model):
    genre_type    = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.pk) + " | " + self.genre_type


class Movie(models.Model):
    # Ele cria uma coluna album que, na verdade, eh o primary key da classe Album
    # on_delete = models.CASCADE --  quando o album for deletado, deletar também todas as musicas associadas a ele
    recommender            = models.ForeignKey(create_user_app_models.Recommender, on_delete = models.CASCADE)
    movie_title            = models.CharField(max_length = 50, default = '')
    youtube_trailer_link   = models.CharField(max_length = 250, default = '')
    genre                  = models.ForeignKey(Genre, on_delete = models.CASCADE)
    recommendee_first_name = models.CharField(max_length = 50, default = '')
    recommendee_last_name  = models.CharField(max_length = 50, default = '')
    vote_count             = models.IntegerField(default = 0)
    imdb_score             = models.CharField(max_length = 10, default = '')

    def __str__(self):
        return  str(self.pk) + " | " + self.recommender.first_name + " - " + self.movie_title
