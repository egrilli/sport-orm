from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Q, Count
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

def index1(request):

	'''1) Todos los equipos en la American Lacrosse Conference'''
	american=League.objects.get(name__icontains="American Lacrosse Conference")
	todo_equipo_american=american.teams.all()

	'''2)todos los jugadores (actuales) en los Detroit Trail Blazers'''
	trail_blazers=Team.objects.get(team_name__icontains="Trail Blazers", location="Detroit")
	jugadores_trail=trail_blazers.curr_players.all()

	'''3) Todos los jugadores (actuales) en la International Conference of Baseball atlantic'''
	jugadores_baseball= Player.objects.filter(curr_team__league__name="International Conference of Baseball atlantic")

	'''4) todos los jugadores (actuales) en la Transamerican Football Conference con el apellido "Richardson" '''
	
	jugadores_tamerican= Player.objects.filter(curr_team__league__name="Transamerican Football Conference", last_name="Richardson" )

	'''5) todos los jugadores de fútbol''' 
	
	todo_futbol=Player.objects.filter(curr_team__league__sport="Football")

	'''6) todos los equipos con un jugador (actual) llamado "Sophia" '''

	todo_equipo_sofia=Team.objects.filter(curr_players__first_name="Sophia")

	'''7) todas las ligas con un jugador (actual) llamado "Sophia" '''
	todo_liga_sofia=League.objects.filter(teams__curr_players__first_name="Sophia")

	'''8) todos los jugadores con el apellido "Flores" que NO juegan  (actualmente) para los Washington Roughriders '''
	todo_jugador_no_flores=Player.objects.filter(last_name="Flores").exclude(curr_team__team_name="Roughriders")

	'''9) todos los equipos, pasados y presentes, con los que Samuel Price ha jugado '''

	todo_equipo_samuel= Team.objects.filter(all_players__first_name="Samuel",all_players__last_name="Price")

	'''10) todos los jugadores, pasados y presentes, con los  Lakers Cleveland"  '''

	todo_jugador_chicago= Player.objects.filter(all_teams__team_name="Lakers", all_teams__location="Cleveland")

	'''11) todos los jugadores que anteriormente estaban (pero que no lo están) con los Miami Robots '''
	todo_jugador_sino= Player.objects.filter(all_teams__team_name="Robots", all_teams__location="Miami").exclude(curr_team__team_name="Robots")
	
	'''12) cada equipo para el que Jacob Hill jugó antes de unirse a los Ohio Rangers '''
	todo_equipo_jacob= Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Hill").exclude(team_name="Rangers",location="Ohio")

	'''13) todos llamados "Joshua" que alguna vez han jugado en la International Conference of Baseball atlantic '''
	todo_jugador_joshua=Player.objects.filter(first_name="Joshua", all_teams__league__name="International Conference of Baseball atlantic")

	'''14) todos los equipos que han tenido 12 o más jugadores, pasados y presentes. (SUGERENCIA: busque la función de anotación de Django). '''
	todo_equipo_doce=Team.objects.annotate(jugadores=Count("all_players")).filter(jugadores__gt=12).order_by("jugadores")

	'''15) todos los jugadores y el número de equipos para los que jugó, ordenados por la cantidad de equipos para los que han jugado '''
	todo_jugador_equipo=Player.objects.annotate(equipos= Count("all_teams")).order_by("equipos")

	context = {
		"todo_equipo_american":todo_equipo_american,
		"jugadores_trail":jugadores_trail,
		"jugadores_baseball":jugadores_baseball,
		"jugadores_tamerican":jugadores_tamerican,
		"todo_futbol":todo_futbol,
		"todo_equipo_sofia":todo_equipo_sofia,
		"todo_liga_sofia":todo_liga_sofia,
		"todo_jugador_no_flores":todo_jugador_no_flores,
		"todo_equipo_samuel":todo_equipo_samuel,
		"todo_jugador_chicago":todo_jugador_chicago,
		"todo_jugador_sino":todo_jugador_sino,
		"todo_equipo_jacob":todo_equipo_jacob,
		"todo_jugador_joshua":todo_jugador_joshua,
		"todo_equipo_doce":todo_equipo_doce,
		"todo_jugador_equipo":todo_jugador_equipo
	}
	return render(request, "index1.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")