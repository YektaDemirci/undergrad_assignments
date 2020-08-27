% Yekta Demirci 2093607
% Zumrud Shukurlu 2174761
%%
f = imread('C1.png');
x=[0 1;-1 0];
y=[1 0;0 -1];


F = fft2(f);
X = fft2(x, size(f,1), size(f,2));
Y = fft2(y, size(f,1), size(f,2));
F1 = X.*F;
F2 = Y.*F;
ffix = ifft2(F1);
ffiy = ifft2(F2);

[x,y] = size(ffix);
fin= zeros(x, y);

for row = 1:x
    for column = 1:y
       fin(row,column) = sqrt( (ffix(row,column).^2) + (ffiy(row,column).^2) );
    end
end

%imshow(uint8(fin));

imwrite(uint8(fin), 'C1_output.png');
%%
%The same stuff for the 2nd image
f = imread('C2.png');
x=[0 1;-1 0];
y=[1 0;0 -1];


F = fft2(f);
X = fft2(x, size(f,1), size(f,2));
Y = fft2(y, size(f,1), size(f,2));
F1 = X.*F;
F2 = Y.*F;
ffix = ifft2(F1);
ffiy = ifft2(F2);

[x,y] = size(ffix);
fin= zeros(x, y);

for row = 1:x
    for column = 1:y
       fin(row,column) = sqrt( (ffix(row,column).^2) + (ffiy(row,column).^2) );
    end
end

%imshow(uint8(fin));

imwrite(uint8(fin), 'C2_output.png');
