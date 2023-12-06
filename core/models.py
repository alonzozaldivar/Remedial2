from django.db import models

# Create your models here.

class City(models.Model):
    city_name = models.CharField(max_length=20, default="Nombre de la ciudad")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.city_name
    
class Team(models.Model):
    venue = models.ForeignKey(City, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=30, default="Nombre del equipo")
    players = models.CharField(max_length=60, default="No total de jugadores")
    director = models.CharField(max_length=30, default="Director a cargo")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.team_name
    
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=30, default="Nombre del Jugador")
    number =  models.IntegerField(0)
    director = models.CharField(max_length=30, default="Director a cargo")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.player_name

class Stadium(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    stadium_name = models.CharField(max_length=50, default="Nombre del estadio")
    capacity = models.IntegerField(0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.stadium_name


