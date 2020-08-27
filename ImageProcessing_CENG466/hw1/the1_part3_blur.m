%Zumrud Shukurlu 2174761 & Yekta Demirci 2093607
%All figures are filtered with a gaussian kernel of size 3x3
for no = 1:3

    A = imread('C'+string(no)+'.png');    
    gausKernel = (1/16).*[1 2 1; 2 4 2; 1 2 1];
    B = the1_convolution (A,gausKernel);
    B = cast(B,'uint8');
    imwrite(B,'C'+string(no)+'_blurred.png');
    
end

clear all