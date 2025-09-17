import turtle
#Para esta practica tenemos que hacer que la digura se mueva en diferentes
#direcciones, como en turtle no hay una forma de mover el dibujo como tal,
#tendremos que simular el movimiento, haciendo que el dibujo se elimina para
#aparecer en un lugar diferente a la que tiene originalmente sumando la
#cordenada anterior

#Se uso python 3.10.11

tortubean= turtle.Turtle()
#speed lo usamos para que la tortuga dibuje mas rapido"""
tortubean.speed(0)
#hideturtle lo usamos para hacer que la tortuga sea invisible"""
tortubean.hideturtle()

#son las cordenadas que se usaran para simular el movimiento"""
POS_X = 0
POS_Y = 0

#Esta funcion generara el cuadrado
def bean():
    """crea el cuadrado"""
    #clear lo usamos para eliminar la figura"""
    tortubean.clear()
    #penup lo usamos para que la tortuga no dibuje"""
    tortubean.penup()
    #goto lo usamos para mover la tortuga en una cordenada especifica"""
    tortubean.goto(POS_X, POS_Y)
    #pendown lo usamos para hacer que la tortuga dibuje"""
    tortubean.pendown()
    #Estas lineas crean el cuadrado"""
    for _ in range(4):
        tortubean.forward(100)
        tortubean.right(90)

#ahora hacemos las funciones para simular el movimiento de la tortuga

def arriba():
    """mueve la figura hacia arriba"""
    #global llama a la variable que esta afuera de la funcion"""
    global POS_Y
    #aqui se suma 20 a la cordenada y"""
    POS_Y += 20
    #Bean llama a la funcion para hacer la figura"""
    bean()

def abajo():
    """mueve la figura hacia abajo"""
    #global llama a la variable que esta afuera de la funcion"""
    global POS_Y
    #aqui se suma 20 a la cordenada y"""
    POS_Y -= 20
    #Bean llama a la funcion para hacer la figura"""
    bean()

def izquierda():
    """Mueve la figuara a la izquierda"""
    #global llama a la variable que esta afuera de la funcion"""
    global POS_X
    #aqui se suma 20 a la cordenada x"""
    POS_X -= 20
    #Bean llama a la funcion para hacer la figura"""
    bean()

def derecha():
    """Mueve la figura hacia la derecha"""
    #global llama a la variable que esta afuera de la funcion"""
    global POS_X
    #aqui se suma 20 a la cordenada x"""
    POS_X += 20
    #Bean llama a la funcion para hacer la figura"""
    bean()

bean()


VENTANA_B = turtle.Screen()
#Creamos una ventana"""
#listen es para que la ventana sepa que vas a precionar tecla"""
VENTANA_B.listen()
#onkey es para asignar una función a una tecla específica del teclado"""
VENTANA_B.onkey(arriba, "Up")
VENTANA_B.onkey(abajo, "Down")
VENTANA_B.onkey(izquierda, "Left")
VENTANA_B.onkey(derecha, "Right")
#mainloop para que no se cierre la ventana
VENTANA_B.mainloop()
