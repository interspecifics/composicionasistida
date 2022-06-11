////////NO OLVIDAR///////////


Server.local.boot;  //bootear servidor local
s.boot; //s variable global para el servidor

s.meter; // despliega monitor de canales
s.volume.gui; // despiega un control general de volumen

//punto y coma al final de cada línea = enter (ejecutar/evaluar)

{SinOsc.ar}.play; //crear una función {} reusable bit of code

//command+punto parar sonido de emergencia

/// si no se pone ningún valor los valores son los predeterminados

{ SinOsc.ar(400, 0, 0,1) }.play; //ejemplo simple con argumentos básicos

//función en variable global
x = {SinOsc.ar}.play;
x.free;

y = {LFTri.ar}.play;
y.free;

//función con argumentos establecido en variable global
x = {SinOsc.ar(330.2,0,0.125,0)}.play;
x.free;

y = {LFTri.ar(540,0,0.125,0)}.play;
y.free;

~misinte = {LFTri.ar(540,0,0.125,0)}.play;
~misinte.free;

//shift+command+d en el objeto que quieras explorar para desplegar ayuda

//shift+command+p para limpiar la post window



////////DEMO DE LA FÍSICA DEL SONIDO/////////

{ SinOsc.ar (400,0,1,0) }.scope

{ LFTri.ar (320,0,1,0) }.play;

{ LFSaw.ar (320,0,1,0) }.play;

{ BrownNoise.ar(1) }.play;

{ WhiteNoise.ar(1) }.play;

{ PinkNoise.ar(1) }.play;

{ GrayNoise.ar(1) }.play;

{ ClipNoise.ar(0.1) }.play;



(
{ var freq;
    freq = [[660, 880], [440, 660], 1320, 880].choose;
    SinOsc.ar(freq, 0, 0.2);
}.play;
)


// cambiar valores en tiempo real
// declarar los propios argumentos y variable
(
z = {
arg freq=440, amp=1;
var sig;
	sig = SinOsc.ar(freq) * amp
}.play;
)
z.free;
z.set(\freq,320);
z.set(\amp,0.6);
z.set(\freq,660, \amp,1);
// no importa el orden en que fueron declarados
// las variables pueden ser declaradas con los nombres que sean mientras sean facil de recordar



////////LENGUAJE ORIENTADO A OBJETOS

//// oscilador sinusoidal controla la frecuencia de un oscilador sinusoidal
{SinOsc.ar(SinOsc.kr(440, 20,100, 100),0, 1) }.scope

// oscilador de triángulo es oscilador y lfo al modular la frecuencia del primer oscilador
{ LFTri.ar(LFTri.kr(4, 0, 200, 400), 0, 0.3) }.play

// oscilador de sierra controla la frecuencia de otro oscilador de sierra previo
{LFSaw.ar(LFSaw.kr(1, 0, 200, 400), 0, 0.1) }.play


// modular la frecuencia con una linea exponencial en un oscilador sinusoidal
{ SinOsc.ar(XLine.kr(2000, 200), 0, 0.5) }.play;

// o en con un hard sync sawtooth wave.
{ SyncSaw.ar(100, Line.kr(100, 800, 12), 0.1) }.play;

//Band limited impulse oscillator.  step noise
{Blip.ar(25, LFNoise0.kr(5, 12, 14),1.5)}.scope

//Band limited impulse oscillator generador de linea
{ Blip.ar(200,Line.kr(1,100,20),0.5) }.play;

//Par de osciladores de fase modulada y un generador de linea
{PMOsc.ar(Line.kr(600, 900,5),600,3,0,0.5)}.scope

//Phase modulation oscillator pair
{PMOsc.ar(440, MouseY.kr(1,500), MouseX.kr(1, 15))}.scope



// LFNoise0 > non interpolating noise generator
(
y = {
var freq, sig;
	freq = LFNoise0.kr(8, 400, 600); //freq random value // beteween 200 and 1000 hz
	sig= SinOsc.ar(freq);
}.play;
)

// entre paréntesis par evaluar varias lineas del codigo

(
z = {
	arg noiseHz=8;
	var freq,amp,sig;
	freq = LFNoise0.kr(noiseHz).exprange(400,600);
	amp = LFNoise1.kr(12).exprange(0.2,1);
	sig = SinOsc.ar(freq) * amp;
}.play;
)

z.set(\noiseHz,10);
z.set(\noiseHz. exprand(4,100));
z.set(\amp, 3);
z.free;


//////// WHAT YOU SEE IS WHAT YOU GET 