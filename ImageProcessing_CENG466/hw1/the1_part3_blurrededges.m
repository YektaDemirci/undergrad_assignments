%Zumrud Shukurlu 2174761 & Yekta Demirci 2093607
%Exact same methods are used for the blurred images as the previous parts
%Kernels
Sx=[-1 0 1; -2 0 2; -1 0 1];
Sy=[1 2 1; 0 0 0; -1 -2 -1];
Rx=[0 1;-1 0];
Ry=[1 0;0 -1];

%Operations for S
for no = 1:3

    A = imread('C'+string(no)+'_blurred.png');

    B = the1_convolution (A,Sx);
    C = the1_convolution (A,Sy);
    
    [x,y] = size(B);
    D = zeros(x, y);
    
    for row = 1:x

            for column = 1:y

               D(row,column) = sqrt( (B(row,column).^2) + (C(row,column).^2) );

            end
    end
    
    D = cast(D,'uint8');
    imwrite(D,'C'+string(no)+'_S_blurred.png');

end


%Operations for R
for no = 1:3

    A = imread('C'+string(no)+'_blurred.png');

    B = the1_convolution (A,Rx);
    C = the1_convolution (A,Ry);
    
    [x,y] = size(B);
    D = zeros(x, y);
    
    for row = 1:x

            for column = 1:y

               D(row,column) = sqrt( (B(row,column).^2) + (C(row,column).^2) );

            end
    end
    
    D = cast(D,'uint8');
    imwrite(D,'C'+string(no)+'_R_blurred.png');

end

clear all