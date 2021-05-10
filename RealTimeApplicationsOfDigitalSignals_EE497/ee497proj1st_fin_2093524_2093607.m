p=1044;
m=16;
L=108;

x=randn(1,p);
h=randn(1,m);
x_pad=horzcat(zeros(1,m-1),x,zeros(1,L));

fin=[];
h_fft=fft(h,L);
x_fft=fft(x_pad(1:L),L);
y_fft=x_fft.*h_fft;
y=ifft(y_fft,L);
fin=horzcat(fin,y(m:end));
for wind=L:(L-m+1):length(x_pad)-L
h_fft=fft(h,L);
x_fft=fft(x_pad(wind-(m-2):wind+L-(m-2)),L);
y_fft=x_fft.*h_fft;
y=ifft(y_fft,L);
d0ru=y(m:end);
fin=horzcat(fin,d0ru);
end
fin=fin(1:m+p-1);
cont=conv(x,h);

figure;
hold on;
plot(cont)
title('Plot of the Convolution & OLS Results')
plot(fin,':')
legend('Control by conv','Overlap and Save')
hold off;
if(isequal(round(fin,10),round(cont,10)))
    disp('Result is True')
    
else disp('Result is False')
    
end