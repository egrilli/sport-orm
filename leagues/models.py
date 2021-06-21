from django.db import models

class League(models.Model):
    name = models.CharField(max_length=50)
    sport = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
	#teams
    def __repr__(self):
        return f"< Liga: Nombre = {self.name}, Sport = {self.sport}>"

class Team(models.Model):
    location = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    league = models.ForeignKey(League, related_name="teams", on_delete = models.CASCADE)
    #curr_players
	#all_players
    def __repr__(self):
        return f"< Team: Nombre = {self.team_name}, League = {self.league}, Localidad ={self.location}>"

class Player(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    curr_team = models.ForeignKey(Team, related_name="curr_players", on_delete = models.CASCADE)
    all_teams = models.ManyToManyField(Team, related_name="all_players")

    def __repr__(self):
        return f"< Jugador: Nombre = {self.first_name}, Apellido = {self.last_name}, Equipo ={self.curr_team}, Historico Equipo = {self.all_teams}>"
