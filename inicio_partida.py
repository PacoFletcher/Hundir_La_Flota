import jugada
import variables
import funciones

while True:
    turno = 0
    tirada = 1
    vidas = [20,20]
    M = variables.P
    C = variables.Q
    F = variables.R



    print("¡Bienvenido al juego de hundir la flota!")
    print("Antes de comenzar, debes seleccinar la dificultad de tu contrincante")
    pre = input("Antes de comenzar, quieres consultar los mapas? \n\
          1. Tu mapa\n\
          2. Mapa del contrincante\n \
          3. Jugar")
    if pre == "1":
        funciones.imprime_tablero(M[0])
    elif pre == "2":
        funciones.imprime_tablero(M[1])
    while True:
        dif = input("¿Cuál quieres que sea el nivel de dificultad?\n\
                0. La máquina realizará todas las tiradas de manera aleatoria.\n\
                1. La máquina intentará imitar la estrategia de un humano.\n\
                2. Si la máquina da con uno de tus barcos, puedes olvidarte de él.\n\
                3. ¡NI LO INTENTES! Este nivel es CASI imposible.\n")
        if funciones.entero(dif) and 0 <= int(dif) <= 3:
            dif = int(dif)
            break
        else:
            print("Error, introduce un número entre el 0 y el 3")
    jugada.partida(dif,turno, tirada, vidas, M, C,F)


    otra = input("Fin de la demo, pulsa cualquier botón para salir.")    
    break
print("Hasta la próxima")
