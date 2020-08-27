%Zumrud Shukurlu 2174761 & Yekta Demirci 2093607
%Kernels are used for each input by using self written convolution function
%Kernels
Sx=[-1 0 1; -2 0 2; -1 0 1];
Sy=[1 2 1; 0 0 0; -1 -2 -1];
Rx=[0 1;-1 0];
Ry=[1 0;0 -1];

%Images Image
for no = 1:3

    A = imread('C'+string(no)+'.png');

    B = the1_convolution (A,Sx);
    B = cast(B,'uint8');
    imwrite(B,'C'+string(no)+'_Sx.png');

    B = the1_convolution (A,Sy);
    B = cast(B,'uint8');
    imwrite(B,'C'+string(no)+'_Sy.png');

    B = the1_convolution (A,Rx);
    B = cast(B,'uint8');
    imwrite(B,'C'+string(no)+'_Rx.png');

    B = the1_convolution (A,Ry);
    B = cast(B,'uint8');
    imwrite(B,'C'+string(no)+'_Ry.png');

end

clear all