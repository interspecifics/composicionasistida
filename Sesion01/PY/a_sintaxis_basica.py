"""
Centro de Cultura Digital
Técnicas de composición asistida por datos 
Sesion 01 / 05
------------------------------------------------------------------------------------

Este script contiene instrucciones que pueden ser copiados a la consola
de python y no ha sido planeado para ser ejecutado necesariamente de modo secuencial.
"""

# ------------------------------------------------- < - >
# 01 sintaxis básica
# una variable es el nombre que le damos a una unidad de información
# puede ser de distintos tipos: valores numéricos, textuales o lógicos
# pero tambien listas, diccionarios o tablas

x = 640
height = 480
contador = 0
variable_txt = 'Un mensaje'
is_running = False

lista_datos = [90, 127, 121, 83, 12]
dicci = {'uno':1, 'dos':2, 'tres':3, 'cuatro':4}



# ------------------------------------------------- < - >
# 02 operaciones
# variables y valores constantes se pueden usar en operaciones algebraicas
# o almacenar en otras variables para uso posterior

suma = 30 + 210
var1 = (x - suma) / 50
contador = contador + 1

p1 = "fragmento de texto "
p2 = "del mensaje"
p3 = p1 + p2

on = True
off = False
uno_u_otro = on or off
uno_y_otro = on and off

lista_a = lista_datos + [31, 32, 46, 23]
lista_b = lista_a + 10



# ------------------------------------------------- < - >
# 03 metodos y operaciones con listas
# las estructuras de datos como las listas tienen una conjunto de instrucciones 
# asociadas a operaciones internas como llamar valores, añadir, insertar o borrar

lista_datos = [50, 60, 70, 80, 90]
lista_auxiliar = [1010, 2020, 3030, 8080]
# indexado, llamar al elemento en cierta posición
val_1 = lista_datos[0]
# añadir valores 
lista_datos.append(100)
# extender lista 
lista_datos.extend([110, 180, 200])
# insertar en cierta posición
lista_datos.insert(2, 65)
# remover elemento (s)
lista_datos.remove(100)
# concatenar dos listas
nueva_lista = lista_datos + lista_auxiliar
# seleccionar algunos elementos de la lista
mini_lista = nueva_lista[2:5]
mini_lista = nueva_lista[4:]
mini_lista = nueva_lista[:6]


# ------------------------------------------------- < - >
# 04 operaciones de entrada y salida de datos

# leer lista de archivo con un valor por línea
nom_archivo = "lista_de_datos.txt"
fi = open(nom_archivo, 'rt')
vals = fi.readlines()
vals = [int(v) for v in vals.strip()]
print("número de valores en la lista: ", len(vals))

# imprimir la lista:
print ("La lista de valores del archivo es:")
print ("-----------------------------------")
for v in vals:
    print(v)

# imprimir la lista numerada:
print ("La lista de valores del archivo es:")
print ("-----------------------------------")
for i,v in enumerate(vals):
    print(v)

# imprimir la lista otra vez usando los indices:
print ("La lista de valores del archivo es:")
print ("-----------------------------------")
for i in range(len(vals)):
    print(vals[i])


# leer archivo de datos con más de un valor por línea
nom_archivo = "tabla_de_datos.txt"
fi = open(nom_archivo, 'rt')
tabla = []
lines = fi.readlines()
for l in lines:
    row = [v for v in l.strip().split(',')]
    tabla.append(row)
print("número de filas en la tabla: ", len(tabla))
print("numero de columnas por fila:", len(row))

# imprimir la tabla:
print ("La tabla del archivo es:")
print ("------------------------")
for row in tabla:
    for col in row:
        print(col, '\t', end=''), 
    print('')
print ('------------------------')
# ejercicio encontrar indices de los elementos de una tabla