#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Centro de Cultura Digital
Técnicas de composición asistida por datos // i.n.t.e.r.s.p.e.c.i.f.i.c.s
Sesion 03 / 05 
C: more powerful dataserver
------------------------------------------------------------------------------------
"""

import pygame
import json
import statistics
from oscpy.client import OSCClient


#----------------------------- [osc]
OSC_HOST = "127.0.0.1"
OSC_PORT = 8000
OSC_CLIENT = []
#-----------------------------



#init
pygame.init()
DATA_PATH = "sea_levels.json"
FONT_PATH = "RevMiniPixel.ttf"

WIDTH = 600
HEIGHT = 300
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
ORANGE = (232,111,97)
BACKGROUND_COLOR = BLACK

# load stuff, like fonts
FONT = pygame.font.Font(FONT_PATH, 16)
FONTmini = pygame.font.Font(FONT_PATH, 14)

# main screen for drawing buttons
DRAW_SCREEN = pygame.Surface((WIDTH,HEIGHT))
DRAW_SCREEN.fill(BACKGROUND_COLOR)

# buttons
canales = ['time', 'level', 'delta_t', 'delta_l']
n_ch = len(canales)
botones_canal = [pygame.draw.rect(DRAW_SCREEN, GREEN, pygame.Rect(120+c*80, 100, 80, 50), 2) for c in range(n_ch)]
botones_norm =  [pygame.draw.rect(DRAW_SCREEN, BLUE, pygame.Rect(120+c*80, 150, 80, 20), 2) for c in range(n_ch)]
botones_logic = [pygame.draw.rect(DRAW_SCREEN, RED, pygame.Rect(120+c*80, 170, 80, 20), 2) for c in range(n_ch)]
labels_canal = [FONT.render(cs, 1, (0, 255, 0)) for cs in canales]

# timer events
TIC_EVENT = pygame.USEREVENT + 1
TIC_TIMER = 1000

#states and counters
clock = pygame.time.Clock()
actual_set = [0,0,0,0]
buffers = []
sws_canales = [False for c in range(n_ch)]
sws_norm = [False for c in range(n_ch)]
sws_logic = [False for c in range(n_ch)]
contadores = [0  for c in range(n_ch)]
pos = (0,0)
running = True
ii=0


# air
contaminantes = {}
fechas = []

# now
datatable = []
datalabels = []
vmins = [0,0,0,0]
vmaxs = [0,0,0,0]


#-osc
def init_osc(osc_host = OSC_HOST, osc_port = OSC_PORT):
	"""inicia el osc"""
	global OSC_CLIENT
	OSC_CLIENT = OSCClient(osc_host, osc_port)



def update_data_send(i=0):
	"""update the state of actual set and sends update"""
	global datatable, datalabels, fechas, OSC_CLIENT, actual_set
	print("\n\n[timetag]: ", fechas[i])
	actual_set = datatable[i] 
	print("actual_set:", actual_set)
	for k,dl in enumerate(datalabels):
		try:
			ruta = '/sealevels/{}'.format(dl).encode()
			if sws_canales[k]:
				vnorm = pmap(actual_set[k], vmins[k], vmaxs[k], 0, 1)
				if sws_logic[k]:
					lruta = '/sealevels/{}/bool'.format(dl).encode()
					if vnorm>0.5:
						OSC_CLIENT.send_message(lruta, [True])
						print("{} \t-\t{}\t{}".format(i, dl, True))
					else:
						OSC_CLIENT.send_message(lruta, [False])
						print("{} \t-\t{}\t{}".format(i, dl, False))
				if sws_norm[k]:
					OSC_CLIENT.send_message(ruta, [vnorm])
					print("{} \t-\t{}\t{}".format(i, dl, vnorm))
				else:
					OSC_CLIENT.send_message(ruta, [actual_set[k]])
					print("{} \t-\t{}\t{}".format(i, dl, actual_set[k]))
		except:
			print("X.X .... Bad DATA at {}".format(fechas[i]))


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


# -data stuff
def load_data():
	"""loads and parse json file containing data"""
	global datatable, datalabels, fechas
	# para acceder a los datos del archivo:
	c = 0
	json_data = json.load(open(DATA_PATH,'r+'))
	datatable = []
	datalabels = ['x','y', 'dx', 'dy']
	fechas = ["{}/{}/{}".format(it['year'],	it['month'], it['day']) for it in json_data['items'][2:]]
	for i in range(2, len(json_data['items'])):
		l = [
			float(json_data['items'][i]['x']),
			float(json_data['items'][i]['y']),
			float(json_data['items'][i]['x']) - float(json_data['items'][i-1]['x']),
			float(json_data['items'][i]['y']) - float(json_data['items'][i-1]['y'])
			]
		c+=1
		datatable.append(l)
	for i in range(len(datatable[0])):
		dd = [dt[i] for dt in datatable]
		vmins[i] = min(dd)
		vmaxs[i] = max(dd)
	print("minmaxs:", vmins, vmaxs)
	print ("[DATA]: {} records".format(c))



def isFloat(s):
	try:
		float(s)
		return True
	except ValueError:
		return False



# tic for the timer
def tic():
	global ii
	update_data_send(ii)
	ii = ii+1
	#print ("\t\t -->   Aqui ENVIA DATOS")
	return

# handle keys pressed
def handle_keys(event):
	global running
	if (event.key == pygame.K_q):
		running = False

# handlear eventos con un diccionario
def handle_events():
	event_dict = {
		pygame.QUIT: exit,
		pygame.KEYDOWN: handle_keys,
		TIC_EVENT: tic
		}
	for event in pygame.event.get():
		if event.type in event_dict:
			if (event.type==pygame.KEYDOWN):
				event_dict[event.type](event)
			else:
				event_dict[event.type]()
	return


# handlear clicks del mouse
def handle_mouse_clicks():
	global sws_canales, contadoress
	# check for mouse pos and click
	pos = pygame.mouse.get_pos()
	pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
	# Check collision between buttons and mouse1
	for j,b in enumerate(botones_canal):
		if (b.collidepoint(pos) and pressed1):
			sws_canales[j] = not (sws_canales[j])
			print("[click{}]!: ".format(j))
	# Check collision between buttons and mouse1
	for j,b in enumerate(botones_norm):
		if (b.collidepoint(pos) and pressed1):
			sws_norm[j] = not (sws_norm[j])
			print("[click{}]!: ".format(j))
	# Check collision between buttons and mouse1
	for j,b in enumerate(botones_logic):
		if (b.collidepoint(pos) and pressed1):
			sws_logic[j] = not (sws_logic[j])
			print("[click{}]!: ".format(j))
	return


# update labels and other text in display
def update_text():
	global labels_canal, actual_set
	WINDOW.blit(DRAW_SCREEN, (0, 0))
	AUX_LABEL = FONT.render('->DATASERVER_TCAD:  ', 1, (32, 48, 0))
	WINDOW.blit(AUX_LABEL, (100, 50))
	AUX_LABEL = FONT.render('[ DATA ] -mini-', 1, GREEN)
	WINDOW.blit(AUX_LABEL, (320, 50))
	for j in range(len(actual_set)):
		WINDOW.blit(labels_canal[j], (125+j*80, 104))
		#cambia el color on/off
		if sws_canales[j]:
			STA = FONTmini.render("{:0.2f}".format(actual_set[j]), 1, (0, 255, 0))
		else:
			STA = FONTmini.render("{:0.2f}".format(actual_set[j]), 1, (32,48, 0))
		WINDOW.blit(STA, (125+j*80, 134))

		#cambia el color norm
		if sws_norm[j]:
			NS = FONTmini.render("ON", 1, (0, 255, 0))
		else:
			NS = FONTmini.render("OFF", 1, (0,64,32))
		WINDOW.blit(NS, (125+j*80, 155))

		#cambia el color logic
		if sws_logic[j]:
			NL = FONTmini.render("ON", 1, (0, 255, 0))
		else:
			NL = FONTmini.render("OFF", 1, (0,64,32))
		WINDOW.blit(NL, (125+j*80, 175))


	UNT_LABEL = FONTmini.render("[step]:  {}".format(ii), 1, ORANGE)
	WINDOW.blit(UNT_LABEL, (100, 280))
	UNT_LABEL = FONTmini.render("[timetag]:  "+fechas[ii], 1, ORANGE)
	WINDOW.blit(UNT_LABEL, (320, 280))

	pygame.display.flip()





# the loop from outside
def game_loop():
	while running:
		handle_events()
		handle_mouse_clicks()
		update_text()
		clock.tick(9)

# the main (init+loop)
def main():
	pygame.display.set_caption('[ DATASERVER :: Taller de Composición Asistida ]')
	init_osc()
	load_data()
	pygame.time.set_timer(TIC_EVENT, TIC_TIMER)
	game_loop()
	print("FIN DE LA TRANSMISSION //...")

if __name__=="__main__":
	main()