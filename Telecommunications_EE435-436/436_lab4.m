%Lab 4, group 12

clear all;
close all;

% channel = [0.9 0.5 0.3 0.2];
channel = [0.9 0.5 0.3 0.2 ];     % actual channel response
M = 4;
N = 1000;                         % length of transmitted sequence
SNR_dB = 50;
SNR=10^SNR_dB/10;

T=1;    %Symbol length
beta = 1;
m =5;


% seq = randi([0 M-1],1,N);
seq = randi([0 M-1],1,N);       % transmitted bit sequence
x = pskmod(seq, M, pi/4);       % transmitted signal
x = [x(1:N/2) x(end-length(channel)+2:end)  x(N/2+1:end)];

%Root raised cosine pulse p(t)
p = rcosdesign(beta,2*m,10, 'sqrt');

x_up = upsample(x,10);
y_up = conv(x_up,p);

channel_up = upsample(channel,10);
r = filter(channel_up,1,y_up);
r2= conv(channel_up,y_up);

%In-phase, Quadrature and total noise components
noise_real = (1/sqrt(SNR*2))*randn(1,length(r));
noise_imag = (1/sqrt(SNR*2))*j*randn(1,length(r));
noise = noise_real + noise_imag;

r_noisy = r + noise;

% r = filter(channel,1,x);
% r2= conv(channel,x);

% MF:
s_long = conv(r_noisy,fliplr(p));
s = s_long(length(p):10:end-length(p));   %Sample MF output at 10th samples
scatterplot(s)
title('Matched Filter Output s(t)');


iter = 50;                      % number of iterations
mu = 1e-1;
tap = 4;                        % channel tap

Input = zeros(1,tap);           % Input initial
H = zeros(1,tap);               % initial H


for k = 1 : iter
    for n = 1 : N/2
        Input(1,2:end) = Input(1,1:end-1);  % Shifting for convolution
operation
        Input(1,1) = x(n);


        z = conj(H)*Input.';
        error=s(n)-z;

        H= H + mu * conj(error) *Input;

    end
end


%plot the results
response_channel=freqz(channel);
mag_channel=10*log10(real(response_channel).^2 + imag(response_channel).^2);
phase_channel=imag(response_channel)./real(response_channel);

response_equalizer=freqz(H);
mag_est=10*log10(real(response_equalizer).^2 + imag(response_equalizer).^2);
phase_equ2=imag(response_equalizer)./real(response_equalizer);

normalized_freq=(0:length(response_channel)-1)./(length(response_channel));



figure(2)
plot(normalized_freq,mag_channel)
hold on
plot(normalized_freq,mag_est)
grid on
legend('Actual Channel','Estimate');
title('Magnitude Response');

% % equalizer
equ1=fft(H.',N/2);
equ2=conj(equ1)./(abs(equ1).^2);
y=s;
y(1:N/2+length(channel)-1)=[];
rx_f=fft(y,N/2);
rxFilt=ifft(rx_f.*equ2.',N/2);
scatterplot(rxFilt);
