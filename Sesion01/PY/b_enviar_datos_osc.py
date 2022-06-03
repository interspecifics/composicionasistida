"""
Centro de Cultura Digital
Técnicas de composición asistida por datos 
Sesion 01 / 05
------------------------------------------------------------------------------------

Este script contiene instrucciones que pueden ser copiados a la consola
de python y no ha sido planeado para ser ejecutado necesariamente de modo secuencial.
"""


from oscpy.client import OSCClient
from time import sleep

# setup osc connection
OSC_HOST = "127.0.0.1"
OSC_PORT = 8002
OSC_CLIENT = OSCClient(OSC_HOST, OSC_PORT)

def send_osc(list_data):
    #current data must be a list of FFT components
    ruta = "/data".encode()
    OSC_CLIENT.send_message(ruta, list_data)
    #print('sending', ruta)
    return


# leer archivo:
nom_archivo = "REFS/trayectoria_huracan_elsa_2021.txt"
fi = open(nom_archivo, 'rt')
tabla = []
lines = fi.readlines()
for l in lines:
    row = [v for v in l.strip().split(',')]
    tabla.append(row)
print("número de filas en la tabla: ", len(tabla))
print("numero de columnas por fila:", len(row))
# imprime archivo
print ("La tabla del archivo es:")
print ("------------------------")
for row in tabla:
    for col in row:
        print(col, '\t', end=''), 
    print('')
print ('------------------------')



# loop -------- >
i = 0
while (True):
    in_line = tabla[i]
    values = [0,0,0,0,0]
    try:
        values = [i, float(in_line[1]), float(in_line[2]), int(in_line[3]), int(in_line[4])]
    except:
        i=i+1
        continue
    # envia aqui
    send_osc(values)
    print(">> ", values)
    # incrementa el indice
    if i<(len(tabla)-1):
        i = i+1
    else: 
        i = 0
    sleep(0.1)

        # aa = buff_m[freq_index]
println("[-_-] exit status: 0")

