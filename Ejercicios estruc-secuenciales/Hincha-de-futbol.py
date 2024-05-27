part_ganados1=  int(input("Ingrese la cantidad de partidos ganados la primera semana: "))

part_empatados1=  int(input("Ingrese la cantidad de partidos empatados la primera semana: "))

part_perdidos1=  int(input("Ingrese la cantidad de partidos perdidos la primera semana: "))

cant_puntos_semana1 = (part_ganados1 * 3) + (part_empatados1 * 1)

part_ganados2=  int(input("Ingrese la cantidad de partidos ganados la segunda semana: "))

part_empatados2=  int(input("Ingrese la cantidad de partidos empatados la segunda semana: "))

part_perdidos2=  int(input("Ingrese la cantidad de partidos perdidos la segunda semana: "))

cant_puntos_semana2 = (part_ganados2 * 3) + (part_empatados2 * 1)

part_ganados3=  int(input("Ingrese la cantidad de partidos ganados la tercera semana: "))

part_empatados3=  int(input("Ingrese la cantidad de partidos empatados la tercera semana: "))

part_perdidos3=  int(input("Ingrese la cantidad de partidos perdidos la tercera semana: "))

cant_puntos_semana3 = (part_ganados3 * 3) + (part_empatados3 * 1)

puntos_total = cant_puntos_semana1 + cant_puntos_semana2 + cant_puntos_semana3

print ("Los puntos acumulados en el torneo por su equipo son: ", puntos_total)