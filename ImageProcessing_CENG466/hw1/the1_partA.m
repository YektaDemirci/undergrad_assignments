%%
%Zumrud Shukurlu 2174761 & Yekta Demirci 2093607
%For the first image
a1 = imread('A1.png');
a1_output(:,:,1) = transpose(a1(:,:,1));
a1_output(:,:,2) = transpose(a1(:,:,2));
a1_output(:,:,3) = transpose(a1(:,:,3));

% flipping the image horizontally as the transpose operation created a
% mirror image of the original image, the input image was rotated 90 degrees
% counterclockwise
a1_output = a1_output(:, end:-1:1, :);

imwrite(a1_output, 'A1_output.png');
clear all
%%

%For the second image
a2 = imread('A2.png');
a2 = double(a2)./255;

height = size(a2, 1);
width = size(a2, 2);

theta = pi/4;
rotation_matrix = [cos(theta) -sin(theta) 0; sin(theta) cos(theta) 0; 0 0 1];
                
t_x = width/2;
t_y = height/2;
% pixels have to be translated to the origin
% in order to rotate the image w.r.to the origin
%(the center coordinate of the image does not change)
% and should be translated
%back to their original positions after rotation
translation_matrix = [1 0 -t_x; 0 1 -t_y; 0 0 1];

tf_matrix = inv(translation_matrix) * rotation_matrix * translation_matrix;
inverse_tf_matrix = inv(tf_matrix);
a2_output = zeros(height, width, 3);
%a2_output = zeros(640, 480, 3);

for i = 1:width
    for j = 1:height
        
        x = [i; j; 1];
        %y = rotation_matrix * x;
        y = inverse_tf_matrix * x;
        
        a = round(y(1));
        b = round(y(2));
        
        if (a > 0 && a<= width && b > 0 && b <= height)
            a2_output(j, i, :) = a2(b, a, :);
        end
    end
end

% these values were obtained from the original images
% supplied for comparison
w_orig = 640;
h_orig = 480;

% remove the black parts surrounding the output image
w_start = round((width - w_orig)/2);
w_end = w_start + w_orig;

h_start = round((height - h_orig)/2);
h_end = h_start + h_orig;

a2_output = a2_output(h_start:h_end, w_start:w_end, :);

%Filtering for better image
%kernel=[0 -1 0; -1 5 -1; 0 -1 0];
%a2_output(:,:,1) = the1_convolution (a2_output(:,:,1),kernel);
%a2_output(:,:,2) = the1_convolution (a2_output(:,:,2),kernel);
%a2_output(:,:,3) = the1_convolution (a2_output(:,:,3),kernel);


imwrite(a2_output, 'A2_output.png');
clear all


%%
%For the third image
A = imread('A3.png');

cont=1;
row=1;
col=1;
%Location of the first pure black pixel is found from left top corner
while cont
    if (A(row,col,1) == 0) && (A(row,col,2) == 0) && (A(row,col,3) == 0)
        if col == 450
            col=1;
            row=row+1;
        else
            col=col+1;
        end
    else
        break
    end    
end
%After finding the first pure black pixel, the meaningful part is extracted
row=row-1;
col=col-1;

fin = zeros((size(A,1)-row),(size(A,2)-col),3,'uint8');

for colour = 1:size(fin,3)
    for dum2 = 1:size(fin,2)
        for dum = 1:size(fin,1)
            fin(dum,dum2,colour)=A(dum+row,dum2+col,colour);
        end
    end
end
imwrite(fin,'A3_output.png');
clear all
%%
%For the forth image
%First pure black pixel on the left side of the image is found
fin = zeros(480,641,3,'uint8');
A = imread('A4.png');

for row = 1:size(A,1)
    count=1;
    control = 1;
    while control
        if (A(row,count,1) ~= 0) || (A(row,count,2) ~= 0) || (A(row,count,3) ~= 0) || (count < 635)
            count = count + 1;
            if count == 881
                count = 880;
                break
            end
        else
            break
        end
    end
%The non pure black part is shifted to the left.
    for column = 1:641
        fin(row,column,1)=A(row,((count-642)+column),1);
        fin(row,column,2)=A(row,((count-642)+column),2);
        fin(row,column,3)=A(row,((count-642)+column),3);
    end
end

imwrite(fin,'A4_output.png');
clear all
%%
%For the fifth image

a5 = imread('A5.png');
a5_output = a5(end:-1:1, :, :);

imwrite(a5_output, 'A5_output.png');
clear all

