% EE435 Project Phase-2
% Yekta Demirci 2093607
% Ece Bingöl 2093516
% Group 19

%%
% Question 6

noise_var = 50;      % Noise variance parameter
n=1e3;              % Sample number
Ts=1e-6;            % Sampling time
T=1e-3;             % Bit duration
t=0:Ts:n*Ts-Ts;     % Time vector for generating barker code signals
t2 = linspace(0,2*T,2*n-1);     % Time vector for plotting the graphs
nb = 10000;             % bit number

for (i=1:nb)
% Create a bit whose value is 0 or 1 using randi function. Then transform
% these values to +-1 since either +b(t) or -b(t) is sent

% randoms = randi([0,1],1,nb);
% o = ones(1,n*nb);     % Array of ones with size 1x5000, i.e. 10000 bits
% for a=(1:nb)
%     p((1000*(a-1)+1):a*1000)=2*(o(1000*(a-1)+1:a*1000).*randoms(a))-1;
% end
a(i) = randi([0,1]);
A(i) = 2.*a(i)-1;

% Create Barker 3 Code sequence using "pulstran" command
s = 2.*pulstran(t,[1,5]*(1000/6)*Ts,@rectpuls,(1000/3)*Ts)-1;

% Create Barker 7 Code sequence using "pulstran" command
s1 = 2.*pulstran(t,[1,3,5,11]*(1000/14)*Ts,@rectpuls,(1000/7)*Ts)-1;

% Create Barker 13 Code sequence using "pulstran" command
s2 = 2.*pulstran(t,[1,3,5,7,9,15,17,21,25]*(1000/26)*Ts,@rectpuls,(1000/13)*Ts)-1;

% Create 1-bit of random message signals
b = A(i).*s;

% Add AWGN noise this message signal, then convolve it with the matched
% filter
rec_signal = b + sqrt(noise_var)* randn(1,length(b));
mf_out =conv(rec_signal, fliplr(s))./1000;

if (mf_out(1000)>=0)
    rec_bit(i) = 1;
else
    rec_bit(i) = -1;
end

i

figure(19)
plot(t2,mf_out)
hold on
title('Matched Filter output for Barker-3 (noise-var = 50)')
ylabel('z(t)'); xlabel('time(s)');
end