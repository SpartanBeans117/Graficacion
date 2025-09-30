"""En esta practica haremos que nuestro codigo de python cargue
un archivo en el que estara adentro una matriz de 100x100
que tendra 100 filas de 100 digitos del 0 al 9, cada
digito sera un color que turtle usara para dibujar en la pantalla
el archivo se creara en el mismo programa se llamara "matriz_100x100.txt" y
python lo tendra que ejecutar para asi dibujar la matriz
"""

import turtle
#turtle para dibujar la matriz
import random
#random para generar el contenido del archivo de texto


#creamos la tortuga
#le pondre bean para evitar errores con pylint
bean= turtle.Turtle()
#hicimos esta variable pantalla porque tracer no puede ser usado
#como objeto porque esto es parte de la ventana
PANTALLA = turtle.Screen()

#Aqui se asigna un color a cada numero
colores = {
    '0': 'white',
    '1': 'black',
    '2': 'red',
    '3': 'green',
    '4': 'blue',
    '5': 'yellow',
    '6': 'purple',
    '7': 'orange',
    '8': 'cyan',
    '9': 'magenta'
}

def generar_matriz_txt(nombre_archivo):
    """Genera una matriz de 100x100 con numeros del 0 al 9 y la guarda en un archivo de texto."""
    with open(nombre_archivo, "w") as archivo:#w es para generar la matriz
        for _ in range(100):
            fila = ''.join(str(random.randint(0, 9)) for _ in range(100))
            archivo.write(fila + '\n')

def cargar_matriz_desde_txt(nombre_archivo):
    """Carga la matriz desde un archivo de texto y la convierte en una lista de listas."""
    matriz = []
    with open(nombre_archivo, "r") as archivo: #r es para cargar el archivo
        for linea in archivo:
            fila = list(linea.strip())
            if len(fila) == 100:
                matriz.append(fila)
    return matriz

def pintar_matriz(matriz_dibujo):
    """Aqui se pinta la matriz con turtle"""
    bean.speed(0)#se modifica la velocidad para que este lo haga rapido
    bean.hideturtle()#oculta la tortuga
    bean.penup()#levanta la tortuga para no arrastrar el pincel
    PANTALLA.tracer(0, 0)#quita la animacion para mejorar la velocidad
    tamano_pixel = 5#le da tamaño al pixel que dibujara la tortuga
    inicio_x = -250#cordenada donde iniciara la tortuga en x
    inicio_y = 250#cordenada donde iniciara la tortuga en y

#aqui se mira la matriz fila por fila
    for y in range(100):
        for x in range(100):
            valor = matriz_dibujo[y][x]#obtiene los valores de la posicion x y y
            color = colores.get(valor, 'gray')
            #busca el color correspondiente a
            #cada numero, si no lo encuentra pintara
            #como predeterminado gris
            x_pos = inicio_x + x * tamano_pixel
            y_pos = inicio_y - y * tamano_pixel
            bean.goto(x_pos, y_pos)
            #goto se usa para posicionar la tortuga en un lugar especifico
            bean.dot(tamano_pixel, color)
            #se dibuja un pixel en la posicion que se calculo

    PANTALLA.update()
    #actualiza la pantalla para mostrar los puntos
    turtle.done()
    #se finaliza el codigo cuando se cierra la ventana
archivo_matriz = "matriz_100x100.txt"
#aqui se le genera el nombre al archivo donde se aloja la matriz
#aqui se llaman la funciones
generar_matriz_txt(archivo_matriz)#crear el archivo
matriz_cargada = cargar_matriz_desde_txt(archivo_matriz)  #leer el archivo
pintar_matriz(matriz_cargada)#dibujar la matriz
