%EE436 Lab 3.
close all
clear all

T=1;    %Symbol length
beta = 0.25;    %roll-off factor
sigma = 0.00008;  %noise variance
m =5;

%Root raised cosine pulse p(t)
p = rcosdesign(beta,m,10);
% plot(p)
% title('Generated RRC');

% Random bit sequence a[k] takes integer values between 1 to 4
a = randi([1 4], [1,1024]);
% Mapping of a[k] to b[k] for QPSK modulation
b = exp(j*(2*a-1)*pi/4);
scatterplot(b)    %for checking whether the mapping is correct
title('QPSK Symbols');

%Upsample b by 10 and convolve it with p(t)
b_up_l = upsample(b,10);
%drop the last 9 samples of b_up_l since they are all zero due to
%upsampling
b_up = b_up_l(1:length(b_up_l)-9);

%convolve b_up and p(t) to obtain transmit sequence y(t). Notice that p(t)
%has length 11, hence there is 1 sample aliasing since b is upsampled by
%10. In order to get rid of this effect, take only the 1st ten samples of
%p(t) into account
y = conv(b_up,p(1:10));
y2 = downsample(y,10,5);
scatterplot(y2)
title('Transmitted Sequence y(t)');

%In-phase, Quadrature and total noise components
noise_real = (1/sqrt(2))*sigma*randn(1,length(y));
noise_imag = (1/sqrt(2))*j*sigma*randn(1,length(y));
noise = noise_real + noise_imag;

%Received Signal
r = y + noise;
scatterplot(downsample(r,10,5))
title('Received Signal r(t)');

% MF
s_long = conv(r,flip(p(1:10)));
s = s_long(10:10:length(s_long));   %Sample MF output at 10th samples
scatterplot(s)
title('Matched Filter Output s(t)');

%Signal and noise power after MF
yy = conv(y,flip(p(1:10)));
nn = conv(noise,flip(p(1:10)));

SNR_o = abs(yy(11:10:length(yy)).^2)/abs(nn(11:10:length(nn)).^2);
SNR_out = 10*log10(SNR_o)

% EVM
error = s - b;
EMV = mean(abs(error))/mean(abs(b))


