# Tkinter: Versión jugable del clasico juego de mesa Parqués en Python
### Autores: Andrés Felipe Arévalo, Andrés Felipe Panche Garcia, Daniel Esteban Mendez Ramirez

¡Bienvenido al repositorio del clásico juego de Parqués implementado en Python! 
Este proyecto es una recreación digital del famoso juego de mesa, diseñado para ser jugado por 2 a 4 jugadores. 
Utiliza la librería Tkinter para crear una interfaz gráfica interactiva que permite a los usuarios disfrutar de una experiencia de juego fluida.

Esta versión jugable en python del popular juego de mesa fue desarrollado como proyecto final para el curso de Programación de Computadores de la Universidad Nacional Colombia.
El código fue desarrollado y probaaado en los interpretes de Python Spyder y Visual Studio Code
![Captura de pantalla 2025-02-25 112904](https://github.com/user-attachments/assets/03e6b76b-8d47-4a41-b95b-7e2ec2ea5cdc)

# ¿Cómo jugar?
## 1). Descarge y ejecute el código
Despues de ejecutar el código, se le solicitara ingresar el número de jugadores (1-4):
<img width="959" alt="image" src="https://github.com/user-attachments/assets/0334d33f-9346-4afe-9b8c-dad912dcd71b" />

## 2). Tire los dados y empice a jugar
Por defecto siempre iniciara el jugador 1, fichas azules (parte superior izquierda), seguido el jugador 2, fichas rojas (parte superior derecha), subsecuentemente el jugador 3, fichas verdes (parte inferior izquierda) y finalmente el jugador 4, fichas blancas (parte inferior derecha)
Nota: 
-	Las fichas solo salen al sacar 5, bien sea en un único dado o la suma de los valores sacados en los dados.
-	Si un jugador tiene todas las fichas en la cárcel y saca par no podrá volver a lanzar los dados, la lógica de dados pares se programo para funcionar n veces siempre y cuando l jugador tenga por lo menos una ficha fuera de la prisión.
-	En cada roda, al tirar los dados, el programa le indicara si puede salir de prisión y la cantidad de pasos que puede avanzar. 
![image](https://github.com/user-attachments/assets/411944e2-f848-4184-b92f-614f2ac5b977)

## 3). Aclaraciones sobre el movimiento de fichas
Al tirar los dados, seleccione y haga clic sobre la ficha que desea mover e indíquele a la consola el valor del dado que desea emplear. Es decir, si un jugador saco 5 y 3 en el lanzamiento de los dados y desea mover todos los valores con una única ficha, deberá primero hacer clic sobre la ficha e indicarle que mueva 5, darle enter y posteriormente darle clic nuevamente a la misma ficha e indicarle que mueva 3 y darle enter.
<img width="959" alt="image" src="https://github.com/user-attachments/assets/b5e687f4-7516-4292-a8b7-df32e3c4a9cf" />


