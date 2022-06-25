#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Centro de Cultura Digital
Técnicas de composición asistida por datos // i.n.t.e.r.s.p.e.c.i.f.i.c.s
Sesion 04 / 05 
C: Optical character recognition
------------------------------------------------------------------------------------
"""

#----------------------------- [modules]
from PIL import Image
import pytesseract
import numpy as np


#----------------------------- [extraction]

filename = 'tabla_metalfood.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)



