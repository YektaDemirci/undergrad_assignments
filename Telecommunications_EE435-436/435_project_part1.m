% EE435 Project Phase 1
% Yekta Demirci 2093607
% Ece Bingöl 2093516
% Group 19

%%
% Question 1
n=1e3;              % Sample number
Ts=1e-6;            % Sampling time
T=1e-3;             % Bit duration
t=0:Ts:n*Ts-Ts;     % Time vector for plots

% Create a bit with value 1 (i.e. p(t) = 1)
p = 2.*pulstran(t,500*Ts,@rectpuls,1000*Ts)-1;

% Create Barker 3 Code sequence using "pulstran" command
s = 2.*pulstran(t,[1,5]*(1000/6)*Ts,@rectpuls,(1000/3)*Ts)-1;

b = p .* s;
figure(1)
plot(t,b)
xlabel ('Time (s)'); ylabel ('b(t)');  ylim([-1.5 1.5]);
title('Message signal p(t) = 1 coded with Barker-3 Sequence');
%%
% Question 2
% a: Barker 7 
n=1e3;              % Sample number
Ts=1e-6;            % Sample time
T=1e-3;             % Bit duration
t=0:Ts:n*Ts-Ts;     % Time vector for plots

% Create a bit with value 1, using "pulstran" command (p(t) = 1)
p = 2.*pulstran(t,500*Ts,@rectpuls,1000*Ts)-1;

% Create Barker 7 Code sequence using "pulstran" command
s1 = 2.*pulstran(t,[1,3,5,11]*(1000/14)*Ts,@rectpuls,(1000/7)*Ts)-1;

b1 = p .* s1;
figure(2)
plot(t,b1)
xlabel ('Time (s)'); ylabel ('b1(t)'), ylim([-1.5, 1.5]);
title('Message signal p(t) = 1 coded with Barker-7 Sequence');

% Create Barker 13 Code sequence using "pulstran" command
s2 = 2.*pulstran(t,[1,3,5,7,9,15,17,21,25]*(1000/26)*Ts,@rectpuls,(1000/13)*Ts)-1;

b2 = p .* s2;
figure(3)
plot(t,b2)
xlabel ('Time (s)'), ylabel ('b2(t)'); ylim([-1.5 1.5]);
title('Message signal p(t) = 1 coded with Barker-13 Sequence');

% Create Anti Barker 13 Code sequence using "pulstran" command
s3 = 2.*pulstran(t,[11,13,19,23]*(1000/26)*Ts,@rectpuls,(1000/13)*Ts)-1;

b3 = p .* s3;
figure(4)
plot(t,b3)
xlabel ('Time (s)'), ylabel ('b3(t)'); ylim([-1.5 1.5]);
title('Message signal p(t) = 1 coded with Anti Barker-13 Sequence');

%%
% Question 3
n=1e3;              % Sample number
Ts=1e-6;            % Sampling time
T=1e-3;             % Bit duration
fs=1/Ts;            % Sampling frequency
    
% In order to create a random 5-bit sequence as message, create a 1x5
% vector whose elements are either 1 or -1.
randoms = randi([0,1],1,5);

% Since message signal consists of 5 bits, the array we create must have
% size 1x5000 (one bit had 1000 samples, therefore 5 bits have 5000
% samples)
o = ones(1,5000);     % Array of ones with size 1x5000, i.e. 5 bits

% Multiply p, with randoms array to construct 5-bit message signal. Since
% one bit consists of 1000 samples, the first 1000 elements of p must be
% multiplied with first element of randoms array. The next 1000 elements
% (from o(1001) to o(2000)) must be multiplied with randoms(2) and so on.
% This is done by the following for loop
for a=(1:5)
    p((1000*(a-1)+1):a*1000)=2*(o(1000*(a-1)+1:a*1000).*randoms(a))-1;
end

% Barker-3
s = 2.*pulstran(t,[1,5]*(1000/6)*Ts,@rectpuls,(1000/3)*Ts)-1;
% Barker-7
s1 = 2.*pulstran(t,[1,3,5,11]*(1000/14)*Ts,@rectpuls,(1000/7)*Ts)-1;
% Barker-13
s2 = 2.*pulstran(t,[1,3,5,7,9,15,17,21,25]*(1000/26)*Ts,@rectpuls,(1000/13)*Ts)-1;

% Create coded message signals b(t), b1(t) & b2(t) (coded with Barker-3,
% Barker-7 and Barker-13 respectively
for a=(1:5)
    b((1000*(a-1)+1):a*1000)=p(1000*(a-1)+1:a*1000).*s;
end

for a=(1:5)
    b1((1000*(a-1)+1):a*1000)=p(1000*(a-1)+1:a*1000).*s1;
end

for a=(1:5)
    b2((1000*(a-1)+1):a*1000)=p(1000*(a-1)+1:a*1000).*s2;
end

% Autocorrelation functions of b(t), b1(t) & b2(t) found using "xcorr"
% command
acf_b = xcorr(b,b);        % Autocorrelation function of b(t)
acf_b1 = xcorr(b1,b1);     % Autocorrelation function of b1(t)
acf_b2 = xcorr(b2,b2);     % Autocorrelation function of b2(t)

% Power Spectrum Densities of b(t), b1(t) & b2(t) found using "fft"
% command. (Note that DFT size is 5 times length of corresponding acf)
PSD_b = 10*log10(abs(fft(acf_b,5*length(acf_b))));
PSD_b1 = 10*log10(abs(fft(acf_b1,5*length(acf_b1))));
PSD_b2 = 10*log10(abs(fft(acf_b2,5*length(acf_b2))));

w = linspace(0,2,5*length(acf_b));   % Frequency array

figure(5)
plot(w,PSD_b);
title('PSD of b(t) in dB scale');
ylabel('dB');
xlabel('frequency (*pi rad)');   % For clarity (*pi) multiplicity 
                                        % is taken outside, i.e. multiply
                                        % each x axis reading by pi.

figure(6)
plot(10.^(PSD_b(1:1001)/10));
title('PSD of b(t) for the first 1000 samples');
ylabel('PSD of b(t)'); xlabel('sample (n)');
                                        
figure(7)
plot(w,PSD_b1);
title('PSD of b1(t) in dB scale');
ylabel('dB'); xlabel('frequency (*pi rad)');

figure(8)
plot(10.^(PSD_b1(1:1001)/10));
title('PSD of b1(t) for the first 1000 samples');
ylabel('PSD of b1(t)'); xlabel('sample (n)');

figure(9)
plot(w,PSD_b2);
title('PSD of b2(t) in dB scale');
ylabel('dB'); xlabel('frequency (*pi rad/sample)');

figure(10)
plot(10.^(PSD_b2(1:1001)/10));
title('PSD of b2(t) for the first 1000 samples');
ylabel('PSD of b2(t)'); xlabel('sample (n)');

% In Figures 5, 7 and 9 PSDs of b(t), b1(t) and b2(t) are drawn in
% decibel scale. When these figures are compared not much of a difference
% is observed. All of three PDSs begin from a very high value 
% (approximately 70 dB) then decrease as the frequency increases. The 
% actual difference between these PSDs are better observed in Figures 6, 8
% and 10. Since there are too many samples, PSDs are drawn upto the first 
% 1000 samples in these figures. By looking at them we can easily see the 
% lobes of sinc functon. Since the message signal consists of rectangular 
% pulses, the general shape (envelope) of PSD is a sinc function and since 
% these pulses are quasi periodic PSDs consist of impulse like . From
% inspection of these figures we can see that as the degree of barker code 
% increases, the bandwith also increases. The first zero of PSD of b(t)
% occurs approximately at 150th sample whereas the first zeros of PSDs of
% b1(t) and b2(t) occur approximately at 350th and 650th samples
% respectively (see Figures 5, 7 and 9 to see this more clearly). 
% Therefore the bandwith of the message signal is larger when
% it is coded with a higher degree barker code (Barker-13 > Barker-7 >
% Barker-3). This result is expected since the autocorrelation function of 
% Barker-3 is flatter than Barker-7 and Barker-13 (see figure 16, 17 and 
% 18). There is an inverse relation between autocorrelation and PSD. Since 
% they are related by Fourier Transform, the flatter the autocorrelation 
% is, the sharper the PSD. As as result when the messae is coded with
% Barker-13, it has largest bandwidth because, the autocorrelation function 
% of Barker-13 is the sharpest. On the other hand, when the message was 
% coded with Barker-3, it has the narrowest bandwidth because the 
% autocorrelation function of Barker-3 is the flattest. The characteristics
% of Barker-7 is in the middle (neither sharpest, nor the flattest both in 
% PSD and autocorrelation). 

%%
% Question 4
n=1e3;              % Sample number
Ts=1e-6;            % Sampling time
T=1e-3;             % Bit duration

% Barker 13 code sequence for modulating the first signal (b2(t))
s2 = 2.*pulstran(t,[1,3,5,7,9,15,17,21,25]*(1000/26)*Ts,@rectpuls,(1000/13)*Ts)-1;

% Anti Barker 13 code sequeence for modulating the second signal (b3(t))
s3 = 2.*pulstran(t,[11,13,19,23]*(1000/26)*Ts,@rectpuls,(1000/13)*Ts)-1;

% Create two independent 5-bit random message signals b2(t) and b3(t) using
% "randi" & "ones" commands with for loop. This process is explained in 
% Question 3.
% First signal b2(t):
randoms2=randi([0,1],1,5);
o2=ones(1,5000);
for a=(1:5)
    p2((1000*(a-1)+1):a*1000)=2*(o2(1000*(a-1)+1:a*1000).*randoms2(a))-1;
end

for a=(1:5)
    b2((1000*(a-1)+1):a*1000)=p2(1000*(a-1)+1:a*1000).*s2;
end

% Second signal b3(t)
randoms3=randi([0,1],1,5);
o3=ones(1,5000);
for a=(1:5)
    p3((1000*(a-1)+1):a*1000)=2*(o3(1000*(a-1)+1:a*1000).*randoms3(a))-1;
end

for a=(1:5)
    b3((1000*(a-1)+1):a*1000)=p3(1000*(a-1)+1:a*1000).*s3;
end

r=b2+b3;    % Received signal r(t)
acf_r = xcorr(r,r);     % Autocorrelation function of r(t)
PSD_r = 10*log10(abs(fft(acf_r,5*length(acf_r))));

figure(11)
wr = linspace(0,2,5*length(acf_r));   % Frequency array
plot(wr,PSD_r);
title('PSD of r(t) in dB scale');
ylabel('dB');
xlabel('frequency (*pi rad)');

figure(12)
plot(10.^(PSD_r(1:1001)/10));
title('PSD of r(t) for the first 1000 samples');
ylabel('PSD of r(t)'); xlabel('sample (n)');

% Question 5:
% Despread r(t) by multiplying with again Barker-13 sequence (s(t))
for a=(1:5)
    d((1000*(a-1)+1):a*1000)=r(1000*(a-1)+1:a*1000).*s2;
end

acf_d = xcorr(d,d);     % Autocorrelation function of d(t)
PSD_d = 10*log10(abs(fft(acf_d,5*length(acf_d))));

figure(13)
wd = linspace(0,2,5*length(acf_d));   % Frequency array
plot(wd,PSD_d);
title('PSD of d(t) in dB scale');
ylabel('dB'); xlabel('frequency (*pi rad)');

figure(14)
plot(10.^(PSD_d(1:1001)/10));
title('PSD of d(t) for the first 1000 samples');
ylabel('PSD of d(t)'); xlabel('sample (n)');

figure(15)
subplot(2,1,1)
plot(b2)
title('Sent message');
xlabel('time(us)');
ylabel('Amplitude');
ylim([-1.5 1.5]);

subplot(2,1,2)
plot(d)
('Received Message');
xlabel('time(us)');
ylabel('Amplitude');
ylim([-2.1 2.1]);

% In Figures 11 and 13, PSDs of r(t) & d(t) are drawn in decibel scale.
% When these plots are compared one can see that PSD of d(t) is sharper
% than PSD of r(t). In other words, the initial high value at w=0 decays
% much faster in PSD of d(t). (For example, in one our trials, we observed 
% that at w=0.2*pi, PSD_d was  16dB whereas PSD_r was 30 dB). When these 
% PSDs are plotted without dB scale for the first 1000 samples (the same 
% process as in question 3), it can be seen that bandwidth of r(t) is much 
% larger than bandwidth of d(t). The first zero of PSD of r(t) occurs
% approximately at 650th sample while the first zero PSD of of d(t) occcurs
% approximately at 50th sample. Hence we can conclude that d(t) has
% narrower bandwidth.


% In addition to above observations we also saw that, we cannot obtain b2(t) 
% by directly multiplying with s2(t) (see Figure 15). The reason is that 
% s2 & s3 are not orthogonal. In fact they are highly correlated. Since s3 
% is negative of s2, when r(t) is multiplied with s2(t) the resultant 
% signal d(t) can have 3 values, -2,0,2. If p2(t) & p3(t) are the same for 
% a bit duration, the corresponding bit of d(t) will be 0 because b2(t) & 
% b3(t) cancels each other. If p2(t) & p3(t) are different for a bit 
% duration, d(t) will be either 2 or -2 since b2(t) & b3(t) adds up.

%%
% Additional helpful plots: autocorrelations of Barker-3, Barker-7 &
% Barker-13
tau = -999:999;    % shift array for calculating autocorrelation function
figure (16)
plot(tau,xcorr(s,s))
title('Autocorrelation function of Barker-3')
ylabel('Rss(tau)'); xlabel('tau');

figure(17)
plot(tau,xcorr(s1,s1))
title('Autocorrelation function of Barker-7')
ylabel('Rss(tau)'); xlabel('tau');

figure(18)
plot(tau,xcorr(s2,s2))
title('Autocorrelation function of Barker-13')
ylabel('Rss(tau)'); xlabel('tau');