% EE436 Lab3
% 16-QAM

close all
clear all

T=1;    %Symbol length
beta = 0.25;    %roll-off factor
sigma = 0.0015;  %noise variance
m =1;

%Root raised cosine pulse p(t)
p = rcosdesign(beta,m,10);
% plot(p)
% title('Generated RRC');

% Random bit sequence a[k] takes integer values between 1 to 4
a = randi([0 15], [1,1024]);
% % Mapping of a[k] to b[k] for QPSK modulation
% b = floor(exp(j*(2*a-1)*pi/4);
% scatterplot(b)    %for checking whether the mapping is correct
% title('QPSK Symbols');