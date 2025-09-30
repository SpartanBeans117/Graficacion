#Este programa fue hecho en la version de python 3.10.11
#Se utilizo la ayuda de IA, la IA que se utilizo fue Copilot

Buenas tardes, en esta practica se hizo un programa para hacer que turtle siga y pueda entender
las instrucciones que estaran en un archivo de texto llamado "dibujante.txt", dentro de esta misma
estaran todas las intrucciones que seguira turtle para poder dibujar lo que se pide ahi dentro.

Lo que se dibujara son las figuras que vimos en la practica 1, las cuales son un cuadrado,
triangulo, linea y un circulo

Para hacer todo esto tuvimos que buscar las instrucciones que usamos para hacer que la tortuga
dibuje las figuras y modificaralas para que turtle las pueda entender mejor, para que turtle
pueda leer estas instrucciones tuvimos que usar ".startswith" que sirve para verificar si una cadena comienza con
un texto específico, como goto( para cambiar la posicion de la tortuga, entoces si lee esto
se ejecutara todo este bloque de codigo:

elif linea.startswith("goto("):
        #startswith sirve para verificar si una cadena comienza con un texto específico
        coords = linea[len("goto("):-1].split(",")
        x = int(coords[0].strip())
        y = int(coords[1].strip())
        bean.goto(x, y)


Para hacer que el programa pueda encontrar el archivo .txt tuvimos que importar la libreria llamada os
que nos ayuda a interactuar con el sistema operativo, escribimos estas lineas de codigo para
hacer que el programa busque el archivo en la misma carpeta donde se encuentra el codigo .py

#Esta linea de codigo asegura que el archivo de las instrucciones
#se encuentre en la misma carpeta y asi evitar errores
ruta = os.path.join(os.path.dirname(__file__), "dibujante.txt")

Para que el programa cargue el archivo utilizamos estas lineas de codigo para que busque en la carpeta el archivo
.txt, y este mismo lo corra usando la variable ruta que anteriormente comentamos

with open(ruta, "r") as archivo:  # se usa para cargar el archivo
    for numero, linea in enumerate(archivo, start=1):
        if linea.strip():  # ignora lineas vacías
            print(f"Ejecutando {numero}: {linea.strip()}")#muestra que si se estan ejecutando las lineas
            try:
                dibujar(linea)
            except Exception as e: #sirve para capturar errores que ocurren dentro del bloque
                #y poder avisar de este error y en que linea fue
                print(f"Error linea {numero}: '{linea.strip()}' no es valida: {e}")

De paso tambien pusimos este codigo para cuando algo no se escribiera bien en las instrucciones nos mande en la
consola en que linea de las instrucciones hubo un error y tambien que despues de señalizar donde fue el error, esta
esta todavia siga dibujando saltandose la linea en la que estuvo el error

try:
                dibujar(linea)
            except Exception as e: #sirve para capturar errores que ocurren dentro del bloque
                #y poder avisar de este error y en que linea fue
                print(f"Error linea {numero}: '{linea.strip()}' no es valida: {e}")