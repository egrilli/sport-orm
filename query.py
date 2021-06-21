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

