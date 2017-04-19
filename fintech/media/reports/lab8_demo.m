% demo for Lab 8 concerning modulation schemes

Fc = 50; % carrier frequency for digital processing in Hz
Fc_audio = 1500; % carrier frequency for audio output in Hz
Fs_audio = 8000; % audio sampling rate

% time sampling (64x sampling)
t = (0:2*Fc*64)./(Fc*64);
t_audio = (0:2*Fs_audio)./Fs_audio;
%{
%% 2. square wave
sqwave = @(f,t) 2.*(f.*t - floor(f.*t) < 0.5) - 1;

figure; plot(t,sqwave(2,t));

%% 3. ASK carrier
xASK = cos(2*pi*Fc*t).*(1+0.5*sqwave(2,t));

figure; plot(t,[sqwave(2,t);xASK]);

xASK_audio = cos(2*pi*Fc_audio*t_audio).*(1+0.5*sqwave(2,t_audio));
xASK_audio = xASK_audio./max(xASK_audio);
sound(xASK_audio,Fs_audio);


%% 4. PSK carrier
xPSK = cos(2*pi*Fc*t).*sqwave(2,t);

figure; plot(t,[sqwave(2,t);xPSK]);

xPSK_audio = cos(2*pi*Fc_audio*t_audio).*sqwave(2,t_audio);
xPSK_audio = xPSK_audio./max(xPSK_audio);
sound(xPSK_audio,Fs_audio);

%% 5. do PSK again for higher frequency modulation
Fm = 10; % try a few values here
xPSK = cos(2*pi*Fc*t).*sqwave(Fm,t);

figure; plot(t,[sqwave(Fm,t);xPSK]);

xPSK_audio = cos(2*pi*Fc_audio*t_audio).*sqwave(Fm,t_audio);
xPSK_audio = xPSK_audio./max(xPSK_audio);
sound(xPSK_audio,Fs_audio);
%}
%% 6. FSK carrier and varying deviation parameter m
m = 0.9; % try a few different values (0 < m < 1)
xFSK = cos(2*pi*Fc*(1+m.*sqwave(2,t)).*t);

figure; plot(t,[sqwave(2,t);xFSK]);

xFSK_audio = cos(2*pi*Fc_audio*(1+m.*sqwave(2,t_audio)).*t_audio);
xFSK_audio = xFSK_audio./max(xFSK_audio);
sound(xFSK_audio,Fs_audio);
%}