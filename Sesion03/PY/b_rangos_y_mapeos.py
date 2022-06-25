#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Centro de Cultura Digital
Técnicas de composición asistida por datos // i.n.t.e.r.s.p.e.c.i.f.i.c.s
Sesion 03 / 05 
B: ranges and mappings
------------------------------------------------------------------------------------
"""


# data types
#integer:    valores enteros, positivos y negativos
#float:      valores de punto flotante (decimal, fracción, científico)
#boolean:    valores lógicos (True, False)



# ranges
"""
int:    acotado [0, 100]
float:  acotado [0.00, 100.00]
float:  normalizado[0.0, 1.0]
boolean: [True, False]
"""




# los datos tienen distintos rangos:

# tiempo (años)
#   x_min = 1993.0659
#   x_max = 2022.1416
#   #rango_x = x_max-x_min = 29.0757

# nivel del mar (mm)
#   y_min = 0
#   y_max = 100.8
#    #rango_y = 100.8

# cambio en nivel del mar (mm)
#   delta_y_min = -1.19
#   delya_y_max =  1.5
#   #rango_delta_y = 2.69


#rango de entrada:  rango de valores originales (0 - 100.8)
#rango de salida:   rango de valores deseados   (20 - 440)






# mapping function
def pmap(value, inMin, inMax, outMin, outMax, clamp=True):
    """ like processing's map """
    inSpan = inMax - inMin
    outSpan = outMax - outMin
    if (clamp):
        if (value<inMin): value = inMin
        if (value>inMax): value = inMax
    try:
        transVal = float(value - inMin) / float(inSpan)
        return outMin + (transVal * outSpan)
    except:
        return 0

#



a = pmap(7.5, 0, 100.8, 20, 440, False)