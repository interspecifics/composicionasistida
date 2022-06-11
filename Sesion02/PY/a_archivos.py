"""
Centro de Cultura Digital
Técnicas de composición asistida por datos 
Sesion 02 / 05
------------------------------------------------------------------------------------

Este script contiene bloques de instrucciones que pueden ser copiados a la consola
de python y no ha sido planeado para ser ejecutado necesariamente de modo secuencial.
"""



# ------------------------------------------------- < - >
# 01 operaciones de entrada y salida de datos

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