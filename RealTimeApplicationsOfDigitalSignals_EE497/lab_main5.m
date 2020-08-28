rng default;

N=1000;
P=10;
a=0.8;
var=1;


[co,top,top2,coefs2]=filtre(N,P,a,var);

raw=randn(1,N);

Sn=filter(1,[1,-a],raw);

Xn=Sn+randn(1,N);

Yn=filter(co,1,Xn);

Dn = Sn;

En=Dn-Yn;

% top=0
% for i = (1:P)
%     top=top+(Dn(i)*Dn(i));
% end
%top = 2.777777777777779;
MSE=top-top2;
LSE = mean(En.^2);

figure
hold on
plot(Dn)
plot(Yn)

yenifilt=firpm(30,[0 0.4 0.8 1],[1 1 0 0]);

yeniYn=filter(yenifilt,1,Xn);

yeniEn=Dn-yeniYn;
yeniLSE = mean(yeniEn.^2);

top3=0
for i = (1:3)
   top3=top3+(1/(1-a^2))*co(i)*(a)^abs(i+2-1) 
end

MSEson=top-top3;

Dnfin = Sn(3:end);
Ynfin=filter(coefs2,1,Dnfin);
Enfin=Dnfin-Ynfin;
LSEfin = mean(Enfin.^2);


