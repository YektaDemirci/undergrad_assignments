% Yekta Demirci 2093607 & Zumrud Shukurlu 2174761

A1 = imread('A1.png');
A2 = imread('A2.png');
A3 = imread('A3.png');
A4 = imread('A4.png');
A5 = imread('A5.png');

% grayscale images
A1_gray = rgb2gray(A1);
A2_gray = rgb2gray(A2);
%A3_gray = rgb2gray(A3);
A4_gray = rgb2gray(A4);
A5_gray = rgb2gray(A5);

% elem<i> : disk shaped structuring element with radius r 
% make the element logical so that it can be used for logical indexing of
% the image matrix

% --- A1.png ---
elem1 = logical(disk(20));
elem11 = logical(disk(4));

temp1 = imbinarize(dilation(bottomhat(A1_gray, elem1), elem11));
[~, n] = bwlabel(temp1);
fprintf("The number of flying balloons in image A1 is %d\n", n);
imwrite(temp1, 'part1_A1.png');

% --- A2.png ---
temp2 = imbinarize(opening(bottomhat(A2_gray, elem1), elem11));
[~, n] = bwlabel(temp2);
fprintf("The number of flying balloons in image A2 is %d\n", n);
imwrite(temp2, 'part1_A2.png');

% --- A3.png ---
% TAKES TOO LONG TO RUN
elem3 = logical(disk(40));
elem31 = logical(disk(2));
elem32 = logical(disk(10));
elem33 = logical(disk(3));

A3_gray = A3(:, :, 1);
temp3 = smoothing(A3_gray, elem32, elem32);
temp3 = bottomhat(temp3, elem3);
temp3 = imbinarize(temp3);
temp3 = [temp3(1:350, :) ; zeros(90, size(temp3, 2))];
temp3 = erosion(temp3, elem31);
temp3 = dilation(temp3, elem33);
temp3 = logical(temp3);
[~, n] = bwlabel(temp3);
fprintf("The number of flying balloons in image A3 is %d\n", n);
imwrite(temp3, 'part1_A3.png');

% --- A4.png ---
elem4 = logical(disk(40));
elem42 = logical(disk(5));

temp4 = bottomhat(A4_gray, elem4);
temp4 = opening(imbinarize(temp4), elem42);
temp4 = [temp4(1:200, :); zeros(58, size(A4_gray, 2))];
[~, n] = bwlabel(temp4);
fprintf("The number of flying balloons in image A4 is %d\n", n);
%figure, imshow(logical(temp4));
imwrite(logical(temp4), 'part1_A4.png');


% --- A5.png ---
elem5 = logical(disk(20));
temp5 = smoothing(A5_gray, logical(disk(3)), logical(disk(2)));
temp5 = bottomhat(temp5, elem5);
temp5 = imbinarize(temp5);
temp5 = opening(temp5, logical(disk(1)));
temp5 = dilation(temp5, logical(disk(2)));
temp5 = logical(temp5);
[~, n] = bwlabel(temp5);
fprintf("The number of flying balloons in image A5 is %d\n", n);
imwrite(temp5, 'part1_A5.png');



% --- MORPHOLOGICAL OPERATIONS ---
% f - image, b - (logical) flat structuring element
function [output] = tophat(f, b)
    output = f - opening(f, b);
end

function [output] = bottomhat(f, b)
    output = closing(f, b) - f;
end

function [output] = gradient(f, b)
    output = dilation(f, b) - erosion(f, b);
end

function [output] = smoothing(f, b1, b2)
    output = closing(opening(f, b1), b2);
end

function [output] = opening(f, b)
    output = dilation(erosion(f, b), b);
end

function [output] = closing(f, b)
    output = erosion(dilation(f, b), b);
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

% otsu thresholding function, output is the thresholded image
function [output] = otsu(f)
    [rows, cols] = size(f); 
    MN = rows*cols;
    L = 256;
    % histogram
    freq = zeros(L, 1);    
    for i = 1:rows
        for j = 1:cols
            r_k = f(i, j);      
            freq(r_k + 1) = freq(r_k + 1) + 1;
        end
    end    
    % normalized histogram
    freq = freq ./ MN;    
    % cumulative histogram
    cum_sum = zeros(L, 1);
    for i = 1:L
        cum_sum(i) = cum_sum(i) + freq(i);
    end   
    % cumulative mean - average intensity up to level i for each i
    cum_mean = zeros(L, 1);
    sum = 0;
    for i = 1:L
        sum = sum + freq(i) * i;
        cum_mean(i) = sum;
    end   
    % global intensity mean - average intensity of the entire image
    global_mean = cum_mean(L);  
    % between-class variance
    variance_b = zeros(L, 1);    
    for i = 1:L
        variance_b(i) = ((global_mean * cum_sum(i) - cum_mean(i)) .^2) / (cum_sum(i) * (1 - cum_sum(i)));
    end    
    % otsu threashold value k
    [~, k1] = max(variance_b);
    if (size(k1) == 1)
        k = k1;
        
    elseif (size(k1) > 1)
        k = mean(k1);
    end    
    % global variance
    %global_variance = 0;
    %for i = 1:L
    %    global_variance = global_variance + (i - global_mean) .^ 2 * freq(i);
    %end    
    % separability measure - not used
    % sep = variance_b(k) / global_variance;
    %
    output = zeros(rows, cols);
    for i = 1:rows
        for j = 1:cols
            if (f(i, j) < k)
                output(i, j) = 0;
            else
                output(i, j) = 1;
            end
        end
    end
end





        













    
    
        
