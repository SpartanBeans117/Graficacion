"""En esta practica crearemos un programa de python donde este mismo ejecutara un archivo .txt
como si fueran las intrucciones para dibujar algo, lo que dibujara seran las figuras de la
practica uno, lo que haremos en este programa es que haremos que la tortuga identifique
cada una de las instrucciones del archivo de texto y lo dibuje, este programa aparte
de dibujar las figuras tambien comentara en la consola si hubo un error al interpretar
las instrucciones"""

#Este programa fue hecho en la version de python 3.10.11
#Se utilizo la ayuda de IA, la IA que se utilizo fue Copilot

import turtle#Importamos la libreria turtle para que dibuje las intrucciones
import os#Usamos os para interactuar con el sistema operativo

#Configura la ventana y la tortuga
PANTALLA = turtle.Screen()#se crea la pantalla
PANTALLA.setup(width=600, height=600)#se configura la pantalla para que sea 600x600
bean = turtle.Turtle()#Se crea la tortuga

def dibujar(linea):
    """Esta funcion es para que turtle pueda identificar cada
linea y la pueda dibujar en la pantalla"""
    linea = linea.strip()
    #cambia el color del lapiz
    if linea.startswith("pencolor("):
        #startswith sirve para verificar si una cadena comienza con un texto específico
        color = linea[len("pencolor("):-1].strip('"')
        bean.pencolor(color)
    #Mueve la tortuga hacia delante
    elif linea.startswith("forward("):
        #startswith sirve para verificar si una cadena comienza con un texto específico
        distancia = int(linea[len("forward("):-1])
        bean.forward(distancia)
    #Mueve la tortuga hacia atras
    elif linea.startswith("backward("):
        #startswith sirve para verificar si una cadena comienza con un texto específico
        distancia = int(linea[len("backward("):-1])
        bean.backward(distancia)
    #Gira la tortuga a la izquierda
    elif linea.startswith("left("):
        #startswith sirve para verificar si una cadena comienza con un texto específico
        angulo = int(linea[len("left("):-1])
        bean.left(angulo)
    #gira la tortuga a la derecha
    elif linea.startswith("right("):
        #startswith sirve para verificar si una cadena comienza con un texto específico
        angulo = int(linea[len("right("):-1])
        bean.right(angulo)
    #levanta el lapiz
    elif linea == "penup()":
        bean.penup()
    #baja el lapiz
    elif linea == "pendown()":
        bean.pendown()
    #mueve la tortuga a una posicion especifica
    elif linea.startswith("goto("):
        #startswith sirve para verificar si una cadena comienza con un texto específico
        coords = linea[len("goto("):-1].split(",")
        x = int(coords[0].strip())
        y = int(coords[1].strip())
        bean.goto(x, y)
    elif linea.startswith("repeat "):
        #Todo esto es para hacer que turtle lea las instrucciones de como hacer el circulo
        #startswith sirve para verificar si una cadena comienza con un texto específico
        partes = linea[len("repeat "):].rsplit(" ", 1)
        instrucciones = partes[0].strip()
        veces = int(partes[1])
        for _ in range(veces):
            for instruccion in instrucciones.split():
                if instruccion.startswith("forward("):
                    #startswith sirve para verificar si una cadena comienza con un texto específico
                    distancia = int(instruccion[len("forward("):-1])
                    bean.forward(distancia)
                elif instruccion.startswith("right("):
                    #startswith sirve para verificar si una cadena comienza con un texto específico
                    angulo = int(instruccion[len("right("):-1])
                    bean.right(angulo)
    else:#Si no coincide los datos marcara error
        raise ValueError(f"dato desconocido: {linea}")

#Esta linea de codigo asegura que el archivo de las instrucciones
#se encuente en la misma carpeta y asi evitar errores
ruta = os.path.join(os.path.dirname(__file__), "dibujante.txt")

with open(ruta, "r") as archivo:  # se usa para cargar el archivo
    for numero, linea in enumerate(archivo, start=1):
        if linea.strip():  # ignora lineas vacías
            print(f"Ejecutando {numero}: {linea.strip()}")
            #muestra que si se estan ejecutando las lineas
            try:
                dibujar(linea)
            except Exception as e: #sirve para capturar errores que ocurren dentro del bloque
                #y poder avisar de este error y en que linea fue
                print(f"Error linea {numero}: '{linea.strip()}' no es valida: {e}")

PANTALLA.mainloop() #mantiene la ventena
