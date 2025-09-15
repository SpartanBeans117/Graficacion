import turtle
###Crea a la tortuguita###
tortubean= turtle.Turtle()

###Crea un cuadrado###
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

tortugacuadrada(tortubean)#llama la funcion

###Crea un triangulo###
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

tortutriangulo(tortubean)#llama la funcion

###Crea un circulo###
def tortucircle(tortubean):
    tortubean.penup()#Levanta la pluma para que no pinte
    tortubean.goto(-50, 100) #Cambia de posicion
    tortubean.pendown()#empieza a dibujar
    tortubean.pencolor("green")#cambia el color
    
    for _ in range(180):
        tortubean.forward(1)#distancia del dibujado
        tortubean.right(2)#Angulo donde dibujara la tortuga
        
tortucircle(tortubean)#llama la funcion

###Crea una linea###
def tortuline(tortubean):
    tortubean.penup()#Levanta la pluma para que no pinte
    tortubean.goto(-50, -150) #Cambia de posicion
    tortubean.pendown()#empieza a dibujar
    tortubean.pencolor("blue")#cambia el color
    tortubean.right(0)#Angulo donde dibujara la tortuga
    tortubean.forward(100)#distancia del dibujado
tortuline(tortubean)#llama la funcion

turtle.mainloop()
