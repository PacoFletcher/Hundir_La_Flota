import random
import os
import tablero
import funciones
import variables

def partida(dif,turno, tirada, vidas, M, C,F):

    """    
    os.system('varialbes.py')
    turno = 0
    tirada = 0
    vidas = [20,20]
    M = variables.P
    C = variables.Q
    F = variables.R
    """
    futuro = []
    sec = False
    while vidas[0] > 0 and vidas[1] > 0:
        turno = turno%2

        if turno == 0:
            acierto = True
            while acierto and vidas[1] > 0:
                # Antes de cada tirada, imprimimos por pantalla la matriz 
                # que almacena los resultados de las tiradas para facilitar la jugabilidad
                print(f"Tirada número {tirada}, turno del jugador {turno%2 + 1}")
                funciones.imprime_tablero(C[turno])
                
                turno, acierto =  funciones.tira1(M,C,F,vidas, turno)
                tirada += 1

        else:

            acierto = True
            
            while acierto and vidas[0] > 0:
                print(f"Tirada número {tirada}, turno del jugador {turno%2 + 1}")
                funciones.imprime_tablero(C[turno])
                """for i in range(len(C2)):
                    for j in range(len(C2[i])):
                        print(C2[i][j], end = " ")
                    print("")"""
                # Al ser el turno de la máquina, la tirada será aleatoria

                
                if dif == 0:
                    turno, acierto =  funciones.dif_0(M,C,F,vidas, turno)
                        
                elif dif == 1:
                    #print("Work in Progress")
                    turno, acierto, sec, futuro = funciones.dif_1_alt(M,C,F,vidas, turno, sec, futuro)
                    #turno, acierto =  funciones.dif0(M,C,F,vidas, turno)

                elif dif == 2:
                    turno, acierto, sec =  funciones.dif_2(M,C,F,vidas, turno, sec, futuro)
                
                else :
                    turno,acierto = funciones.dif_3(M,C,F,vidas,turno)
                
                tirada += 1

             
    if vidas[0] == 0:
        print("Has perdido")
    else:
        print("¡Enhorabuena! \n¡Has ganado!")