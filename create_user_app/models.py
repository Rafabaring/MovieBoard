from django.db import models

class Recommender(models.Model):
    first_name    = models.CharField(max_length = 20)
    last_name     = models.CharField(max_length = 20)

    # builtin sintax
    # return a string representation of this object
    def __str__(self):
        return str(self.pk) + " | " + self.first_name + "_" + self.last_name
