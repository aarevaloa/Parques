# -*- coding: utf-8 -*-
'''
Created on Fri Feb 21 13:22:33 2025

@author: aarevaloa, apanche, dmendezra
'''
# Modulos empleados ___________________________________________________________________________________
from tkinter import *
import random

# Inicialización de variables y variables globales ____________________________________________________
global posicion_actual_j1_1, posicion_actual_j1_2, posicion_actual_j1_3, posicion_actual_j1_4
global posicion_actual_j2_1, posicion_actual_j2_2, posicion_actual_j2_3, posicion_actual_j2_4
global posicion_actual_j3_1, posicion_actual_j3_2, posicion_actual_j3_3, posicion_actual_j3_4
global posicion_actual_j4_1, posicion_actual_j4_2, posicion_actual_j4_3, posicion_actual_j4_4
global ultimo_valor_dados, valor_dado1, valor_dado2, ficha_seleccionada
global movimiento_adicional
movimiento_adicional = False
casillas_ocupadas = {}

dado1_usado = False
dado2_usado = False

# Valores iniciales de los dados
ultimo_valor_dados = 0
valor_dado1 = 0
valor_dado2 = 0
ficha_seleccionada = None

# Inicialización de posiciones jugador 1
posicion_actual_j1_1 = 0
posicion_actual_j1_2 = 0
posicion_actual_j1_3 = 0
posicion_actual_j1_4 = 0

# Inicialización de posiciones jugador 2
posicion_actual_j2_1 = 0
posicion_actual_j2_2 = 0
posicion_actual_j2_3 = 0
posicion_actual_j2_4 = 0

# Inicialización de posiciones jugador 3
posicion_actual_j3_1 = 0
posicion_actual_j3_2 = 0
posicion_actual_j3_3 = 0
posicion_actual_j3_4 = 0

# Inicialización de posiciones jugador 4
posicion_actual_j4_1 = 0
posicion_actual_j4_2 = 0
posicion_actual_j4_3 = 0
posicion_actual_j4_4 = 0

# Elementos gráficos __________________________________________________________________________________
def dibujar_malla(canva, filas, columnas, ancho, alto, desplazamiento_x, desplazamiento_y):
    '''
    Dibuja una malla en un lienzo de Tkinter dividiéndolo en una cuadrícula de celdas.

    La función crea líneas horizontales y verticales para formar la cuadrícula 
    basada en el número de filas y columnas especificadas. Se pueden aplicar 
    desplazamientos en los ejes X e Y para ajustar la posición de la malla.

    Args:
        canva (tkinter.Canvas): El lienzo en el que se dibujará la malla.
        filas (int): Número de filas en la malla.
        columnas (int): Número de columnas en la malla.
        ancho (int): Ancho total de la malla en píxeles.
        alto (int): Alto total de la malla en píxeles.
        desplazamiento_x (int): Desplazamiento en el eje X para posicionar la malla.
        desplazamiento_y (int): Desplazamiento en el eje Y para posicionar la malla.
    '''
    # Calcular el tamaño de cada celda
    cell_width = ancho / columnas
    cell_height = alto / filas

    # Dibujar las líneas horizontales
    for i in range(filas + 1):
        y = desplazamiento_y + i * cell_height  # Se agrega el desplazamiento vertical
        canva.create_line(desplazamiento_x, y, desplazamiento_x + ancho, y, fill='black')

    # Dibujar las líneas verticales
    for j in range(columnas + 1):
        x = desplazamiento_x + j * cell_width  # Se agrega el desplazamiento horizontal
        canva.create_line(x, desplazamiento_y, x, desplazamiento_y + alto, fill='black')

def dibujar_rectangulos(canva):
    '''
    Dibuja los rectángulos principales del tablero en un lienzo de Tkinter.

    La función crea un tablero de parqués representado por varios rectángulos de diferentes colores.
    Incluye el área central blanca y las zonas correspondientes a cada jugador (azul, rojo, verde y amarillo).

    Args:
        canva (tkinter.Canvas): El lienzo de Tkinter donde se dibujarán los rectángulos.
    '''
    # Rectángulos para el tablero
    canva.create_rectangle(150, 150, 650, 650, fill='lightblue', outline='black')  # Tablero general
    canva.create_rectangle(340, 340, 460, 460, fill='white')  # Zona central
    canva.create_rectangle(510, 510, 650, 650, fill='yellow')  # Zona amarilla
    canva.create_rectangle(150, 150, 290, 290, fill='blue')  # Zona azul
    canva.create_rectangle(650, 150, 510, 290, fill='red')  # Zona roja
    canva.create_rectangle(150, 510, 290, 650, fill='green')  # Zona verde


def dibujar_lineas_extra(canva):
    '''
    Dibuja líneas adicionales en el tablero de parqués.

    Esta función agrega detalles al diseño del tablero, incluyendo divisiones en el centro 
    y líneas diagonales en las bases de los jugadores. Ayuda a mejorar la representación 
    visual del tablero.

    Args:
        canva (tkinter.Canvas): El lienzo de Tkinter donde se dibujarán las líneas.
    '''
    # Coordenadas de las líneas adicionales en el tablero
    lineas = [
        (363.3, 290, 363.3, 340), (436.6, 290, 436.6, 340),  # Líneas verticales superiores
        (290, 363.3, 340, 363.3), (290, 436.6, 340, 436.6),  # Líneas horizontales izquierdas
        (363.3, 460, 363.3, 510), (436.6, 460, 436.6, 510),  # Líneas verticales inferiores
        (460, 363.3, 510, 363.3), (460, 436.6, 510, 436.6),  # Líneas horizontales derechas
        (290, 290, 340, 340), (460, 340, 510, 290),  # Líneas diagonales superiores
        (290, 510, 340, 460), (460, 460, 510, 510)   # Líneas diagonales inferiores
    ]
    
    # Dibujar cada línea en el lienzo
    for linea in lineas:
        canva.create_line(*linea, fill='black')

def dibujar_circulos(canvas, numero):
    '''
    Dibuja los puntos de un dado en un canvas según el número indicado.

    Esta función simula los puntos de un dado de seis caras en un área de 50x50 píxeles. 
    Dependiendo del número proporcionado (entre 1 y 6), se dibujan los círculos en 
    posiciones predefinidas dentro del dado.

    Args:
        canvas (tkinter.Canvas): El lienzo donde se dibujarán los puntos del dado.
        numero (int): El número del dado (debe estar en el rango de 1 a 6).
    '''
    
    # Coordenadas de los círculos para cada número del dado
    posiciones = {
        1: [(25, 25)],  # Centro
        2: [(10, 10), (40, 40)],  # Esquinas opuestas
        3: [(10, 10), (25, 25), (40, 40)],  # Diagonal
        4: [(10, 10), (40, 10), (10, 40), (40, 40)],  # Cuatro esquinas
        5: [(10, 10), (40, 10), (25, 25), (10, 40), (40, 40)],  # Esquinas + centro
        6: [(10, 10), (40, 10), (10, 25), (40, 25), (10, 40), (40, 40)],  # Dos columnas
    }

    # Dibujar los círculos en el canvas según la posición de cada número
    for (x, y) in posiciones[numero]:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='black')
        
def dibujar_dado(canvas, numero):
    '''
    Dibuja la representación gráfica de un dado en un canvas de Tkinter.

    La función borra cualquier dibujo previo en el canvas y luego dibuja los puntos 
    correspondientes al número del dado lanzado (1-6), siguiendo el diseño estándar 
    de distribución de puntos en un dado de seis caras.

    Args:
        canvas (tkinter.Canvas): El lienzo de Tkinter donde se dibujará el dado.
        numero (int): El valor del dado a representar (entre 1 y 6).

    Returns:
        La función no retorna nada, solo dibuja en el canvas.

    Notas:
        - Se utiliza un sistema de coordenadas predefinido para colocar los puntos 
          correctamente dentro de un dado de 50x50 píxeles.
        - Cada punto del dado es un pequeño círculo negro.
        - La función elimina cualquier dibujo previo en el canvas antes de dibujar 
          el nuevo resultado del dado.
    '''
    # Limpiar el canvas antes de dibujar
    canvas.delete('all')

    # Parámetros de tamaño y posición de los puntos del dado
    radio = 4  # Radio de los círculos que representan los puntos
    padding = 10  # Margen entre los puntos y los bordes del dado
    centro_x = 25  # Coordenada x central del dado
    centro_y = 25  # Coordenada y central del dado
    
    # Diccionario con las posiciones de los puntos para cada número del dado
    posiciones = {
        1: [(centro_x, centro_y)],
        2: [(padding, padding), (50-padding, 50-padding)],
        3: [(padding, padding), (centro_x, centro_y), (50-padding, 50-padding)],
        4: [(padding, padding), (padding, 50-padding), 
            (50-padding, padding), (50-padding, 50-padding)],
        5: [(padding, padding), (padding, 50-padding), 
            (centro_x, centro_y),
            (50-padding, padding), (50-padding, 50-padding)],
        6: [(padding, padding), (padding, centro_y), (padding, 50-padding),
            (50-padding, padding), (50-padding, centro_y), (50-padding, 50-padding)]
    }
    
    # Dibujar los puntos correspondientes al número del dado
    for x, y in posiciones[numero]:
        canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill='black')


# Funciones para la selección de jugadores y determinar el orden ______________________________________
def seleccionar_jugadores():
    '''
    Solicita al usuario que ingrese la cantidad de jugadores para la partida.

    La función pide un número entre 2 y 4, validando la entrada del usuario. 
    Si la entrada es incorrecta (fuera del rango o no es un número entero), 
    se muestra un mensaje de error y se vuelve a solicitar hasta recibir una 
    entrada válida.

    Returns:
        int: Número de jugadores seleccionados (entre 2 y 4).
    '''
    while True:
        try:
            num_jugadores = int(input('Ingrese el número de jugadores (2-4): '))
            if 2 <= num_jugadores <= 4:
                return num_jugadores
            else:
                print('Por favor, ingrese un número entre 2 y 4.')
        except ValueError:
            print('Entrada no válida. Ingrese un número entero.')


num_jugadores = seleccionar_jugadores()

def determinar_orden_jugadores(jugadores):
    '''
    Determina el orden de turno de los jugadores lanzando un dado.

    Cada jugador lanza un dado (valores entre 1 y 6). El jugador con el número más alto
    jugará primero. En caso de empate, los jugadores empatados vuelven a lanzar el dado
    hasta que se determine un único ganador. El proceso se repite hasta establecer un 
    orden de turnos sin empates.

    Args:
        jugadores (int): Número total de jugadores en la partida.

    Returns:
        list: Lista ordenada con los jugadores en el orden en que jugarán, del primero al último.
    
    Prints:
        - Mensajes indicando los empates y relanzamientos de los dados.
        - Resultados finales del lanzamiento de los dados.
    '''
    # Lanzamiento inicial de los dados
    resultados = {jugador: random.randint(1, 6) for jugador in range(jugadores)}
    
    max_puntaje = max(resultados.values())
    empatados = [jugador for jugador, puntaje in resultados.items() if puntaje == max_puntaje]

    # Desempatar en caso de empate
    while len(empatados) > 1:
        print(f'Empate entre {empatados}. Relanzando el dado...')
        nuevos_resultados = {jugador: random.randint(1, 6) for jugador in empatados}
        resultados.update(nuevos_resultados)

        max_puntaje = max(nuevos_resultados.values())
        empatados = [jugador for jugador, puntaje in nuevos_resultados.items() if puntaje == max_puntaje]

    # Ordenar jugadores por puntaje de mayor a menor
    orden_jugadores = sorted(resultados.items(), key=lambda x: x[1], reverse=True)
    
    print('\nResultados finales del lanzamiento:')
    for jugador, puntaje in orden_jugadores:
        print(f'{jugador}: {puntaje}')

    return [jugador for jugador, _ in orden_jugadores]

orden = determinar_orden_jugadores(num_jugadores)
            
# Diccionario de coordenadas para el movimiento de las fichas _________________________________________
# Coordenadas de movieminto del jugar 1
Jugador_1_coor = {1:[312.5, 231, 332.5, 251], # Salida
                  2:[312.5, 251, 332.5, 271],
                  3:[312.5, 271, 332.5, 291],
                  4:[312.5, 291, 332.5, 311], 
                  5:[293.5, 316, 313.5, 336],
                  6:[270.3, 316, 290.3, 336],
                  7:[250.3, 316, 270.3, 336],
                  8:[230.3, 316, 250.3, 336],
                  9:[210.3, 316, 230.3, 336],
                  10:[190.3, 316, 210.3, 336],
                  11:[170.3, 316, 190.3, 336],
                  12:[150.3, 316, 170.3, 336],
                  13:[150.3, 388, 170.3, 408],
                  14:[150.3, 465, 170.3, 485],
                  15:[170.3, 465, 190.3, 485],
                  16:[190.3, 465, 210.3, 485],
                  17:[210.3, 465, 230.3, 485],
                  18:[230.3, 465, 250.3, 485],
                  19:[250.3, 465, 270.3, 485],
                  20:[270.3, 465, 290.3, 485],
                  21:[290.3, 465, 310.3, 485],
                  22:[317.3, 485, 337.3, 505],
                  23:[317.3, 510, 337.3, 530],
                  24:[317.3, 530, 337.3, 550],
                  25:[317.3, 550, 337.3, 570],
                  26:[317.3, 570, 337.3, 590],
                  27:[317.3, 590, 337.3, 610],
                  28:[317.3, 610, 337.3, 630],
                  29:[317.3, 630, 337.3, 650],
                  30:[390.3, 630, 410.3, 650],
                  31:[463.3, 630, 483.3, 650],
                  32:[463.3, 610, 483.3, 630],
                  33:[463.3, 590, 483.3, 610],
                  34:[463.3, 570, 483.3, 590],
                  35:[463.3, 550, 483.3, 570],
                  36:[463.3, 530, 483.3, 550],
                  37:[463.3, 510, 483.3, 530],
                  38:[463.3, 490, 483.3, 510],
                  39:[490.3, 460, 510.3, 480],
                  40:[510.3, 460, 530.3, 480],
                  41:[530.3, 460, 550.3, 480],
                  42:[550.3, 460, 570.3, 480],
                  43:[570.3, 460, 590.3, 480],
                  44:[590.3, 460, 610.3, 480],
                  45:[610.3, 460, 630.3, 480],
                  46:[630.3, 460, 650.3, 480],
                  47:[630.3, 390, 650.3, 410],
                  48:[630.3, 318, 650.3, 338],
                  49:[610.3, 318, 630.3, 338],
                  50:[590.3, 318, 610.3, 338],
                  51:[570.3, 318, 590.3, 338],
                  52:[550.3, 318, 570.3, 338],
                  53:[530.3, 318, 550.3, 338],
                  54:[510.3, 318, 530.3, 338],
                  55:[490.3, 318, 510.3, 338],
                  56:[460.3, 290, 480.3, 310],
                  57:[460.3, 270, 480.3, 290],
                  58:[460.3, 250, 480.3, 270],
                  59:[460.3, 230, 480.3, 250],
                  60:[460.3, 210, 480.3, 230],
                  61:[460.3, 190, 480.3, 210],
                  62:[460.3, 170, 480.3, 190],
                  63:[460.3, 150, 480.3, 170],
                  64:[390.3, 150, 410.3, 170], # Casillas llegada Azul
                  65:[390.3, 170, 410.3, 190], # Casillas llegada Azul
                  66:[390.3, 190, 410.3, 210], # Casillas llegada Azul
                  67:[390.3, 210, 410.3, 230], # Casillas llegada Azul
                  68:[390.3, 230, 410.3, 250], # Casillas llegada Azul
                  69:[390.3, 250, 410.3, 270], # Casillas llegada Azul
                  70:[390.3, 270, 410.3, 290], # Casillas llegada Azul
                  71:[390.3, 310, 410.3, 330], # Casillas llegada Azul
                  72:[390.3, 350, 410.3, 370]} # Casillas llegada Azul 

# Coordenadas de movieminto del jugar 2
Jugador_2_coor = {1:[550.3, 318, 570.3, 338], # salida área roja
                  2:[530.3, 318, 550.3, 338],
                  3:[510.3, 318, 530.3, 338],
                  4:[490.3, 318, 510.3, 338],
                  5:[460.3, 290, 480.3, 310],
                  6:[460.3, 270, 480.3, 290],
                  7:[460.3, 250, 480.3, 270], # Seguro 2 área roja
                  8:[460.3, 230, 480.3, 250],
                  9:[460.3, 210, 480.3, 230], 
                  10:[460.3, 190, 480.3, 210],
                  11:[460.3, 170, 480.3, 190], # Seguro 3 área roja
                  12:[460.3, 150, 480.3, 170],
                  13:[390.3, 150, 410.3, 170], # Inicio área azul
                  14:[315.3, 150, 335.3, 170], 
                  15:[315.3, 170, 335.3, 190],
                  16:[315.3, 190, 335.3, 210],
                  17:[315.3, 210, 335.3, 230],
                  18:[312.5, 231, 332.5, 251], # Salida área azul 
                  19:[312.5, 251, 332.5, 271],
                  20:[312.5, 271, 332.5, 291],
                  21:[312.5, 291, 332.5, 311], 
                  22:[293.5, 316, 313.5, 336],
                  23:[270.3, 316, 290.3, 336],
                  24:[250.3, 316, 270.3, 336],
                  25:[230.3, 316, 250.3, 336],
                  26:[210.3, 316, 230.3, 336],
                  27:[190.3, 316, 210.3, 336],
                  28:[170.3, 316, 190.3, 336],
                  29:[150.3, 316, 170.3, 336], # Fin área azul
                  30:[150.3, 388, 170.3, 408], # Inicio área verde
                  31:[150.3, 465, 170.3, 485],
                  32:[170.3, 465, 190.3, 485],
                  33:[190.3, 465, 210.3, 485],
                  34:[210.3, 465, 230.3, 485],
                  35:[230.3, 465, 250.3, 485], # Seguro área verde
                  36:[250.3, 465, 270.3, 485],
                  37:[270.3, 465, 290.3, 485],
                  38:[290.3, 465, 310.3, 485],
                  39:[317.3, 485, 337.3, 505],
                  40:[317.3, 510, 337.3, 530],
                  41:[317.3, 530, 337.3, 550],
                  42:[317.3, 550, 337.3, 570],
                  43:[317.3, 570, 337.3, 590],
                  44:[317.3, 590, 337.3, 610],
                  45:[317.3, 610, 337.3, 630],
                  46:[317.3, 630, 337.3, 650], # Fin área verde
                  47:[390.3, 630, 410.3, 650], # Inicio área blanca
                  48:[463.3, 630, 483.3, 650],
                  49:[463.3, 610, 483.3, 630],
                  50:[463.3, 590, 483.3, 610],
                  51:[463.3, 570, 483.3, 590],
                  52:[463.3, 550, 483.3, 570], # Seguro área blanca
                  53:[463.3, 530, 483.3, 550],
                  54:[463.3, 510, 483.3, 530],
                  55:[463.3, 490, 483.3, 510],
                  56:[490.3, 460, 510.3, 480],
                  57:[510.3, 460, 530.3, 480],
                  58:[530.3, 460, 550.3, 480],
                  59:[550.3, 460, 570.3, 480],
                  60:[570.3, 460, 590.3, 480],
                  61:[590.3, 460, 610.3, 480],
                  62:[610.3, 460, 630.3, 480],
                  63:[630.3, 460, 650.3, 480], # Fin área blanca
                  64:[630.3, 390, 650.3, 410], # Casillas llegada Rojas
                  65:[610.3, 390, 630.3, 410], # Casillas llegada Rojas
                  66:[590.3, 390, 610.3, 410], # Casillas llegada Rojas
                  67:[570.3, 390, 590.3, 410], # Casillas llegada Rojas
                  68:[550.3, 390, 570.3, 410], # Casillas llegada Rojas
                  69:[530.3, 390, 550.3, 410], # Casillas llegada Rojas
                  70:[510.3, 390, 530.3, 410], # Casillas llegada Rojas
                  71:[470.3, 390, 490.3, 410], # Casillas llegada Rojas
                  72:[430.3, 390, 450.3, 410]} # Casillas llegada Rojas

# Coordenadas de movieminto del jugar 3
Jugador_3_coor = {1:[230.3, 465, 250.3, 485], # Salida área verde
                  2:[250.3, 465, 270.3, 485],
                  3:[270.3, 465, 290.3, 485],
                  4:[290.3, 465, 310.3, 485],
                  5:[317.3, 485, 337.3, 505],
                  6:[317.3, 510, 337.3, 530],
                  7:[317.3, 530, 337.3, 550],
                  8:[317.3, 550, 337.3, 570], # Seguro 2 área verde
                  9:[317.3, 570, 337.3, 590],
                  10:[317.3, 590, 337.3, 610],
                  11:[317.3, 610, 337.3, 630],
                  12:[317.3, 630, 337.3, 650], # Fin área verde
                  13:[390.3, 630, 410.3, 650], # Inicio área blanca
                  14:[463.3, 630, 483.3, 650],
                  15:[463.3, 610, 483.3, 630],
                  16:[463.3, 590, 483.3, 610],
                  17:[463.3, 570, 483.3, 590],
                  18:[463.3, 550, 483.3, 570], # Seguro área blanca
                  19:[463.3, 530, 483.3, 550],
                  20:[463.3, 510, 483.3, 530],
                  21:[463.3, 490, 483.3, 510],
                  22:[490.3, 460, 510.3, 480],
                  23:[510.3, 460, 530.3, 480],
                  24:[530.3, 460, 550.3, 480],
                  25:[550.3, 460, 570.3, 480],
                  26:[570.3, 460, 590.3, 480],
                  27:[590.3, 460, 610.3, 480],
                  28:[610.3, 460, 630.3, 480],
                  29:[630.3, 460, 650.3, 480], # Fin área blanca
                  30:[630.3, 390, 650.3, 410], # Seguro llegada área roja
                  31:[630.3, 318, 650.3, 338],
                  32:[610.3, 318, 630.3, 338],
                  33:[590.3, 318, 610.3, 338],
                  34:[570.3, 318, 590.3, 338],
                  35:[550.3, 318, 570.3, 338], # salida área roja
                  36:[530.3, 318, 550.3, 338],
                  37:[510.3, 318, 530.3, 338],
                  38:[490.3, 318, 510.3, 338],
                  39:[460.3, 290, 480.3, 310],
                  40:[460.3, 270, 480.3, 290],
                  41:[460.3, 250, 480.3, 270],
                  42:[460.3, 230, 480.3, 250],
                  43:[460.3, 210, 480.3, 230],
                  44:[460.3, 190, 480.3, 210],
                  45:[460.3, 170, 480.3, 190],
                  46:[460.3, 150, 480.3, 170], # Fin área roja
                  47:[390.3, 150, 410.3, 170], # Inicio área azul
                  48:[315.3, 150, 335.3, 170], 
                  49:[315.3, 170, 335.3, 190],
                  50:[315.3, 190, 335.3, 210],
                  51:[315.3, 210, 335.3, 230],
                  52:[312.5, 231, 332.5, 251], # Salida área azul 
                  53:[312.5, 251, 332.5, 271],
                  54:[312.5, 271, 332.5, 291],
                  55:[312.5, 291, 332.5, 311], 
                  56:[293.5, 316, 313.5, 336],
                  57:[270.3, 316, 290.3, 336],
                  58:[250.3, 316, 270.3, 336],
                  59:[230.3, 316, 250.3, 336],
                  60:[210.3, 316, 230.3, 336],
                  61:[190.3, 316, 210.3, 336],
                  62:[170.3, 316, 190.3, 336],
                  63:[150.3, 316, 170.3, 336], # Fin área azul
                  64:[150.3, 388, 170.3, 408], # Inicio área verde
                  65:[170.3, 388, 190.3, 408], # Casillas llegada verde
                  66:[190.3, 388, 210.3, 408], # Casillas llegada verde
                  67:[210.3, 388, 230.3, 408], # Casillas llegada verde
                  68:[230.3, 388, 250.3, 408], # Casillas llegada verde
                  69:[250.3, 388, 270.3, 408], # Casillas llegada verde
                  70:[270.3, 388, 290.3, 408], # Casillas llegada verde
                  71:[310.3, 388, 330.3, 408], # Casillas llegada verde
                  72:[350.3, 388, 370.3, 408]} # Casillas llegada verde 
        
# Coordenadas de movieminto del jugar 4
Jugador_4_coor = {1:[463.3, 550, 483.3, 570], # Salida área blanca
                  2:[463.3, 530, 483.3, 550],
                  3:[463.3, 510, 483.3, 530],
                  4:[463.3, 490, 483.3, 510],
                  5:[490.3, 460, 510.3, 480],
                  6:[510.3, 460, 530.3, 480],
                  7:[530.3, 460, 550.3, 480],
                  8:[550.3, 460, 570.3, 480],
                  9:[570.3, 460, 590.3, 480],
                  10:[590.3, 460, 610.3, 480],
                  11:[610.3, 460, 630.3, 480],
                  12:[630.3, 460, 650.3, 480], # Fin área blanca
                  13:[630.3, 390, 650.3, 410], # Seguro llegada área roja
                  14:[630.3, 318, 650.3, 338],
                  15:[610.3, 318, 630.3, 338],
                  16:[590.3, 318, 610.3, 338],
                  17:[570.3, 318, 590.3, 338],
                  18:[550.3, 318, 570.3, 338], # Salida área roja
                  19:[530.3, 318, 550.3, 338],
                  20:[510.3, 318, 530.3, 338],
                  21:[490.3, 318, 510.3, 338],
                  22:[460.3, 290, 480.3, 310],
                  23:[460.3, 270, 480.3, 290],
                  24:[460.3, 250, 480.3, 270],
                  25:[460.3, 230, 480.3, 250],
                  26:[460.3, 210, 480.3, 230],
                  27:[460.3, 190, 480.3, 210],
                  28:[460.3, 170, 480.3, 190],
                  29:[460.3, 150, 480.3, 170], # Fin área roja
                  30:[390.3, 150, 410.3, 170], # Inicio área azul
                  31:[315.3, 150, 335.3, 170], 
                  32:[315.3, 170, 335.3, 190],
                  33:[315.3, 190, 335.3, 210],
                  34:[315.3, 210, 335.3, 230],
                  35:[312.5, 231, 332.5, 251], # Salida área azul 
                  36:[312.5, 251, 332.5, 271],
                  37:[312.5, 271, 332.5, 291],
                  38:[312.5, 291, 332.5, 311], 
                  39:[293.5, 316, 313.5, 336],
                  40:[270.3, 316, 290.3, 336],
                  41:[250.3, 316, 270.3, 336],
                  42:[230.3, 316, 250.3, 336],
                  43:[210.3, 316, 230.3, 336],
                  44:[190.3, 316, 210.3, 336],
                  45:[170.3, 316, 190.3, 336],
                  46:[150.3, 316, 170.3, 336], # Fin área azul
                  47:[150.3, 388, 170.3, 408], # Inicio área verde
                  48:[150.3, 465, 170.3, 485],
                  49:[170.3, 465, 190.3, 485],
                  50:[190.3, 465, 210.3, 485],
                  51:[210.3, 465, 230.3, 485],
                  52:[230.3, 465, 250.3, 485], # Seguro área verde
                  53:[250.3, 465, 270.3, 485],
                  54:[270.3, 465, 290.3, 485],
                  55:[290.3, 465, 310.3, 485],
                  56:[317.3, 485, 337.3, 505],
                  57:[317.3, 510, 337.3, 530],
                  58:[317.3, 530, 337.3, 550],
                  59:[317.3, 550, 337.3, 570],
                  60:[317.3, 570, 337.3, 590],
                  61:[317.3, 590, 337.3, 610],
                  62:[317.3, 610, 337.3, 630],
                  63:[317.3, 630, 337.3, 650], # Fin área verde
                  64:[390.3, 630, 410.3, 650], # Inicio área blanca
                  65:[390.3, 610, 410.3, 630], # LLegada área blanca
                  66:[390.3, 590, 410.3, 610], # LLegada área blanca
                  67:[390.3, 570, 410.3, 590], # LLegada área blanca
                  68:[390.3, 550, 410.3, 570], # LLegada área blanca
                  69:[390.3, 530, 410.3, 550], # LLegada área blanca
                  70:[390.3, 510, 410.3, 530], # LLegada área blanca
                  71:[390.3, 470, 410.3, 490], # LLegada área blanca
                  71:[390.3, 420, 410.3, 440]} # LLegada área blanca

# Funciones par el movimiento _________________________________________________________________________
def obtener_posicion_actual(ficha):
    '''
    Devuelve la posición actual de una ficha específica en el tablero.

    Parámetros:
    ficha : objeto
        Representa una ficha de uno de los jugadores.

    Retorna:
    tuple
        Coordenadas de la posición actual de la ficha en el tablero.

    Notas:
    - La función asocia cada ficha con su respectiva posición actual.
    - lA función hace uso variables globales que almacenan las posiciones actuales de las fichas de cada jugador.
    - La función cubre hasta cuatro fichas por jugador y admite cuatro jugadores.
    '''
    # Jugador 1
    if ficha == cir_j1_1:
        return posicion_actual_j1_1
    elif ficha == cir_j1_2:
        return posicion_actual_j1_2
    elif ficha == cir_j1_3:
        return posicion_actual_j1_3
    elif ficha == cir_j1_4:
        return posicion_actual_j1_4
    # Jugador 2
    elif ficha == cir_j2_1:
        return posicion_actual_j2_1
    elif ficha == cir_j2_2:
        return posicion_actual_j2_2
    elif ficha == cir_j2_3:
        return posicion_actual_j2_3
    elif ficha == cir_j2_4:
        return posicion_actual_j2_4
    # Jugador 3
    elif ficha == cir_j3_1:
        return posicion_actual_j3_1
    elif ficha == cir_j3_2:
        return posicion_actual_j3_2
    elif ficha == cir_j3_3:
        return posicion_actual_j3_3
    elif ficha == cir_j3_4:
        return posicion_actual_j3_4
    # Jugador 4
    elif ficha == cir_j4_1:
        return posicion_actual_j4_1
    elif ficha == cir_j4_2:
        return posicion_actual_j4_2
    elif ficha == cir_j4_3:
        return posicion_actual_j4_3
    elif ficha == cir_j4_4:
        return posicion_actual_j4_4

def mover_ficha(ficha, posicion):
    '''
    Mueve una ficha a una nueva posición en el tablero si la posición es válida.

    Parámetros:
    ficha : objeto
        Representa la ficha que se va a mover.
    posicion : int
        Índice de la nueva posición de la ficha en el tablero.

    Comportamiento:
    - Si la posición es diferente de 0, la función verifica a qué jugador pertenece la ficha.
    - Si la posición es válida dentro del conjunto de coordenadas del jugador correspondiente, 
      actualiza las coordenadas de la ficha en el canvas.
    - Utiliza el método `coords` de `canva` para ajustar la posición de la ficha en la interfaz gráfica.

    Notas:
    - Las coordenadas de cada posición están almacenadas en diccionarios específicos para cada jugador.
    - Cada jugador tiene hasta cuatro fichas que pueden moverse en el tablero.
    '''
    if posicion != 0:
        if ficha in [cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4]:
            if posicion in Jugador_1_coor:
                nuevas_coords = Jugador_1_coor[posicion]
                canva.coords(ficha, 
                            nuevas_coords[0], 
                            nuevas_coords[1], 
                            nuevas_coords[2], 
                            nuevas_coords[3])
        elif ficha in [cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4]:
            if posicion in Jugador_2_coor:
                nuevas_coords = Jugador_2_coor[posicion]
                canva.coords(ficha, 
                            nuevas_coords[0], 
                            nuevas_coords[1], 
                            nuevas_coords[2], 
                            nuevas_coords[3])
        elif ficha in [cir_j3_1, cir_j3_2, cir_j3_3, cir_j3_4]:
            if posicion in Jugador_3_coor:
                nuevas_coords = Jugador_3_coor[posicion]
                canva.coords(ficha, 
                            nuevas_coords[0], 
                            nuevas_coords[1], 
                            nuevas_coords[2], 
                            nuevas_coords[3])
        elif ficha in [cir_j4_1, cir_j4_2, cir_j4_3, cir_j4_4]:
            if posicion in Jugador_4_coor:
                nuevas_coords = Jugador_4_coor[posicion]
                canva.coords(ficha, 
                            nuevas_coords[0], 
                            nuevas_coords[1], 
                            nuevas_coords[2], 
                            nuevas_coords[3])

def obtener_jugador_ficha(ficha):
    '''
    Determina a qué jugador pertenece una ficha específica.

    Parámetros:
    ficha : objeto
        Representa la ficha cuya pertenencia se desea conocer.

    Retorna:
    int o None
        - Retorna un número entero del 1 al 4 indicando el jugador al que pertenece la ficha.
        - Retorna None si la ficha no corresponde a ningún jugador conocido.

    Notas:
    - Los jugador tiene un conjunto de cuatro fichas.
    - La función compara la ficha con las listas predefinidas de fichas de cada jugador.
    '''
    if ficha in [cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4]:
        return 1
    elif ficha in [cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4]:
        return 2
    elif ficha in [cir_j3_1, cir_j3_2, cir_j3_3, cir_j3_4]:
        return 3
    elif ficha in [cir_j4_1, cir_j4_2, cir_j4_3, cir_j4_4]:
        return 4
    return None

def enviar_a_prision(ficha):
    '''
    Envía una ficha a la zona de prisión y actualiza su estado en el juego.

    Parámetros:
    ficha : objeto
        Representa la ficha que será enviada a la prisión.

    Comportamiento:
    - Elimina la ficha de su posición actual en el diccionario `casillas_ocupadas` si está registrada.
    - Actualiza la posición de la ficha a 0.
    - Mueve gráficamente la ficha a las coordenadas correspondientes en `canva`.
    - Imprime un mensaje confirmando que la ficha ha sido enviada a prisión.

    Notas:
    - `obtener_posicion_actual(ficha)` se usa para determinar la ubicación actual de la ficha.
    - La `casillas_ocupadas` es un diccionario global que rastrea la ocupación del tablero.
    - Las coordenadas de la prisión varían según el jugador al que pertenece la ficha.
    '''
    # Primero eliminar la ficha de su posición actual en el diccionario
    posicion_actual = obtener_posicion_actual(ficha)
    if posicion_actual in casillas_ocupadas and casillas_ocupadas[posicion_actual] == ficha:
        del casillas_ocupadas[posicion_actual]
    
    # Actualizar la posición a 0
    # actualizar_posicion(ficha, 0)
    
    # Mover la ficha a las coordenadas de prisión correspondientes
    if ficha == cir_j1_1:
        canva.coords(ficha, 192.5, 192.5, 212.5, 212.5)
    elif ficha == cir_j1_2:
        canva.coords(ficha, 227.5, 192.5, 247.5, 212.5)
    elif ficha == cir_j1_3:
        canva.coords(ficha, 192.5, 227.5, 212.5, 247.5)
    elif ficha == cir_j1_4:
        canva.coords(ficha, 227.5, 227.5, 247.5, 247.5)
    elif ficha == cir_j2_1:
        canva.coords(ficha, 552.5, 192.5, 572.5, 212.5)
    elif ficha == cir_j2_2:
        canva.coords(ficha, 587.5, 192.5, 607.5, 212.5)
    elif ficha == cir_j2_3:
        canva.coords(ficha, 552.5, 227.5, 572.5, 247.5)
    elif ficha == cir_j2_4:
        canva.coords(ficha, 587.5, 227.5, 607.5, 247.5)
    elif ficha == cir_j3_1:
        canva.coords(ficha, 192.5, 552.5, 212.5, 572.5)
    elif ficha == cir_j3_2:
        canva.coords(ficha, 227.5, 552.5, 247.5, 572.5)
    elif ficha == cir_j3_3:
        canva.coords(ficha, 192.5, 587.5, 212.5, 607.5)
    elif ficha == cir_j3_4:
        canva.coords(ficha, 227.5, 587.5, 247.5, 607.5)
    elif ficha == cir_j4_1:
        canva.coords(ficha, 552.5, 552.5, 572.5, 572.5)
    elif ficha == cir_j4_2:
        canva.coords(ficha, 587.5, 552.5, 607.5, 572.5)
    elif ficha == cir_j4_3:
        canva.coords(ficha, 552.5, 587.5, 572.5, 607.5)
    elif ficha == cir_j4_4:
        canva.coords(ficha, 587.5, 587.5, 607.5, 607.5)
    
    print(f'¡Ficha enviada a prisión (casa)!')

def calcular_distancia(x1, y1, x2, y2):
    '''
    Calcula la distancia euclidiana entre dos puntos en un plano cartesiano.

    Parámetros:
    x1, y1 : float
        Coordenadas del primer punto.
    x2, y2 : float
        Coordenadas del segundo punto.

    Retorna:
    float
        Distancia euclidiana entre los dos puntos.

    Notas:
    - La distancia se calcula usando la fórmula: sqrt((x1 - x2)^2 + (y1 - y2)^2).
    - Útil para determinar proximidad entre objetos en un tablero o interfaz gráfica.
    - Se emplea para detección de captura por áreas en lugar de coordenadas exactas.
    '''
    # Para poder capturar por arreas y no por coordenadas.
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def verificar_captura(ficha, nueva_posicion):
    '''
   Verifica si una ficha captura a otra al moverse a una nueva posición.

   Parámetros:
   ficha : objeto
       La ficha que se está moviendo.
   nueva_posicion : int
       La nueva posición a la que se mueve la ficha.

   Retorna:
   bool
       - `True` si la ficha ha capturado a otra.
       - `False` si no hay captura.

   Comportamiento:
   - No se verifican capturas si la ficha está en la prisión.
   - Se obtiene el jugador al que pertenece la ficha y sus coordenadas en el tablero.
   - Se verifica si hay fichas cercanas dentro de un radio de tolerancia de 10 píxeles.
   - No se capturan fichas propias ni fichas ubicadas en áreas de seguridad.
   - Si una ficha enemiga está dentro del radio de captura, se envía a prisión y la captura se registra.
   - Si no hay captura, simplemente se actualiza la nueva posición de la ficha en el diccionario `casillas_ocupadas`.

   Notas:
   - `canva.coords(ficha)` obtiene las coordenadas de la ficha en el lienzo.
   - `calcular_distancia(x1, y1, x2, y2)` calcula la distancia euclidiana entre dos fichas.
   - `enviar_a_prision(ficha_existente)` mueve la ficha capturada a la prisión.
   - `esta_en_seguro(ficha_existente)` verifica si la ficha enemiga está en una zona segura, evitando su captura.
   '''
    global movimiento_adicional
    
    # No verificar capturas en la prisión
    if nueva_posicion == 0:
        return False
        
    jugador_actual = obtener_jugador_ficha(ficha)
    
    # Obtener coordenadas de la ficha actual
    coords_ficha = canva.coords(ficha)
    centro_ficha_x = (coords_ficha[0] + coords_ficha[2]) / 2
    centro_ficha_y = (coords_ficha[1] + coords_ficha[3]) / 2
    
    # Radio de tolerancia en píxeles
    radio_tolerancia = 10
    
    # Buscar fichas cercanas para capturar
    for pos, ficha_existente in list(casillas_ocupadas.items()):
        # No verificar la misma ficha
        if ficha == ficha_existente:
            continue
            
        # Verificar si la ficha existente está en un área de seguro
        if esta_en_seguro(ficha_existente):
            continue
            
        # Obtener jugador de la ficha existente
        jugador_existente = obtener_jugador_ficha(ficha_existente)
        
        # No capturar fichas del mismo jugador
        if jugador_actual == jugador_existente:
            continue
            
        # Obtener coordenadas de la ficha existente
        coords_existente = canva.coords(ficha_existente)
        centro_existente_x = (coords_existente[0] + coords_existente[2]) / 2
        centro_existente_y = (coords_existente[1] + coords_existente[3]) / 2
        
        # Calcular distancia entre las fichas
        distancia = calcular_distancia(centro_ficha_x, centro_ficha_y, 
                                       centro_existente_x, centro_existente_y)
        
        # Si están dentro del radio de tolerancia, realizar captura
        if distancia <= radio_tolerancia:
            print(f'¡Captura! Jugador {jugador_actual} captura la ficha del Jugador {jugador_existente}')
            enviar_a_prision(ficha_existente)
            casillas_ocupadas[nueva_posicion] = ficha
            
            # Activar el movimiento adicional de 10 espacios
            movimiento_adicional = True
            print(f'¡Jugador {jugador_actual} puede mover 10 espacios adicionales!')
            return True
    
    # Si no hubo captura, simplemente actualizar el diccionario
    casillas_ocupadas[nueva_posicion] = ficha
    return False

# Seguros _____________________________________________________________________________________________
seguro = [[483, 540, 500, 580],
          [360, 140, 440, 180],
          [530, 308, 590, 348],
          [370, 620, 430, 660],
          [200, 455, 280, 495],
          [120, 378, 200, 418],
          [347, 540, 367, 580],
          [493, 540, 513, 580],  # Salida área blanca 
          [600, 380, 680, 420]]  # Inicio área roja

# _____________________________________________________________________________________________________

def esta_en_seguro(ficha):
    '''
    Verifica si una ficha está dentro de un área segura en el tablero.

    Parámetros:
    ficha : objeto
        La ficha cuya ubicación se desea evaluar.

    Retorna:
    bool
        - `True` si la ficha está en una zona segura.
        - `False` si la ficha no está en una zona segura.

    Comportamiento:
    - Obtiene las coordenadas actuales de la ficha en el lienzo `canva`.
    - Calcula el centro de la ficha a partir de sus coordenadas.
    - Recorre la lista de áreas seguras y verifica si el centro de la ficha está dentro de alguna de ellas.

    Notas:
    - `canva.coords(ficha)` obtiene las coordenadas actuales de la ficha en el tablero.
    - `seguro` es una lista de áreas seguras definidas como rectángulos con coordenadas `(x1, y1, x2, y2)`.
    - Las fichas dentro de estas áreas no pueden ser capturadas.
    '''
    # Obtener las coordenadas actuales de la ficha
    coords = canva.coords(ficha)
    
    # Calcular el centro de la ficha
    centro_x = (coords[0] + coords[2]) / 2
    centro_y = (coords[1] + coords[3]) / 2
    
    # Verificar si el centro está dentro de alguna área de seguro
    for area in seguro:
        if (area[0] <= centro_x <= area[2] and 
            area[1] <= centro_y <= area[3]):
            return True
    
    return False

def actualizar_posicion(ficha, nueva_posicion):
    '''
    Actualiza la posición de una ficha en el tablero y en las variables de estado.

    Parámetros:
    ficha : objeto
        La ficha cuya posición se va a actualizar.
    nueva_posicion : int
        La nueva posición de la ficha en el tablero. Si es 0, se considera la prisión.

    Comportamiento:
    - Elimina la ficha de su posición anterior en el diccionario `casillas_ocupadas`.
    - Si la nueva posición no es la prisión, la agrega al diccionario con su nueva ubicación.
    - Actualiza las variables globales que almacenan la posición de cada ficha de cada jugador.

    Notas:
    - `obtener_posicion_actual(ficha)` obtiene la posición actual de la ficha antes de actualizarla.
    - `casillas_ocupadas` es un diccionario que almacena las posiciones de todas las fichas en el tablero.
    - Se utilizan variables globales (`posicion_actual_jX_Y`) para llevar un control de la posición de cada ficha.
    '''
    # Primero eliminar la ficha de su posición actual en el diccionario
    posicion_actual = obtener_posicion_actual(ficha)
    if posicion_actual in casillas_ocupadas and casillas_ocupadas[posicion_actual] == ficha:
        del casillas_ocupadas[posicion_actual]
    
    # Si la nueva posición no es la prisión, agregar la ficha al diccionario
    if nueva_posicion != 0:
        casillas_ocupadas[nueva_posicion] = ficha
    
    # Actualizar las variables globales de posición
    global posicion_actual_j1_1, posicion_actual_j1_2, posicion_actual_j1_3, posicion_actual_j1_4
    global posicion_actual_j2_1, posicion_actual_j2_2, posicion_actual_j2_3, posicion_actual_j2_4
    global posicion_actual_j3_1, posicion_actual_j3_2, posicion_actual_j3_3, posicion_actual_j3_4
    global posicion_actual_j4_1, posicion_actual_j4_2, posicion_actual_j4_3, posicion_actual_j4_4
    
    if ficha == cir_j1_1:
        posicion_actual_j1_1 = nueva_posicion
    elif ficha == cir_j1_2:
        posicion_actual_j1_2 = nueva_posicion
    elif ficha == cir_j1_3:
        posicion_actual_j1_3 = nueva_posicion
    elif ficha == cir_j1_4:
        posicion_actual_j1_4 = nueva_posicion
    # Jugador 2
    elif ficha == cir_j2_1:
        posicion_actual_j2_1 = nueva_posicion
    elif ficha == cir_j2_2:
        posicion_actual_j2_2 = nueva_posicion
    elif ficha == cir_j2_3:
        posicion_actual_j2_3 = nueva_posicion
    elif ficha == cir_j2_4:
        posicion_actual_j2_4 = nueva_posicion
    # Jugador 3
    elif ficha == cir_j3_1:
        posicion_actual_j3_1 = nueva_posicion
    elif ficha == cir_j3_2:
        posicion_actual_j3_2 = nueva_posicion
    elif ficha == cir_j3_3:
        posicion_actual_j3_3 = nueva_posicion
    elif ficha == cir_j3_4:
        posicion_actual_j3_4 = nueva_posicion
    # Jugador 4
    elif ficha == cir_j4_1:
        posicion_actual_j4_1 = nueva_posicion
    elif ficha == cir_j4_2:
        posicion_actual_j4_2 = nueva_posicion
    elif ficha == cir_j4_3:
        posicion_actual_j4_3 = nueva_posicion
    elif ficha == cir_j4_4:
        posicion_actual_j4_4 = nueva_posicion

def seleccionar_jugadores():
    '''
    Solicita al usuario el número de jugadores y valida la entrada.

    Retorna:
    int
        El número de jugadores seleccionado (entre 2 y 4).

    Comportamiento:
    - Pide al usuario ingresar un número entre 2 y 4.
    - Si la entrada no es válida (no es un número entero o está fuera del rango), muestra un mensaje de error y vuelve a solicitar la entrada.
    - Continúa solicitando un valor válido hasta que el usuario ingrese un número correcto.

    Notas:
    - La función usa un bucle `while True` para garantizar que solo se acepte una entrada válida.
    - `int(input(...))` convierte la entrada del usuario en un número entero.
    - Se manejan excepciones `ValueError` para evitar errores si el usuario ingresa un valor no numérico.
    '''
    while True:
        try:
            num_jugadores = int(input('Ingrese el número de jugadores (2-4): '))
            if 2 <= num_jugadores <= 4:
                return num_jugadores
            else:
                print('Por favor, ingrese un número entre 2 y 4.')
        except ValueError:
            print('Entrada no válida. Ingrese un número entero.')

class SistemaTurnos:
    '''
    Gestiona los turnos de los jugadores en el juego.

    Atributos:
    num_jugadores : int
        Número total de jugadores en la partida.
    turno_actual : int
        Índice del jugador cuyo turno está en curso.
    jugadores : list
        Lista con los nombres de los jugadores.
    colores : dict
        Diccionario que asigna un color a cada jugador.
    fichas_jugador : dict
        Diccionario que asigna las fichas disponibles a cada jugador.

    Métodos:
    __init__(num_jugadores)
        Inicializa el sistema de turnos con la cantidad de jugadores especificada.
    inicializar_fichas(fichas_disponibles)
        Asigna las fichas a cada jugador a partir de un diccionario de fichas disponibles.
    obtener_jugador_actual()
        Retorna el nombre del jugador que tiene el turno actual.
    siguiente_turno()
        Avanza al siguiente turno y retorna el nombre del nuevo jugador en turno.
    puede_mover_ficha(ficha)
        Verifica si la ficha pertenece al jugador que tiene el turno.

    Notas:
    - Los colores de los jugadores se definen en el diccionario `colores`.
    - El orden de los turnos es cíclico, avanzando de 0 a `num_jugadores - 1` y reiniciándose después.
    - `fichas_jugador` se llena con las fichas disponibles para cada jugador después de llamar a `inicializar_fichas`.
    '''
    def __init__(self, num_jugadores):
        self.num_jugadores = num_jugadores
        self.turno_actual = 0
        self.jugadores = [f'Jugador {i+1}' for i in range(num_jugadores)]
        self.colores = {
            'Jugador 1': '#4682B4',  # Azul
            'Jugador 2': '#50C878',  # Verde
            'Jugador 3': '#FFFFCC',  # Amarillo
            'Jugador 4': '#FF6666'   # Rojo
        }
    
    def inicializar_fichas(self, fichas_disponibles):
        self.fichas_jugador = {}
        for jugador in self.jugadores:
            num_jugador = int(jugador.split()[-1])
            if num_jugador in fichas_disponibles:
                self.fichas_jugador[jugador] = fichas_disponibles[num_jugador]
    
    def obtener_jugador_actual(self):
        return self.jugadores[self.turno_actual]
    
    def siguiente_turno(self):
        self.turno_actual = (self.turno_actual + 1) % self.num_jugadores
        return self.jugadores[self.turno_actual]
    
    def puede_mover_ficha(self, ficha):
        jugador_actual = self.obtener_jugador_actual()
        return jugador_actual in self.fichas_jugador and ficha in self.fichas_jugador[jugador_actual]
            
def verificar_victoria(jugador_num):
    '''
    Verifica si un jugador ha ganado la partida.

    Parámetros:
    jugador_num : int
        Número del jugador cuya victoria se quiere verificar (1, 2, 3 o 4).

    Retorna:
    bool
        True si todas las fichas del jugador han alcanzado su respectiva zona de victoria, False en caso contrario.

    Descripción:
    - Cada jugador tiene un área de victoria representada por una región triangular específica en el tablero.
    - La función obtiene las coordenadas de las cuatro fichas del jugador indicado.
    - Se verifica si todas las fichas están dentro del área de victoria con una tolerancia de 30 píxeles.
    
    Notas:
    - Las posiciones de victoria están definidas con coordenadas específicas para cada jugador.
    - La función actualmente admite verificación para los cuatro jugadores.
    - Se usa `canva.coords(ficha)` para obtener las coordenadas de cada ficha en el tablero.
    - La tolerancia de 30 píxeles compensa imprecisiones en la detección de posición.
    '''
    if jugador_num == 1:
        # Obtener las coordenadas actuales de cada ficha del jugador 1
        coords_j1_1 = canva.coords(cir_j1_1)
        coords_j1_2 = canva.coords(cir_j1_2)
        coords_j1_3 = canva.coords(cir_j1_3)
        coords_j1_4 = canva.coords(cir_j1_4)
        
        # Verificar si todas las fichas están en la posición central
        centro_x, centro_y = 400, 370
        tolerancia = 30  # Un pequeño margen de error para las coordenadas
        
        return (abs(coords_j1_1[0] + (coords_j1_1[2] - coords_j1_1[0])/2 - centro_x) < tolerancia and
                abs(coords_j1_1[1] + (coords_j1_1[3] - coords_j1_1[1])/2 - centro_y) < tolerancia and
                abs(coords_j1_2[0] + (coords_j1_2[2] - coords_j1_2[0])/2 - centro_x) < tolerancia and
                abs(coords_j1_2[1] + (coords_j1_2[3] - coords_j1_2[1])/2 - centro_y) < tolerancia and
                abs(coords_j1_3[0] + (coords_j1_3[2] - coords_j1_3[0])/2 - centro_x) < tolerancia and
                abs(coords_j1_3[1] + (coords_j1_3[3] - coords_j1_3[1])/2 - centro_y) < tolerancia and
                abs(coords_j1_4[0] + (coords_j1_4[2] - coords_j1_4[0])/2 - centro_x) < tolerancia and
                abs(coords_j1_4[1] + (coords_j1_4[3] - coords_j1_4[1])/2 - centro_y) < tolerancia)
                
    elif jugador_num == 2:
        # Obtener las coordenadas actuales de cada ficha del jugador 2
        coords_j2_1 = canva.coords(cir_j2_1)
        coords_j2_2 = canva.coords(cir_j2_2)
        coords_j2_3 = canva.coords(cir_j2_3)
        coords_j2_4 = canva.coords(cir_j2_4)
        
        # Verificar si todas las fichas están en la posición central
        centro_x, centro_y = 430, 400
        tolerancia = 30
        
        return (abs(coords_j2_1[0] + (coords_j2_1[2] - coords_j2_1[0])/2 - centro_x) < tolerancia and
                abs(coords_j2_1[1] + (coords_j2_1[3] - coords_j2_1[1])/2 - centro_y) < tolerancia and
                abs(coords_j2_2[0] + (coords_j2_2[2] - coords_j2_2[0])/2 - centro_x) < tolerancia and
                abs(coords_j2_2[1] + (coords_j2_2[3] - coords_j2_2[1])/2 - centro_y) < tolerancia and
                abs(coords_j2_3[0] + (coords_j2_3[2] - coords_j2_3[0])/2 - centro_x) < tolerancia and
                abs(coords_j2_3[1] + (coords_j2_3[3] - coords_j2_3[1])/2 - centro_y) < tolerancia and
                abs(coords_j2_4[0] + (coords_j2_4[2] - coords_j2_4[0])/2 - centro_x) < tolerancia and
                abs(coords_j2_4[1] + (coords_j2_4[3] - coords_j2_4[1])/2 - centro_y) < tolerancia)
                
    elif jugador_num == 3:
        # Obtener las coordenadas actuales de cada ficha del jugador 3
        coords_j3_1 = canva.coords(cir_j3_1)
        coords_j3_2 = canva.coords(cir_j3_2)
        coords_j3_3 = canva.coords(cir_j3_3)
        coords_j3_4 = canva.coords(cir_j3_4)
        
        # Verificar si todas las fichas están en la posición central
        centro_x, centro_y = 370, 400
        tolerancia = 30
        
        return (abs(coords_j3_1[0] + (coords_j3_1[2] - coords_j3_1[0])/2 - centro_x) < tolerancia and
                abs(coords_j3_1[1] + (coords_j3_1[3] - coords_j3_1[1])/2 - centro_y) < tolerancia and
                abs(coords_j3_2[0] + (coords_j3_2[2] - coords_j3_2[0])/2 - centro_x) < tolerancia and
                abs(coords_j3_2[1] + (coords_j3_2[3] - coords_j3_2[1])/2 - centro_y) < tolerancia and
                abs(coords_j3_3[0] + (coords_j3_3[2] - coords_j3_3[0])/2 - centro_x) < tolerancia and
                abs(coords_j3_3[1] + (coords_j3_3[3] - coords_j3_3[1])/2 - centro_y) < tolerancia and
                abs(coords_j3_4[0] + (coords_j3_4[2] - coords_j3_4[0])/2 - centro_x) < tolerancia and
                abs(coords_j3_4[1] + (coords_j3_4[3] - coords_j3_4[1])/2 - centro_y) < tolerancia)
                
    elif jugador_num == 4:
        # Obtener las coordenadas actuales de cada ficha del jugador 4
        coords_j4_1 = canva.coords(cir_j4_1)
        coords_j4_2 = canva.coords(cir_j4_2)
        coords_j4_3 = canva.coords(cir_j4_3)
        coords_j4_4 = canva.coords(cir_j4_4)
        
        # Verificar si todas las fichas están en la posición central
        centro_x, centro_y = 400, 430
        tolerancia = 30
        
        return (abs(coords_j4_1[0] + (coords_j4_1[2] - coords_j4_1[0])/2 - centro_x) < tolerancia and
                abs(coords_j4_1[1] + (coords_j4_1[3] - coords_j4_1[1])/2 - centro_y) < tolerancia and
                abs(coords_j4_2[0] + (coords_j4_2[2] - coords_j4_2[0])/2 - centro_x) < tolerancia and
                abs(coords_j4_2[1] + (coords_j4_2[3] - coords_j4_2[1])/2 - centro_y) < tolerancia and
                abs(coords_j4_3[0] + (coords_j4_3[2] - coords_j4_3[0])/2 - centro_x) < tolerancia and
                abs(coords_j4_3[1] + (coords_j4_3[3] - coords_j4_3[1])/2 - centro_y) < tolerancia and
                abs(coords_j4_4[0] + (coords_j4_4[2] - coords_j4_4[0])/2 - centro_x) < tolerancia and
                abs(coords_j4_4[1] + (coords_j4_4[3] - coords_j4_4[1])/2 - centro_y) < tolerancia)
    
    return False

def mostrar_victoria(jugador_num):
    '''
    Muestra un mensaje emergente anunciando la victoria de un jugador.

    Parámetros:
    jugador_num : int
        Número del jugador que ha ganado la partida.

    Descripción:
    - Utiliza `tkinter.messagebox.showinfo` para desplegar un cuadro de diálogo con el mensaje de victoria.
    - El mensaje indica qué jugador ha ganado el juego.
    
    '''
    import tkinter as tk
    from tkinter import messagebox
    
    # Mostrar mensaje de victoria
    messagebox.showinfo('¡Felicidades!', f'¡El Jugador {jugador_num} ha ganado el juego!')

# Áreas de prisión (x1, y1, x2, y2)
prision_j1 = (180, 180, 250, 250)  # Jugador 1
prision_j2 = (540, 180, 610, 250)  # Jugador 2
prision_j3 = (180, 540, 250, 610)  # Jugador 3
prision_j4 = (540, 540, 610, 610)  # Jugador 4

def esta_en_prision(ficha, area_prision):
    '''
    Verifica si una ficha se encuentra dentro del área de prisión.

    Parámetros:
    ficha : objeto de tkinter
        La ficha cuya posición se va a verificar en el canvas.
    area_prision : tuple
        Una tupla de cuatro valores (x1, y1, x2, y2) que define los límites del área de prisión.

    Retorna:
    bool
        True si el centro de la ficha está dentro del área de prisión, False en caso contrario.

    Descripción:
    - Obtiene las coordenadas actuales de la ficha en el canvas.
    - Calcula el punto central de la ficha.
    - Verifica si ese punto está dentro de los límites del área de prisión.
    '''
    x1, y1, x2, y2 = area_prision
    coords = canva.coords(ficha)
    if not coords:
        return False
    ficha_x1, ficha_y1, ficha_x2, ficha_y2 = coords
    # Verificar si el centro de la ficha está dentro del área de prisión
    centro_x = (ficha_x1 + ficha_x2) / 2
    centro_y = (ficha_y1 + ficha_y2) / 2
    return (x1 <= centro_x <= x2) and (y1 <= centro_y <= y2)

def tiene_fichas_en_prision(jugador_num):
    """
    Verifica si el jugador tiene al menos una ficha en prisión.
    """
    if jugador_num == 1:
        fichas = [cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4]
        area_prision = prision_j1
    elif jugador_num == 2:
        fichas = [cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4]
        area_prision = prision_j2
    elif jugador_num == 3:
        fichas = [cir_j3_1, cir_j3_2, cir_j3_3, cir_j3_4]
        area_prision = prision_j3
    elif jugador_num == 4:
        fichas = [cir_j4_1, cir_j4_2, cir_j4_3, cir_j4_4]
        area_prision = prision_j4
    else:
        return False

    # Verificar si alguna ficha está en prisión
    for ficha in fichas:
        if esta_en_prision(ficha, area_prision):
            return True
    return False

def todas_las_fichas_en_prision(jugador_num):
    '''
    Verifica si todas las fichas de un jugador están dentro de su área de prisión.

    Parámetros:
    jugador_num : int
        Número del jugador cuya condición de prisión se quiere verificar (1-4).

    Retorna:
    bool
        True si todas las fichas del jugador están en prisión, False en caso contrario.

    Descripción:
    - Determina las fichas del jugador en función de su número.
    - Obtiene el área de prisión correspondiente a ese jugador.
    - Verifica si todas las fichas están dentro de la zona de prisión usando `esta_en_prision(ficha, area_prision)`.

    Notas:
    - Si el número de jugador no es válido (fuera del rango 1-4), la función devuelve False.
    '''
    if jugador_num == 1:
        fichas = [cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4]
        area_prision = prision_j1
    elif jugador_num == 2:
        fichas = [cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4]
        area_prision = prision_j2
    elif jugador_num == 3:
        fichas = [cir_j3_1, cir_j3_2, cir_j3_3, cir_j3_4]
        area_prision = prision_j3
    elif jugador_num == 4:
        fichas = [cir_j4_1, cir_j4_2, cir_j4_3, cir_j4_4]
        area_prision = prision_j4
    else:
        return False

    # Verificar si todas las fichas están en prisión
    for ficha in fichas:
        if not esta_en_prision(ficha, area_prision):
            return False
    return True

def tirar_dados(par):
    '''
    Realiza la acción de lanzar los dados y maneja la lógica del turno del jugador.

    Parámetros:
    par : No se utiliza dentro de la función, pero se mantiene en la firma por compatibilidad con llamadas previas.

    Variables globales utilizadas:
    - ultimo_valor_dados: Almacena la suma de los valores de los dados (aunque ya no se usa para mover).
    - sistema_turnos: Controla la gestión de los turnos de los jugadores.
    - valor_dado1, valor_dado2: Guardan los valores actuales de los dados lanzados.
    - dado1_usado, dado2_usado: Flags que indican si cada dado ha sido utilizado.

    Descripción:
    - Verifica si el jugador aún tiene valores de dados pendientes de usar. Si es así, le notifica y no permite lanzar nuevamente.
    - Reinicia los estados de los dados antes de cada tirada.
    - Genera dos valores aleatorios entre 1 y 6 simulando el lanzamiento de los dados.
    - Muestra visualmente los dados en `canvas1` y `canvas2` llamando a `dibujar_dado()`.
    - Verifica si el jugador actual tiene todas sus fichas en prisión:
      - Si obtiene un 5 en alguno de los dados o la suma es 5, puede liberar una ficha.
      - Si los valores de los dados son pares mientras está en prisión, pierde su turno.
      - En caso contrario, pasa el turno al siguiente jugador.
    - Si los dados obtenidos son pares y el jugador no está en prisión, puede lanzar nuevamente.
    
    Notas:
    - `todas_las_fichas_en_prision(jugador_num)` verifica si un jugador tiene todas sus fichas bloqueadas.
    - La visualización de los dados depende de `dibujar_dado()`, que se encarga de actualizar los gráficos en el lienzo.
    - En algunos casos, la función fuerza el cambio de turno si el jugador no puede moverse.

    '''
    global ultimo_valor_dados, sistema_turnos, valor_dado1, valor_dado2, dado1_usado, dado2_usado
    
    # Verificar si hay dados pendientes por usar
    if not (dado1_usado and dado2_usado) and (valor_dado1 != 0 or valor_dado2 != 0):
        print('Aún tienes dados disponibles para usar')
        if not dado1_usado:
            print(f'Dado 1: {valor_dado1}')
        if not dado2_usado:
            print(f'Dado 2: {valor_dado2}')
        return
    
    # Reiniciar estados de dados
    dado1_usado = False
    dado2_usado = False
    
    # Tirar los dados
    valor_dado1 = random.randint(1, 6)
    valor_dado2 = random.randint(1, 6)
    ultimo_valor_dados = valor_dado1 + valor_dado2  # Este ya no se usará para mover
    
    # Dibujar los dados
    dibujar_dado(canvas1, valor_dado1)
    dibujar_dado(canvas2, valor_dado2)
    
    jugador_actual = sistema_turnos.obtener_jugador_actual()
    jugador_num = int(jugador_actual.split()[-1])
    print(f'\nTurno de {jugador_actual}')
    print(f'Dado 1: {valor_dado1}, Dado 2: {valor_dado2}')
    
    # Verificar si el jugador tiene todas sus fichas en prisión
    if todas_las_fichas_en_prision(jugador_num):
        # Nueva condición: Si la suma de los dados es 5 o alguno de los dados es 5
        if (valor_dado1 + valor_dado2 == 5) or (valor_dado1 == 5 or valor_dado2 == 5):
            print('¡Puedes sacar una ficha de prisión!')
            return
        else:
            if valor_dado1 == valor_dado2:
                print('Todas tus fichas están en prisión y sacaste pares. Pasando al siguiente jugador.')
                sistema_turnos.siguiente_turno()
                siguiente_jugador = sistema_turnos.obtener_jugador_actual()
                print(f'Turno de {siguiente_jugador}')
                valor_dado1 = 0
                valor_dado2 = 0
                return
            else:
                print('No sacaste un 5 o la suma de los dados no es 5. No puedes mover fichas. Pasando al siguiente jugador.')
                sistema_turnos.siguiente_turno()
                siguiente_jugador = sistema_turnos.obtener_jugador_actual()
                print(f'Turno de {siguiente_jugador}')
                valor_dado1 = 0
                valor_dado2 = 0
                return
    
    # Verificar si los dados son pares (para jugadores que no están bloqueados)
    if valor_dado1 == valor_dado2:
        print('¡Dados pares! Puedes lanzar de nuevo.')
    else:
        # Si no son pares, el turno cambiará después de usar ambos dados
        pass

def esta_en_prision(ficha, area_prision):
    '''
    Verifica si una ficha está dentro de un área de prisión.

    Parámetros:
    ficha : objeto gráfico de Tkinter
        La ficha cuya posición se desea verificar.
    area_prision : tuple
        Coordenadas del área de prisión en formato (x1, y1, x2, y2),
        donde (x1, y1) representa la esquina superior izquierda y (x2, y2) la inferior derecha.

    Retorna:
    bool
        True si el centro de la ficha está dentro del área de prisión, False en caso contrario.

    Descripción:
    - Obtiene las coordenadas de la ficha dentro del lienzo (`canva`).
    - Calcula el centro de la ficha como el promedio de sus coordenadas extremas.
    - Verifica si el centro de la ficha está dentro de los límites del área de prisión.
    - Si la ficha no tiene coordenadas asignadas, se asume que no está en prisión y se retorna False.

    Notas:
    - La comparación se realiza con los límites del área de prisión para determinar si la ficha está dentro
    '''
    x1, y1, x2, y2 = area_prision
    coords = canva.coords(ficha)
    if not coords:
        return False
    ficha_x1, ficha_y1, ficha_x2, ficha_y2 = coords
    # Verificar si el centro de la ficha está dentro del área de prisión
    centro_x = (ficha_x1 + ficha_x2) / 2
    centro_y = (ficha_y1 + ficha_y2) / 2
    return (x1 <= centro_x <= x2) and (y1 <= centro_y <= y2)
 
def click_ficha(event, ficha):
    '''
    Maneja el evento de clic sobre una ficha y permite su movimiento según las reglas del juego.

    Parámetros:
    event : Evento de Tkinter
        Evento de clic generado al seleccionar una ficha en el tablero.
    ficha : objeto gráfico de Tkinter
        La ficha seleccionada que el jugador intenta mover.

    Descripción:
    - Verifica si los dados han sido lanzados antes de permitir el movimiento.
    - Comprueba si es el turno del jugador correspondiente a la ficha seleccionada.
    - Determina la posición actual de la ficha en el tablero.
    - Evalúa si la ficha está en prisión y si puede salir según las reglas (se necesita un 5 o que la suma de los dados sea 5).
    - Permite al jugador elegir qué dado usar para mover la ficha en caso de que tenga opciones.
    - Mueve la ficha en el tablero y actualiza su posición.
    - Verifica si hay capturas de fichas rivales.
    - Comprueba si el movimiento realizado conduce a una condición de victoria.
    - Controla el flujo del turno y decide si el jugador puede volver a tirar los dados en caso de sacar pares.

    Notas:
    - La función usa variables globales para gestionar los valores de los dados y el control de turnos.
    - Se asume que `mover_ficha`, `actualizar_posicion`, `verificar_captura` y `verificar_victoria` están definidas en el juego.
    - La entrada del dado a usar es solicitada mediante `input()`, lo que puede necesitar adaptación si se usa en una interfaz completamente gráfica.

    Retorna:
        No retorna un valor explícito, pero realiza múltiples operaciones sobre las fichas y el flujo del juego.
    '''
    global valor_dado1, valor_dado2, dado1_usado, dado2_usado, sistema_turnos, movimiento_adicional
    
    if valor_dado1 == 0 and valor_dado2 == 0:
        print('Primero tira los dados')
        return
    
    jugador_actual = sistema_turnos.obtener_jugador_actual()
    jugador_num = int(jugador_actual.split()[-1])
    
    if not sistema_turnos.puede_mover_ficha(ficha):
        print(f'No es tu turno. Es el turno de {jugador_actual}')
        return
    
    posicion_actual = obtener_posicion_actual(ficha)
    
    # Mostrar dados disponibles
    dados_disponibles = []
    if not dado1_usado:
        dados_disponibles.append(valor_dado1)
    if not dado2_usado:
        dados_disponibles.append(valor_dado2)
    
    if not dados_disponibles:
        print('Ya usaste todos los dados. Tira los dados nuevamente.')
        return
    
    # Si la ficha está en prisión
    if posicion_actual == 0:
        # Nueva condición: Si la suma de los dados es 5 o alguno de los dados es 5
        if (valor_dado1 + valor_dado2 == 5) or (valor_dado1 == 5 or valor_dado2 == 5):
            # Usar el 5 para salir
            if valor_dado1 == 5 and not dado1_usado:
                dado1_usado = True
                nueva_posicion = 1
            elif valor_dado2 == 5 and not dado2_usado:
                dado2_usado = True
                nueva_posicion = 1
            else:
                # Si la suma es 5 pero no hay un 5 individual, usar ambos dados
                if valor_dado1 + valor_dado2 == 5:
                    if not dado1_usado and not dado2_usado:
                        dado1_usado = True
                        dado2_usado = True
                        nueva_posicion = 1
                    else:
                        print('Error: Ambos dados deben estar disponibles para usar la suma.')
                        return
                else:
                    print('Error al seleccionar el dado')
                    return
            
            print('¡Ficha liberada de prisión!')
            
            # Mover la ficha a la nueva posición
            mover_ficha(ficha, nueva_posicion)
            
            # Actualizar la posición en el diccionario
            actualizar_posicion(ficha, nueva_posicion)
            
            # Verificar si se usaron todos los dados
            if dado1_usado and dado2_usado:
                # Reiniciar valores y pasar turno solo si los dados no son pares
                if valor_dado1 != valor_dado2:
                    valor_dado1 = 0
                    valor_dado2 = 0
                    dado1_usado = False
                    dado2_usado = False
                    sistema_turnos.siguiente_turno()
                    siguiente_jugador = sistema_turnos.obtener_jugador_actual()
                    print(f'\nTurno de {siguiente_jugador}')
                else:
                    print('¡Dados pares! Puedes lanzar de nuevo.')
            else:
                # Mostrar dados restantes
                print('\nAún tienes dados disponibles para usar')
                if not dado1_usado:
                    print(f'Dado 1: {valor_dado1}')
                if not dado2_usado:
                    print(f'Dado 2: {valor_dado2}')
            
            return  # Terminar la función después de sacar la ficha de prisión
        else:
            print('Necesitas un 5 o que la suma de los dados sea 5 para salir de prisión')
            return
    else:
        # Si la ficha está en el tablero, preguntar qué dado quiere usar
        print(f'Dados disponibles: {dados_disponibles}')
        dado_elegido = int(input('Ingrese el valor del dado que desea usar: '))
        
        if dado_elegido not in dados_disponibles:
            print('Ese dado no está disponible')
            return
        
        # Usar el dado seleccionado
        if dado_elegido == valor_dado1 and not dado1_usado:
            dado1_usado = True
            nueva_posicion = posicion_actual + valor_dado1
        elif dado_elegido == valor_dado2 and not dado2_usado:
            dado2_usado = True
            nueva_posicion = posicion_actual + valor_dado2
        else:
            print('Error al seleccionar el dado')
            return
    
    if nueva_posicion <= max(Jugador_1_coor.keys()):
        # Mover la ficha a la nueva posición
        mover_ficha(ficha, nueva_posicion)
        
        # Verificar y procesar capturas después de mover la ficha
        hubo_captura = verificar_captura(ficha, nueva_posicion)
        
        # Actualizar la posición en el diccionario
        actualizar_posicion(ficha, nueva_posicion)
        
        if hubo_captura:
            print('¡Capturaste una ficha!')
            # Si hubo captura, permitir mover 10 espacios adicionales
            if movimiento_adicional:
                nueva_posicion += 10
                if nueva_posicion <= max(Jugador_1_coor.keys()):
                    mover_ficha(ficha, nueva_posicion)
                    actualizar_posicion(ficha, nueva_posicion)
                    print(f'Ficha movida 10 espacios adicionales a la posición {nueva_posicion}')
                movimiento_adicional = False  # Reiniciar el movimiento adicional
        
        print(f'Ficha movida a la posición {nueva_posicion}')
        
        # Verificar si hay victoria después de mover
        if verificar_victoria(jugador_num):
            mostrar_victoria(jugador_num)
            return  # Terminar la función si hay victoria
        
        # Verificar si se usaron todos los dados
        if dado1_usado and dado2_usado:
            # Reiniciar valores y pasar turno solo si los dados no son pares
            if valor_dado1 != valor_dado2:
                valor_dado1 = 0
                valor_dado2 = 0
                dado1_usado = False
                dado2_usado = False
                sistema_turnos.siguiente_turno()
                siguiente_jugador = sistema_turnos.obtener_jugador_actual()
                print(f'\nTurno de {siguiente_jugador}')
            else:
                print('¡Dados pares! Puedes lanzar de nuevo.')
        else:
            # Mostrar dados restantes
            print('\nAún tienes dados disponibles para usar')
            if not dado1_usado:
                print(f'Dado 1: {valor_dado1}')
            if not dado2_usado:
                print(f'Dado 2: {valor_dado2}')
    else:
        print('Movimiento no válido: excede el límite del tablero')
        
def main():
    '''
    Función principal que inicializa y configura la interfaz gráfica del juego de Parchís.
    
    - Crea una ventana principal con un lienzo (Canvas) donde se dibuja el tablero.
    - Dibuja las áreas de juego con colores correspondientes a cada jugador.
    - Dibuja las casillas seguras, las salidas y las zonas de llegada.
    - Configura el número de jugadores y sus fichas, permitiendo su interacción con el ratón.
    - Inicializa el sistema de turnos basado en el número de jugadores seleccionados.

    Variables globales:
    - canva: Objeto Canvas donde se dibuja el tablero.
    - raiz: Ventana principal de la aplicación.
    - sistema_turnos: Objeto que maneja los turnos de los jugadores.
    - cir_jX_Y: Fichas de cada jugador (X: número de jugador, Y: número de ficha).
    - fichas_disponibles: Diccionario que almacena las fichas de cada jugador.

    Llamadas a funciones auxiliares:
    - dibujar_rectangulos(canva): Dibuja las áreas principales del tablero.
    - dibujar_malla(canva, filas, columnas, x, y, ancho, alto): Dibuja las casillas del tablero.
    - dibujar_lineas_extra(canva): Agrega detalles adicionales al tablero.
    - click_ficha(evento, ficha): Maneja la selección de fichas mediante clics.

    Consideraciones:
    - Soporta de 2 a 4 jugadores.
    - Cada jugador tiene 4 fichas que pueden moverse por el tablero.
    - El color de cada jugador está representado en su zona de inicio y fichas.
    '''
    global canva, cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4
    global canva, cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4
    global canva, canvas1, canvas3, canvas2, canvas4, boton1, boton2, raiz
    global sistema_turnos
    
    raiz = Tk()
    raiz.title('Parchís')
    raiz.resizable(False, False)
    
    canva = Canvas(raiz, width=800, height=800, background='pink')
    canva.pack()
    
    # Llamadas a funciones para dibujar (mantén todas tus funciones de dibujo aquí)
    dibujar_rectangulos(canva)
    coordenadas1 = [290, 150, 436.6, 150, 436.6, 340, 340, 340, 340, 363.3, 150, 363.3, 150, 290, 290, 290]
    coordenadas2 = [340, 363.3, 340, 363.3, 340, 460, 363.3, 460, 363.3, 650, 290, 650, 290, 510, 150, 510, 150, 363.3]
    coordenadas3 = [363.3, 650, 363.3, 460, 460, 460, 460, 436.6, 650, 436.6, 650, 510, 510, 510, 510, 650]
    coordenadas4 = [460, 436.6, 460, 340, 436.6, 340, 436.6, 150, 510, 150, 510, 290, 650, 290, 650, 436.6]

    canva.create_polygon(coordenadas1, outline='black', fill='#4682B4')
    canva.create_polygon(coordenadas2, outline='black', fill='#50C878')
    canva.create_polygon(coordenadas3, outline='black', fill='#FFFFCC')
    canva.create_polygon(coordenadas4, outline='black', fill='#FF6666')
    dibujar_malla(canva, 7, 3, 220, 140, 290, 150)
    dibujar_malla(canva, 3, 7, 140, 220, 150, 290)
    dibujar_malla(canva, 3, 7, 140, 220, 510, 290)
    dibujar_malla(canva, 7, 3, 220, 140, 290, 510)
    dibujar_lineas_extra(canva)

    coords = [340, 340, 400, 400, 460, 340]
    coords1 = [340, 340, 400, 400, 340, 460]
    coords2 = [340, 460, 400, 400, 460, 460]
    coords3 = [460, 460, 400, 400, 460, 340]

    canva.create_polygon(coords, outline='black', fill='#4682B4', width=1)
    canva.create_polygon(coords1, outline='black', fill='#50C878', width=1)
    canva.create_polygon(coords2, outline='black', fill='#FFFFCC', width=1)
    canva.create_polygon(coords3, outline='black', fill='#FF6666', width=1)
    
    canva.create_text(328, 240, text='Salida', font=('Helvetica', 12), fill='black')
    canva.create_text(475, 561, text='Salida', font=('Helvetica', 12), fill='black')
    canva.create_text(475, 239, text='Seguro', font=('Helvetica', 12), fill='black')
    canva.create_text(400, 159, text='Seguro', font=('Helvetica', 12), fill='black')
    canva.create_text(403, 639, text='Seguro', font=('Helvetica', 12), fill='black')
    canva.create_text(330, 559, text='Seguro', font=('Helvetica', 12), fill='black')
    canva.create_text(240, 475, text='Seguro', font=('Helvetica', 12), fill='black', angle=270)
    canva.create_text(240, 330, text='Seguro', font=('Helvetica', 12), fill='black', angle=270)
    canva.create_text(160, 400, text='Seguro', font=('Helvetica', 12), fill='black', angle=270)
    canva.create_text(640, 400, text='Seguro', font=('Helvetica', 12), fill='black', angle=90)
    canva.create_text(560, 475, text='Seguro', font=('Helvetica', 12), fill='black', angle=90)
    canva.create_text(560, 330, text='Salida', font=('Helvetica', 12), fill='black', angle=90)
    canva.create_text(440, 400, text='Llegada', font=('Helvetica', 12), fill='black', angle=90)
    canva.create_text(360, 400, text='Llegada', font=('Helvetica', 12), fill='black', angle=270)
    canva.create_text(400, 440, text='Llegada', font=('Helvetica', 12), fill='black')
    canva.create_text(400, 360, text='Llegada', font=('Helvetica', 12), fill='black', angle=360)
    
    if num_jugadores == 2:
        
        cir_j1_1 = canva.create_oval(192.5, 192.5, 212.5, 212.5, outline='black', fill='lightblue', width=2)
        cir_j1_2 = canva.create_oval(227.5, 192.5, 247.5, 212.5, outline='black', fill='lightblue', width=2)
        cir_j1_3 = canva.create_oval(192.5, 227.5, 212.5, 247.5, outline='black', fill='lightblue', width=2)
        cir_j1_4 = canva.create_oval(227.5, 227.5, 247.5, 247.5, outline='black', fill='lightblue', width=2)
       
        cir_j2_1 = canva.create_oval(552.5, 192.5, 572.5, 212.5, outline='black', fill='#FF6666', width=2)
        cir_j2_2 = canva.create_oval(587.5, 192.5, 607.5, 212.5, outline='black', fill='#FF6666', width=2)
        cir_j2_3 = canva.create_oval(552.5, 227.5, 572.5, 247.5, outline='black', fill='#FF6666', width=2)
        cir_j2_4 = canva.create_oval(587.5, 227.5, 607.5, 247.5, outline='black', fill='#FF6666', width=2)
    
        canva.tag_bind(cir_j1_1, '<Button-1>', lambda e: click_ficha(e, cir_j1_1))
        canva.tag_bind(cir_j1_2, '<Button-1>', lambda e: click_ficha(e, cir_j1_2))
        canva.tag_bind(cir_j1_3, '<Button-1>', lambda e: click_ficha(e, cir_j1_3))
        canva.tag_bind(cir_j1_4, '<Button-1>', lambda e: click_ficha(e, cir_j1_4))
        
        canva.tag_bind(cir_j2_1, '<Button-1>', lambda e: click_ficha(e, cir_j2_1))
        canva.tag_bind(cir_j2_2, '<Button-1>', lambda e: click_ficha(e, cir_j2_2))
        canva.tag_bind(cir_j2_3, '<Button-1>', lambda e: click_ficha(e, cir_j2_3))
        canva.tag_bind(cir_j2_4, '<Button-1>', lambda e: click_ficha(e, cir_j2_4))
    
        # Inicializar el sistema de turnos con el número de jugadores seleccionado
        sistema_turnos = SistemaTurnos(num_jugadores)
        
        # Crear el diccionario de fichas disponibles según el número de jugadores
        fichas_disponibles = {
            1: [cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4],
            2: [cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4]
        }
    
    elif num_jugadores == 3:
        global cir_j3_1, cir_j3_2, cir_j3_3, cir_j3_4
        
        cir_j1_1 = canva.create_oval(192.5, 192.5, 212.5, 212.5, outline='black', fill='lightblue', width=2)  # Círculo 1
        cir_j1_2 = canva.create_oval(227.5, 192.5, 247.5, 212.5, outline='black', fill='lightblue', width=2)  # Círculo 2
        cir_j1_3 = canva.create_oval(192.5, 227.5, 212.5, 247.5, outline='black', fill='lightblue', width=2)  # Círculo 3
        cir_j1_4 = canva.create_oval(227.5, 227.5, 247.5, 247.5, outline='black', fill='lightblue', width=2)  # Círculo 4
    
        cir_j2_1 = canva.create_oval(552.5, 192.5, 572.5, 212.5, outline='black', fill='#FF6666', width=2)  # Círculo 5
        cir_j2_2 = canva.create_oval(587.5, 192.5, 607.5, 212.5, outline='black', fill='#FF6666', width=2)  # Círculo 6
        cir_j2_3 = canva.create_oval(552.5, 227.5, 572.5, 247.5, outline='black', fill='#FF6666', width=2)  # Círculo 7
        cir_j2_4 = canva.create_oval(587.5, 227.5, 607.5, 247.5, outline='black', fill='#FF6666', width=2)  # Círculo 8
    
        cir_j3_1 = canva.create_oval(192.5, 552.5, 212.5, 572.5, outline='black', fill='#50C878', width=2)  # Círculo 1
        cir_j3_2 = canva.create_oval(227.5, 552.5, 247.5, 572.5, outline='black', fill='#50C878', width=2)  # Círculo 2
        cir_j3_3 = canva.create_oval(192.5, 587.5, 212.5, 607.5, outline='black', fill='#50C878', width=2)  # Círculo 3
        cir_j3_4 = canva.create_oval(227.5, 587.5, 247.5, 607.5, outline='black', fill='#50C878', width=2)  # Círculo 4
        
    
        canva.tag_bind(cir_j1_1, '<Button-1>', lambda e: click_ficha(e, cir_j1_1))
        canva.tag_bind(cir_j1_2, '<Button-1>', lambda e: click_ficha(e, cir_j1_2))
        canva.tag_bind(cir_j1_3, '<Button-1>', lambda e: click_ficha(e, cir_j1_3))
        canva.tag_bind(cir_j1_4, '<Button-1>', lambda e: click_ficha(e, cir_j1_4))
        
        canva.tag_bind(cir_j2_1, '<Button-1>', lambda e: click_ficha(e, cir_j2_1))
        canva.tag_bind(cir_j2_2, '<Button-1>', lambda e: click_ficha(e, cir_j2_2))
        canva.tag_bind(cir_j2_3, '<Button-1>', lambda e: click_ficha(e, cir_j2_3))
        canva.tag_bind(cir_j2_4, '<Button-1>', lambda e: click_ficha(e, cir_j2_4))
        
        canva.tag_bind(cir_j3_1, '<Button-1>', lambda e: click_ficha(e, cir_j3_1))
        canva.tag_bind(cir_j3_2, '<Button-1>', lambda e: click_ficha(e, cir_j3_2))
        canva.tag_bind(cir_j3_3, '<Button-1>', lambda e: click_ficha(e, cir_j3_3))
        canva.tag_bind(cir_j3_4, '<Button-1>', lambda e: click_ficha(e, cir_j3_4))
        
        # Crear el diccionario de fichas disponibles según el número de jugadores
        fichas_disponibles = {
            1: [cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4],
            2: [cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4],
            3: [cir_j3_1, cir_j3_2, cir_j3_3, cir_j3_4]
        }

        # Inicializar el sistema de turnos con el número de jugadores seleccionado
        sistema_turnos = SistemaTurnos(num_jugadores)
    
    if num_jugadores == 4:
        global cir_j4_1, cir_j4_2, cir_j4_3, cir_j4_4
        
        cir_j1_1 = canva.create_oval(192.5, 192.5, 212.5, 212.5, outline='black', fill='lightblue', width=2)  # Círculo 1
        cir_j1_2 = canva.create_oval(227.5, 192.5, 247.5, 212.5, outline='black', fill='lightblue', width=2)  # Círculo 2
        cir_j1_3 = canva.create_oval(192.5, 227.5, 212.5, 247.5, outline='black', fill='lightblue', width=2)  # Círculo 3
        cir_j1_4 = canva.create_oval(227.5, 227.5, 247.5, 247.5, outline='black', fill='lightblue', width=2)  # Círculo 4

        cir_j2_1 = canva.create_oval(552.5, 192.5, 572.5, 212.5, outline='black', fill='#FF6666', width=2)  # Círculo 5
        cir_j2_2 = canva.create_oval(587.5, 192.5, 607.5, 212.5, outline='black', fill='#FF6666', width=2)  # Círculo 6
        cir_j2_3 = canva.create_oval(552.5, 227.5, 572.5, 247.5, outline='black', fill='#FF6666', width=2)  # Círculo 7
        cir_j2_4 = canva.create_oval(587.5, 227.5, 607.5, 247.5, outline='black', fill='#FF6666', width=2)  # Círculo 8
    
        cir_j3_1 = canva.create_oval(192.5, 552.5, 212.5, 572.5, outline='black', fill='#50C878', width=2)  # Círculo 1
        cir_j3_2 = canva.create_oval(227.5, 552.5, 247.5, 572.5, outline='black', fill='#50C878', width=2)  # Círculo 2
        cir_j3_3 = canva.create_oval(192.5, 587.5, 212.5, 607.5, outline='black', fill='#50C878', width=2)  # Círculo 3
        cir_j3_4 = canva.create_oval(227.5, 587.5, 247.5, 607.5, outline='black', fill='#50C878', width=2)  # Círculo 4

        cir_j4_1 = canva.create_oval(552.5, 552.5, 572.5, 572.5, outline='black', fill='#FFFFCC', width=2)  # Círculo 1
        cir_j4_2 = canva.create_oval(587.5, 552.5, 607.5, 572.5, outline='black', fill='#FFFFCC', width=2)  # Círculo 2
        cir_j4_3 = canva.create_oval(552.5, 587.5, 572.5, 607.5, outline='black', fill='#FFFFCC', width=2)  # Círculo 3
        cir_j4_4 = canva.create_oval(587.5, 587.5, 607.5, 607.5, outline='black', fill='#FFFFCC', width=2)  # Círculo 4
        
        canva.tag_bind(cir_j1_1, '<Button-1>', lambda e: click_ficha(e, cir_j1_1))
        canva.tag_bind(cir_j1_2, '<Button-1>', lambda e: click_ficha(e, cir_j1_2))
        canva.tag_bind(cir_j1_3, '<Button-1>', lambda e: click_ficha(e, cir_j1_3))
        canva.tag_bind(cir_j1_4, '<Button-1>', lambda e: click_ficha(e, cir_j1_4))
        
        canva.tag_bind(cir_j2_1, '<Button-1>', lambda e: click_ficha(e, cir_j2_1))
        canva.tag_bind(cir_j2_2, '<Button-1>', lambda e: click_ficha(e, cir_j2_2))
        canva.tag_bind(cir_j2_3, '<Button-1>', lambda e: click_ficha(e, cir_j2_3))
        canva.tag_bind(cir_j2_4, '<Button-1>', lambda e: click_ficha(e, cir_j2_4))
        
        canva.tag_bind(cir_j3_1, '<Button-1>', lambda e: click_ficha(e, cir_j3_1))
        canva.tag_bind(cir_j3_2, '<Button-1>', lambda e: click_ficha(e, cir_j3_2))
        canva.tag_bind(cir_j3_3, '<Button-1>', lambda e: click_ficha(e, cir_j3_3))
        canva.tag_bind(cir_j3_4, '<Button-1>', lambda e: click_ficha(e, cir_j3_4))
        
        canva.tag_bind(cir_j4_1, '<Button-1>', lambda e: click_ficha(e, cir_j4_1))
        canva.tag_bind(cir_j4_2, '<Button-1>', lambda e: click_ficha(e, cir_j4_2))
        canva.tag_bind(cir_j4_3, '<Button-1>', lambda e: click_ficha(e, cir_j4_3))
        canva.tag_bind(cir_j4_4, '<Button-1>', lambda e: click_ficha(e, cir_j4_4))
        
        # Crear el diccionario de fichas disponibles según el número de jugadores
        fichas_disponibles = {
            1: [cir_j1_1, cir_j1_2, cir_j1_3, cir_j1_4],
            2: [cir_j2_1, cir_j2_2, cir_j2_3, cir_j2_4],
            3: [cir_j3_1, cir_j3_2, cir_j3_3, cir_j3_4],
            4: [cir_j4_1, cir_j4_2, cir_j4_3, cir_j4_4]
        }
        
        # Inicializar el sistema de turnos con el número de jugadores seleccionado
        sistema_turnos = SistemaTurnos(num_jugadores)
    
    # Inicializar las fichas en el sistema de turnos
    sistema_turnos.inicializar_fichas(fichas_disponibles)
    
    # Crear etiqueta para mostrar el turno actual
    turno_label = Label(raiz, text=f'Turno: {sistema_turnos.obtener_jugador_actual()}', 
                       font=('Arial', 14))
    turno_label.pack()
    
    # Crear canvas y botones para los dados
    canvas1 = Canvas(raiz, width=50, height=50, borderwidth=2, relief='solid')
    canvas1.place(x=150, y=90)
    canvas2 = Canvas(raiz, width=50, height=50, borderwidth=2, relief='solid')
    canvas2.place(x=220, y=90)
    
    boton1 = Button(raiz, text='Tirar 1', command=lambda: tirar_dados(1), width=10, height=2)
    boton1.place(x=150, y=40)
    
    raiz.mainloop()


main()
