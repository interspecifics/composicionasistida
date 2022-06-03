// 1, start the server
s.boot;




// 2. create a synth
SynthDef(\sawFilt, { |out = 0, freq = 1600, amp = 0.1, gate = 0, cf = 100, wobble = 3, t_bd, t_sd, pw = 0.4|
    var base = Splay.ar(RLPF.ar(Pulse.ar(freq * [0.99,0.5,1.01],pw),cf.lag(0.05),0.3).madd(SinOsc.ar(wobble).range(0.5,4)).sin) * 0.5;
    var env = Linen.kr(gate, attackTime: 0.01, releaseTime: 0.5, doneAction: 0);
    var sig = base;
    var bd = tanh(Ringz.ar(LPF.ar(Trig.ar(t_bd,SampleDur.ir),100),30,0.5,5).sin*2);
    var sd = tanh(Ringz.ar(LPF.ar(Trig.ar(t_sd,SampleDur.ir),1000),120,0.75,PinkNoise.ar(2!2)).sin*2);
    sd = HPF.ar(sd,60);
    sig = tanh(GVerb.ar(HPF.ar(base * env,30), 70, 11, 0.15)*0.5 + sig + bd + sd);
    Out.ar(out, sig*amp*env);
}).store;


// 3. create a callback for OSC route /data
OSCdef.new(
	\rot_a,
	{
		arg msg, time, addr, port;
		//[msg, time, addr, port].postln;
		var cf_a, wo_a, pw_a;
		cf_a = msg[3].linlin(0,90,10,1000);
		wo_a = msg[2].linlin(0,40,1.0,5.0);
		pw_a = msg[5].linlin(950,1000,2.5, 0.01);
        ~aSynth.set(\cf, cf_a);
		~aSynth.set(\wooble, wo_a);
		~aSynth.set(\pw, pw_a);
		msg.post; "->".post; cf_a.post; " ".post; wo_a.post; " ".post; pw_a.postln;
	},
	'/data'
);




// 4. instance a synth
~aSynth = Synth(\sawFilt, [\gate, 0, \freq, 220]);


// 5. turn it on
~aSynth.set(\gate, 1, \midi, 67);


// 6. start the data flow



// 7. stop the sound
~aSynth.set(\gate, 0);
