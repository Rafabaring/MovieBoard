from django.db import models

class Recommender(models.Model):
    first_name    = models.CharField(max_length = 20)
    last_name     = models.CharField(max_length = 20)


    def __str__(self):
        # return str(self.pk) + " | " + self.first_name + "_" + self.last_name

        # The MovieBoardSerializer is returning the format set in this string
        return self.first_name + " " + self.last_name
