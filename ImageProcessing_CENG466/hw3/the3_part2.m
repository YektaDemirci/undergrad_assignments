% Yekta Demirci 2093607 & Zumrud Shukurlu 2174761

B1 = imread('B1.png');
B2 = imread('B2.png');
B3 = imread('B3.png');

B1gray = rgb2gray(B1);
%B2gray = rgb2gray(B2);
B3gray = rgb2gray(B3);

% --- B3.png --- 
% pixel_labels - output of kmeans applied image
temp = segmentation_function(B3gray, 3, 10, 10);

% show the found borders to the original image
temp2 = B3;
[r, c] = size(temp);
for i = 1:r
    for j = 1:c
            if (temp(i, j) == 1)
                for t = 1:3
                    temp2(i, j, t) = 255;
                end
            end
    end
end

imwrite(temp2, 'the3_B3_output.png');
%figure, imshow(temp2);

% SIMILAR OPERATIONS ARE DONE FOR THE OTHER TWO IMAGES
% --- B1.png ---
% kmeans
temp = segmentation_function(B1gray, 1, 5, 5);

temp2 = B1;
[r, c] = size(temp);
for i = 1:r
    for j = 1:c
            if (temp(i, j) == 1)
                for t = 1:3
                    temp2(i, j, t) = 255;
                end
            end
    end
end

imwrite(temp2, 'the3_B1_output.png');

% --- B2 ---
% blue component gave better result
B2gray = B2(:, :, 3);

temp = segmentation_function(B2gray, 2, 8, 12);

temp2 = B2;
[r, c] = size(temp);
for i = 1:r
    for j = 1:c
            if (temp(i, j) == 1)
                for t = 1:3
                    temp2(i, j, t) = 255;
                end
            end
    end
end

imwrite(temp2, 'the3_B2_output.png');

function [output] = gradient(f, b)
    output = dilation(f, b) - erosion(f, b);
end

function [output] = opening(f, b)
    output = dilation(erosion(f, b), b);
end

function [output] = dilation(f, b)
    output = zeros(size(f, 1), size(f, 2), 'uint8');
    [rows_b, cols_b] = size(b);
    f = pad(f, b);
    
    [rows, cols] = size(f);
    for i = 1:(rows - rows_b)
        for j = 1:(cols - cols_b)
            % subsection of the image that is under the structuring element
            subsection = f(i:i+rows_b, j:j+cols_b);
            % b : str.element, defined as logical, consists of only 1s and 0s
            
            % subsection(b) : extract the elements of subsection corresponding
            % to the nonzero values of b, 
            % write 0 to the remaining. 
            
            % max : gives the top surface of the topographic view of the
            % image
            output(i, j) = max(subsection(b));          
        end
    end
end

function [output] = erosion(f, b)
    output = zeros(size(f, 1), size(f, 2), 'uint8');
    [rows_b, cols_b] = size(b);
    f = pad(f, b);
    [rows, cols] = size(f);
    
    for i = 1:(rows - rows_b)
        for j = 1: (cols - cols_b)
            subsection = f(i:i+rows_b, j:j+cols_b);
            output(i, j) = min(subsection(b));
        end
    end
end

% --- HELPER FUNCTIONS ---

% disk shaped structuring element with radius r
function [output] = disk(r)
    dim = 2*r + 1; % dimension of structuring element matrix 
    output = zeros(dim, dim);

    mid = (dim+1)/2;
    % put one to elements within the radius r
    for i = 1:dim
        for j = 1:dim
            distance = ((i - mid).^2 + (j - mid).^2).^0.5; 
            if (distance <= r)
                output(i, j) = 1;
            end
        end
    end
end

% pad image f with its bordering elements with respect to the size of kernel b
function [output] = pad(f, b)
    [rows, cols] = size(f);
    [rows_b, ~] = size(b);
    % assume a square structuring element so that padsize is 
    % the same for both dimenstions
    padsize = (rows_b - 1)/2;
    %halfpadsize = floor(padsize/2);
    f = [f(:, 1:padsize) f];
    f = [f f(:, (cols-padsize):cols)];
    f = [f(1:padsize, :) ; f];
    f = [f ; f((rows-padsize):rows, :)];
    output = f;
end

% f - grayscale image
% imno - specifies the image, if image does not have the desired colors
% after kmeans, complement the image. 
% r1 - radius of disk used for erosion
% r2 - radius of disk used for dilation
function [output] = segmentation_function(f, imno, r1, r2)
    fdouble = double(f);
    [rows, cols] = size(f);

    temp = reshape(fdouble,rows*cols,1);
    
    % k - number of clusters
    k = 2;

    [cluster_idx, ~] = kmeans(temp, k,'distance','sqEuclidean', 'Replicates', 3);

    % clustered image
    output = reshape(cluster_idx,rows,cols);
    % convert label image to binary image
    output = imbinarize(mat2gray(output));
    
     if (imno == 2)
         check = 1;
     else
         check = 0;
     end
    
    % kmeans labels and colors are random, we check the output image not to be the
    % negative image of what we desired: morphological operations depends on
    % the colors
    % if so, change colors
    if output(1, 1) == check
        output = ~output;
    end

    output = uint8(output);

    elem4 = logical(disk(r1));
    elem5 = logical(disk(r2));
    temp = erosion(output, elem4);
    temp = dilation(temp, elem5);
    temp = gradient(temp, logical(disk(1)));
    
    output = temp;
end


