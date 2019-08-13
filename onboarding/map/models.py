from django.db import models

# Create your models here.


class Coordinates(models.Model):
    location_name = models.CharField(max_length=250)
    coordinates = models.CharField(max_length=250)

    def __str__(self):
        return self.location_name



