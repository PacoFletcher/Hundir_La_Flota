# HUNDIR LA FLOTA

En este proyecto se ha creado un programa en Python para jugar al juego de Hundir la Flota contra la máquina.
El programa consta de cinco archivos .py intercomunicados entre sí, en los que cada uno se encarga de realizar unas funciones específicas:
1. inicio_partida.py (el main): En el se inicializa la partida, se llama al archivo `varialbes.py` para inicializar los mapas y parámetros de ambos jugadores y `jugada.py` donde se desarrollan las diferentes tiradas.
2. En la inicialización de variables, se llama al archivo `tablero.py`, donde se asignan las posiciones de los barcos a la matriz de cada jugador, comprobando previamente que no existe ningún conflicto a la hora de desplegar el barco (las posiciones no salen del tablero, ningún otro barco ocupa una posición aledaña, etc.)
3. En el archivo `funciones.py` se almacenan todas las acciones que se desempeñarán a lo largo de la partida, lo que ocurre al disparar, con qué nivel de inteligencia juega la máquina, determinar si un barco está hundido y rodear sus celdas de agua, etc.

## Inicialización de la partida

Cada vez que iniciemos una partida el programa nos pedirá elegir el nivel de dificultad del contrincante con una breve descripción de cómo se comportará.

## Sucesión de jugadas

Una vez elegida la dificultad, iniciará nuestro turno, en el que se imprimirá por pantalla nuestro tablero "check" y se solicitará primero el input de la coordenada fila y a continuación la coordenada columna. Si realizamos una entrada no válida la máquina nos avisará y nos pedirá que repitamos la introducción de variables. Los escenarios que contempla son los siguientes:
* Alguna de las variables no es numérica.
* Alguna de las variables excede los límites del tablero.
* Las coordenadas asignadas ya han sido visitadas.

La última condición también se aplica a la máquina, ya que por cómo está implementado su comportamiento, los dos primeros casos no se pueden dar.

De esta manera se agiliza la partida y se evita que en los últimos turnos la aleatoriedad de la máquina reincida en celdas que ya conoce.

## Tiradas

Cuando se dispara, se ejecuta la función `disparo(...)` a la que se le asigna la información del jugador que ha realizado la tirada y las coordenadas. Si la casilla asociada al mapa rival es agua, almacena la información en la matriz check, imprime por pantalla que en dicha posición hay y se cambia de turno. En cambio, si da con un barco, accede al vector flota para dar con el objeto que contiene esas coordenadas, le resta una vida y comrpueba cuantas le quedan. Si es mayor que 0, simplemente imprime por pantalla "Tocado", en cambio, si la vida del barco es 0, imprime "Tocado y hundido" y se ejecuta la función `pinta(...)` para añadir agua alrededor las celdas de este barco. Al haber acertado, sigue el turno del mismo jugador.

## Fin de la partida

La partida finaliza cuando uno de los dos jugadores se queda sin barcos a flote. Una vez uno de los dos jugadores se quede sin barcos se imprimirá por pantalla "¡Enhorabuena! ¡Has ganado!" o "Has perdido" y la partida finalizará.