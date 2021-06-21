from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):	
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"todas_ligas":League.objects.all(),
		"baseball_ligas": League.objects.filter(sport="Baseball"),
		"todas_ligas_mujeres":League.objects.filter(name__contains='Womens'),
		"todo_ligas_hockey":League.objects.filter(name__contains='hockey'),
		"todo_liga_menos_futbol":League.objects.exclude(sport="Football"),
		"todas_ligas_conferencia":League.objects.filter(name__contains="conference"),
		"todas_ligas_atlantica":League.objects.filter(name__contains="atlantic"),
		"todo_equipo_dalllas":Team.objects.filter(location="Dallas"),
		"todo_equipo_raptor":Team.objects.filter(team_name__contains="raptors"),
		"todo_equipo_ciudad":Team.objects.filter(location__contains="city"),
		"todo_equipo_emp_t":Team.objects.filter(team_name__startswith="t"),
		"todo_equipo_ordenado_abc":Team.objects.all().order_by("location"),
		"todo_equipo_ordenado_nombre_inverso":Team.objects.all().order_by("-team_name"),
		"jugador_apellido_cooper":Player.objects.filter(last_name="Cooper"),
		"jugador_nombre_Joshua":Player.objects.filter(first_name="Joshua"),
		"jugador_apellido_cooper_ex_joshua":Player.objects.filter(last_name="Cooper").exclude(first_name="joshua"),
		"jugador_alexander_wyatt":Player.objects.extra(where=["first_name='Alexander' OR first_name='Wyatt'"]),
		
	}
	return render(request, "index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")