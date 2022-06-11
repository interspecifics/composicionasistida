////////ESTRUCTURA PARA ESCUCHAR DATOS/////////////

OSCFunc.trace(true);
OSCFunc.trace(false); // Turn posting off

(
SynthDef( \sin, {
	arg amp = 0.01, freq = 120, trig = 1;
    var env, sig;
    env = EnvGen.kr( Env.asr( 0.001, 0.9, 0.001 ), trig, doneAction: 0 );
    sig = SinOsc.ar(freq, 0.0, amp )!2 * env;
    Out.ar( [ 0 ], sig * 0.6 );
}).add;
)

h = Synth( \sin, [ \amp, 0.4 ] );
h.free;

(
x = OSCFunc( { | msg, time, addr, port |
    var data4;
	data4= msg[4];
    ( "cuarto valor " + data4 ).postln;
	h.set ( \freq, data4);
}, '/data' );
)
x.free;


////////MAPEAR VALORES EN UMBRALES/////////////
//Asignar un rango lineal a otro rango lineal

(
SynthDef( \sin, {
	arg amp = 0.01, freq = 120, trig = 1;
    var env, sig;
    env = EnvGen.kr( Env.asr( 0.001, 0.9, 0.001 ), trig, doneAction: 0 );
    sig = SinOsc.ar(freq, 0.0, amp )!2 * env;
    Out.ar( [ 0 ], sig * 0.6 );
}).add;
)

h = Synth( \sin, [ \amp, 0.4 ] );
h.free;

(
x = OSCFunc( { | msg, time, addr, port |
    var data3;
	data3= msg[3].linlin(40,90,120,220);
    ( "tercer valor " + data3 ).postln;
	h.set ( \freq, data3);
}, '/data' );
)
x.free;


////////SYNTHDEF forma organizada de syntes/////////








//ejemplo con aire mini



