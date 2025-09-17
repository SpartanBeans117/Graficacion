"""Para esta practica tenemos que hacer que la digura se mueva en diferentes
direcciones, como en turtle no hay una forma de mover el dibujo como tal,
tendremos que simular el movimiento, haciendo que el dibujo se elimina para
aparecer en un lugar diferente a la que tiene originalmente sumando la
cordenada anterior"""

"""Se uso python 3.10.11"""

import turtle

tortubean= turtle.Turtle()
"""speed lo usamos para que la tortuga dibuje mas rapido"""
tortubean.speed(0)
"""hideturtle lo usamos para hacer que la tortuga sea invisible"""
tortubean.hideturtle()

"""son las cordenadas que se usaran para simular el movimiento"""
x = 0
y = 0

"""Esta funcion generara el cuadrado"""
def Bean(tortubean):
    """clear lo usamos para eliminar la figura"""
    tortubean.clear()
    """penup lo usamos para que la tortuga no dibuje"""
    tortubean.penup()
    """goto lo usamos para mover la tortuga en una cordenada especifica"""
    tortubean.goto(x, y)
    """pendown lo usamos para hacer que la tortuga dibuje"""
    tortubean.pendown()
    """Estas lineas crean el cuadrado"""
    for _ in range(4):
        tortubean.forward(100)
        tortubean.right(90)

"""ahora hacemos las funciones para simular el movimiento de la tortuga"""

def arriba():
    """global llama a la variable que esta afuera de la funcion"""
    global y
    """aqui se suma 20 a la cordenada y"""
    y += 20
    """Bean llama a la funcion para hacer la figura"""
    Bean(tortubean)

def abajo():
    
    global y
    y -= 20
    Bean(tortubean)

def izquierda():
    global x
    x -= 20
    Bean(tortubean)

def derecha():
    global x
    x += 20
    Bean(tortubean)

Bean(tortubean)

"""Creamos una ventana"""
ventanaB = turtle.Screen()
"""listen es para que la ventana sepa que vas a precionar tecla"""
ventanaB.listen()
"""onkey es para asignar una función a una tecla específica del teclado"""
ventanaB.onkey(arriba, "Up")
ventanaB.onkey(abajo, "Down")
ventanaB.onkey(izquierda, "Left")
ventanaB.onkey(derecha, "Right")
"""mainloop para que no se cierre la ventana"""
ventanaB.mainloop()