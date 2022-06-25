#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Centro de Cultura Digital
Técnicas de composición asistida por datos // i.n.t.e.r.s.p.e.c.i.f.i.c.s
Sesion 03 / 05 
A: scrapping data from online plots
------------------------------------------------------------------------------------
"""


import requests
from bs4 import BeautifulSoup
import xmltojson
import json


# descarga la página, almacena en page
url = "https://climate.nasa.gov/vital-signs/sea-level/"
page = requests.get(url)
print(page.content)




# encuentra el campo específico
data=[]
soup = BeautifulSoup(page.content, 'html5lib')

minisoup = soup.find('div', attrs = {'data-react-class':'FlotLineChart'})
print (minisoup.text)

#get the specific attribute
minisoup.attrs.keys()
the_data = minisoup.attrs['data-react-props']

#deserialize object
obj_data = json.loads(the_data)
obj_data.keys()
obj_data['chart'].keys()
len(obj_data['items'])

# then save as json:
json.dump(obj_data, open('sea_levels.json','w+'))


#explore...


"""
table = []
for i in range(2,len(obj_data['items'])):
	l = [
		obj_data['items'][i]['x'],
		obj_data['items'][i]['y'],
		float(obj_data['items'][i]['x']) - float(obj_data['items'][i-1]['x']),
		float(obj_data['items'][i]['y'])-float(obj_data['items'][i-1]['y'])
		]
	table.append(l)

"""