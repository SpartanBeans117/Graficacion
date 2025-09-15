En la práctica de hoy aprendimos sobre el módulo turtle, que nos da varias herramientas para dibujar en la pantalla y usamos estas herramientas para hacer un cuadrado, triángulo, círculo y una línea recta.

Lo primero que hicimos es importar la librería turtle y crear la tortuga, la tortuga se llama, “tortubean”
import turtle
tortubean= turtle.Turtle()

Usamos esta linea para que la ventana no se cierre cuando se termine de ejecutar el codigo
turtle.mainloop()

Para hacer el cuadrado, hicimos una función llamada:
def tortugacuadrada(tortubean):

Para que dibuje el cuadrado usamos estas lineas de codigo:
1- Elegimos un color (esto lo hacemos por que en las instrucciones de la práctica lo piden)
tortubean.pencolor("purple")#cambia el color
2- Escribimos esta linea que hace que la tortuga dibuje, (siempre el angulo con el que inicia es a la derecha)
tortubean.forward(100)#distancia del dibujado
3- Escribimos este código para que la tortuga cambie de ángulo para que cuando pongamos el código anterior dibuje hacia otra dirección
tortubean.right(90)#Angulo donde dibujara la tortuga

Tienes que repetirlo 4 veces, te tiene que quedar así:
def tortugacuadrada(tortubean):
    tortubean.pencolor("purple")#cambia el color
    tortubean.forward(100)#distancia del dibujado
    tortubean.right(90)#Angulo donde dibujara la tortuga
    tortubean.forward(100)#distancia del dibujado
    tortubean.right(90)#Angulo donde dibujara la tortuga
    tortubean.forward(100)#distancia del dibujado
    tortubean.right(90)#Angulo donde dibujara la tortuga
    tortubean.forward(100)#distancia del dibujado
    tortubean.right(90)#Angulo donde dibujara la tortuga

Recuerda llamar a la función para que se ejecute el código
tortugacuadrada(tortubean)#llama la funcion

Para hacer el triangulo, hicimos una función llamada:
def tortutriangulo(tortubean):
Como ahora queremos dibujar un triangulo necesitaremos acambiarlo de posicion para que no dibuje encima del cuadrado, vamos a usar 3 lineas de codigo nuevas las cuales son
    tortubean.penup()#Levanta la pluma para que no pinte
    tortubean.goto(50, 100) #Cambia de posicion
    tortubean.pendown()#empieza a dibujar

Despues de esto vamos a utilizar un color diferente:
tortubean.pencolor("red")#cambia el color
y ahora empezaremos a dibujar el triangulo
tortubean.forward(100)#distancia del dibujado
para cambiar el angulo usaremos esta linea para que dibuje a la izquierda, escribimos un angulo de 120 para que vaya agarrando forma el triangulo
tortubean.left(120)#Angulo donde dibujara la tortuga
Esto lo repetimos 3 veces, tiene que quedar asi
def tortutriangulo(tortubean):
    tortubean.penup()#Levanta la pluma para que no pinte
    tortubean.goto(50, 100) #Cambia de posicion
    tortubean.pendown()#empieza a dibujar
    tortubean.pencolor("red")#cambia el color
    tortubean.forward(100)#distancia del dibujado
    tortubean.left(120)#Angulo donde dibujara la tortuga
    tortubean.forward(100)#distancia del dibujado
    tortubean.left(120)#Angulo donde dibujara la tortuga
    tortubean.forward(100)#distancia del dibujado
    tortubean.left(120)#Angulo donde dibujara la tortuga

Llamamos la función
tortutriangulo(tortubean)#llama la funcion


Para hacer el circulo definimos una funcion
def tortucircle(tortubean):

Cambiamos de posición la tortuga para que dibuje el círculo y de paso le cambiamos el color
tortubean.penup()#Levanta la pluma para que no pinte
    tortubean.goto(-50, 100) #Cambia de posicion
    tortubean.pendown()#empieza a dibujar
    tortubean.pencolor("green")#cambia el color

Ahora para hacer el circulo tuvimos que recurrir a una linea que repetira el codigo varias veces hasta terminar el circulo, le cual es este
for _ in range(180):
        tortubean.forward(1)#distancia del dibujado
        tortubean.right(2)#Angulo donde dibujara la tortuga
       

Despues que se repita 180 veces el circulo estará terminado y lo que se esta repitiendo son los mismos codigos que usamos anteriormente solo que cambiamos la distancia y el angulo, para hallar las variable correctas hicimos varias pruebas.

El codigo para hacer el circulo deberia quedarte asi
def tortucircle(tortubean):
    tortubean.penup()#Levanta la pluma para que no pinte
    tortubean.goto(-50, 100) #Cambia de posicion
    tortubean.pendown()#empieza a dibujar
    tortubean.pencolor("green")#cambia el color
   
    for _ in range(180):
        tortubean.forward(1)#distancia del dibujado
        tortubean.right(2)#Angulo donde dibujara la tortuga
       
Recuerda llamarlo para que corra la funcion
tortucircle(tortubean)#llama la funcion



Para hacer la linea definimos una funcion
def tortuline(tortubean):

Cambiamos de posicion la tortuga
    tortubean.penup()#Levanta la pluma para que no pinte
    tortubean.goto(-50, -150) #Cambia de posicion
    tortubean.pendown()#empieza a dibujar

Cambiamos de color
tortubean.pencolor("blue")#cambia el color

Hicimos la linea
    tortubean.right(0)#Angulo donde dibujara la tortuga
    tortubean.forward(100)#distancia del dibujado

llamamos la funcion
tortuline(tortubean)#llama la funcion

y se termina la practica
