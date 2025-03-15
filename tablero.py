import random
import funciones


class barco:
    
    def __init__(self):
        self.coord = {}
        self.vida = 0


# Creamos dos matrices, M1 y M2, que corresponderán a los mapas de cada jugador y una auxiliar para hacer las modificaciones
#M = [['O' for i in range(10)] for i in range(10)]
M1 = [['O' for i in range(10)] for i in range(10)]
M2 = [['O' for i in range(10)] for i in range(10)]


# Creamos otras dos matrices, C1 y C2, que servirán a cada jugador para comprobar 
# las casillas ya visitadas
C1 = [[0 for i in range(10)] for i in range(10)]
C2 = [[0 for i in range(10)] for i in range(10)]


# Creamos una lista vacía, donde cada elemento sera un objeto clase barco
flota1 = []
# Crearemos uno por uno todos los barcos, por este motivo, los iremos implementando en el tablero según su longitud
# de eslora l
for l in range(4,0,-1):
    # Cuanta menor sea la longitud de eslora, mayor será el número de barcos que implementaremos
    # Esto lo contabilizamos mediante el iterador j que va desde 0 a 5-l
    # En caso de l = 1, 4 barcos, l = 2, 3 barcos, etc. 
    for j in range(0,5-l):
        # Inicializamos un objeto barco y lo añadimos a nuestra lista
        b = barco()      
        flota1.append(b)
        # Ubicamos nuestro barco en el mapa del jugador:
        funciones.set_mapa(M1,l,flota1)
        
        # Implementamos este sistema de control que nos permite comprobar que
        # el programa se ejecuta correctamente 
        # una vez testeado, conviene comentar este bloque de código para 
        # disponer de una mejor presentación por pantalla
        """print(f"Barco de longitud {l} número {j}:")
        for i in range(len(M1)):
            for k in range(len(M1[i])):
                print(M1[i][k], end = " ")
            print("")"""
"""
for i in flota1:
    print(i.vida, i.coord.items())

# print(flota)
for i in range(len(M1)):
    for j in range(len(M1[i])):
        print(M1[i][j], end = " ")
    print("")
"""
#print("Mapa del jugador 1:")
# funciones.imprime_tablero(M1)
# Reinicializamos la matriz auxiliar para completar el segundo mapa
# A = [['O' for i in range(10)] for i in range(10)]

# Creamos una lista vacía, donde cada elemento sera un objeto clase barco
flota2 = []
# Crearemos uno por uno todos los barcos, por este motivo, los iremos implementando en el tablero según su longitud
# de eslora l
for l in range(4,0,-1):
    # Cuanta menor sea la longitud de eslora, mayor será el número de barcos que implementaremos
    # Esto lo contabilizamos mediante el iterador j que va desde 0 a 5-l
    # En caso de l = 1, 4 barcos, l = 2, 3 barcos, etc. 
    for j in range(0,5-l):
        # Inicializamos un objeto barco y lo añadimos a nuestra lista
        b = barco()      
        flota2.append(b)
        # Ubicamos nuestro barco en el mapa del jugador:
        funciones.set_mapa(M2,l,flota2)

        # Implementamos este sistema de control que nos permite comprobar que
        # el programa se ejecuta correctamente 
        # una vez testeado, conviene comentar este bloque de código para 
        # disponer de una mejor presentación por pantalla
        """print(f"Barco de longitud {l} número {j}:")
        for i in range(len(M2)):
            for k in range(len(M2[i])):
                print(M2[i][k], end = " ")
            print("")"""
        

# Como esta información corresponde al segundo jugador (la máquina)
# no lo mostraremos en la versión definitiva

"""

for i in flota2:
    print(i.vida, i.coord.items())
# print(flota)
for i in range(len(M2)):
    for j in range(len(M2[i])):
        print(M2[i][j], end = " ")
    print("")
"""
# funciones.imprime_tablero(M2)