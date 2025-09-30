En esta practica hicimos un archivo de python con el objetivo de que esta misma cree un archivo y tambien lo cargue
para que turtle pueda leerlo y dibujarlo en una ventana.

El programa se hizo en Python 3.10.11

Antes de hacer todo, importamos las librerias que vamos a utilizar, usaremos turtle para dibujar la matriz
y random para ayudarnos a generar una matriz sin complicarnos
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import turtle
#turtle para dibujar la matriz
import random
#random para generar el contenido del archivo de texto
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Hicimos la tortuga la cual le pusimos bean y la pantalla
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#creamos la tortuga
#le pondre bean para evitar errores con pylint
bean= turtle.Turtle()
#hicimos esta variable pantalla porque tracer no puede ser usado
#como objeto porque esto es parte de la ventana
PANTALLA = turtle.Screen()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Le asignamos a los numeros de 0 al 9 los colores
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Tuvimos que definir estas variables para crear y cargar el archivo:
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Definimos una variable para que turtle dibuje la matriz, tuvimos que modificar la tortuga para que esta pueda
dibujar rapido y sin problemas y a la ves esta funcion escribe en el texto haciendo que cada vez que ejecutes el codigo genere un archivo con codigos diferentes 
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Estas lineas de codigo hacen que se actualice la ventana y que se pueda cerrar
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
PANTALLA.update()
    #actualiza la pantalla para mostrar los puntos
    turtle.done()
    #se finaliza el codigo cuando se cierra la ventana
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

En esta linea se le pone nombre al archivo de la matriz
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
archivo_matriz = "matriz_100x100.txt"
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Llamamos las funciones que nos ayudaran a crear, ejecutar y dibujar la matriz
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#aqui se llaman la funciones
generar_matriz_txt(archivo_matriz)#crear el archivo
matriz_cargada = cargar_matriz_desde_txt(archivo_matriz)  #leer el archivo
pintar_matriz(matriz_cargada)#dibujar la matriz
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Ya comprobe que si carga el archivo .txt el cual se debe llamar "matriz_100x100.txt", siempre y cuando se llame
asi el programa podra ejecutarlo y dibujarlo, se puede comprobar si primero generas el archivo "matriz_100x100.txt"
y borras la siguiente linea de codigo que se encuentra en la linea 85
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
generar_matriz_txt(archivo_matriz)#crear el archivo
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
