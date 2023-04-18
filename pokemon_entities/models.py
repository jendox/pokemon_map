from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
