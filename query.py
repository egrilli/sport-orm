#1)todas las ligas de béisbol

todas_ligas=League.objects.all()


#2)todas las ligas de mujeres
todas_ligas_mujeres=League.objects.filter(name__contains='Womens')

#3) todas las ligas donde el deporte es cualquier tipo de hockey
todo_ligas_hockey=League.objects.filter(name__contains='hockey')

#4) todas las ligas donde el deporte no sea football
todo_liga_menos_futbol=League.objects.exclude(sport="Football")

#5) todas las ligas que se llaman "conferencias"

todas_ligas_conferencia=League.objects.filter(name__contains="conference")

#6) todas las ligas de la región atlántica

todas_ligas_atlantica=League.objects.filter(name__contains="atlantic")

#7) todos los equipos con sede en Dallas

todo_equipo_dalllas=Team.objects.filter(location="Dallas")

#8) todos los equipos nombraron los Raptors

todo_equipo_raptor=Team.objects.filter(team_name__contains="raptors")

#9) todos los equipos cuya ubicación incluye "Ciudad"
todo_equipo_ciudad=Team.objects.filter(location__contains="city")

#10) todos los equipos cuyos nombres comienzan con "T"
todo_equipo_emp_t=Team.objects.filter(team_name__startswith="t")


#11) todos los equipos, ordenados alfabéticamente por ubicación

todo_equipo_ordenado_abc=Team.objects.all().order_by("location")

#12) todos los equipos, ordenados por nombre de equipo en orden alfabético inverso

todo_equipo_ordenado_nombre_inverso=Team.objects.all().order_by("-team_name")

#13) cada jugador con apellido "Cooper"
jugador_apellido_cooper=Player.objects.filter(last_name="Cooper")

#14) cada jugador con nombre "Joshua"
jugador_nombre_Joshua=Player.objects.filter(first_name="Joshua")

#15) todos los jugadores con el apellido "Cooper" EXCEPTO aquellos con "Joshua" como primer nombre
jugador_apellido_cooper_ex_joshua=Player.objects.filter(last_name="Cooper").exclude(first_name="joshua")

#16) todos los jugadores con nombre "Alexander" O nombre "Wyatt"
jugador_alexander_wyatt=Player.objects.extra(where=["first_name='Alexander' OR first_name='Wyatt'"])


#PARTE 2 TAREA

#1) Todos los equipos en la American Lacrosse Conference
    american=League.objects.get(name__icontains="American Lacrosse Conference")
    todo_equipo_american=american.teams.all()


#2)todos los jugadores (actuales) en los Detroit Trail Blazers
    trail_blazers=Team.objects.get(team_name__icontains="Trail Blazers", location="Detroit")
    jugadores_trail=trail_blazers.curr_players.all()


#3) Todos los jugadores (actuales) en la International Conference of Baseball atlantic
	baseball_conference_atlantic=League.objects.get(name__icontains="International Conference of Baseball atlantic")
	teams=baseball_conference_atlantic.teams.all()
	teamsId=[]
	for team in teams:
		teamsId.append(team.id)
	jugadores=Player.objects.filter(curr_team__in=teamsId)


#4) todos los jugadores (actuales) en la Transamerican Football Conference con el apellido "Richardson"
	conferecia=League.objects.get(name__icontains="Transamerican Football Conference")
	equipos_conferencia=conferecia.teams.all()
	teamsId=[]
	for team in equipos_conferencia:
		teamsId.append(team.id)
	jugadores_conferencia=Player.objects.filter(curr_team__in=teamsId, last_name="Richardson")






... todos los jugadores de fútbol
... todos los equipos con un jugador (actual) llamado "Sophia"
... todas las ligas con un jugador (actual) llamado "Sophia"
... todos con el apellido "Flores" que NO (actualmente) juegan para los Washington Roughriders
... todos los equipos, pasados y presentes, con los que Samuel Evans ha jugado
... todos los jugadores, pasados y presentes, con los gatos tigre de Manitoba
... todos los jugadores que anteriormente estaban (pero que no lo están) con los Wichita Vikings
... cada equipo para el que Jacob Gray jugó antes de unirse a los Oregon Colts
... todos llamados "Joshua" que alguna vez han jugado en la Federación Atlántica de Jugadores de Béisbol Amateur
... todos los equipos que han tenido 12 o más jugadores, pasados y presentes. (SUGERENCIA: busque la función de anotación de Django).
... todos los jugadores y el número de equipos para los que jugó, ordenados por la cantidad de equipos para los que han jugado

atlantic=League.objects.get(name__icontains="International Conference of Baseball atlantic") 
atlanticTeams=atlantic.teams.all()

