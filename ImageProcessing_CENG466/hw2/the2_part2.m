% Yekta Demirci 2093607
% Zumrud Shukurlu 2174761

b1 = imread('B1.png');
b2 = imread('B2.png');
b3 = imread('B3.png');

% --- B1.png ---


[M, N] = size(b1);

b1_fs = fftshift(fft2(b1));

% bandreject filter with 0 values at specified intervals of distance from the
% center of frequency domain image
filter1 = ones(M, N);

% intervals of distance from the center
% found by trial and error
dist1min = 280;
dist1max = 320;
dist2min = 65;
dist2max = 85;

% center coordinates of freq. domain image
midi = (M-1)/2;
midj = (N-1)/2;

% set filter to 0 for values between specified intervals to reject them
for i=1:M
    for j=1:N
        
        % distance from image center to pixel i, j
        distance = ((i - midi).^2 + (j - midj).^2).^0.5;
        
        if (distance >= dist1min && distance <= dist1max)
            filter1(i, j) = 0;
        elseif (distance >= dist2min && distance <= dist2max)
            filter1(i, j) = 0;   
        end
    end
end

% array  multiplication of freq. domain image and filter
b1_of = b1_fs .* filter1;

b1_output = ifft2(ifftshift(b1_of));

%figure, imshow(uint8(b1_o));

% b1_output values are complex double, take real part
% convert to uint8 to map to [0, 255] intensities
imwrite(uint8(real(b1_output)), 'B1_output.png');


% --- B2.png ---

% the same process as B1.png, 3 intervals are found and set to 0 in the
% bandreject filter

[M, N] = size(b2);

b2_fs = fftshift(fft2(b2));

filter2 = ones(M, N);

% intervals
dist1min = 310;
dist1max = 330;
dist2min= 385;
dist2max = 415;
dist3min = 460;
dist3max = 500;


midi = (M-1)/2;
midj = (N-1)/2;

for i=1:M
    for j=1:N
        
        % distance from image center to pixel i, j
        distance = ((i - midi).^2 + (j - midj).^2).^0.5;
        if (distance >= dist1min && distance <= dist1max)
            filter2(i, j) = 0;
        elseif (distance >= dist2min && distance <= dist2max)
            filter2(i, j) = 0;    
        elseif (distance >= dist3min && distance <= dist3max)
            filter2(i, j) = 0;    
        end
    end
end
   
b2_of = b2_fs .* filter2;
b2_output = ifft2(ifftshift(b2_of));

imwrite(uint8(real(b2_output)), 'B2_output.png');

% --- B3.png ---

[M, N] = size(b3);

b3_fs = fftshift(fft2(b3));

% notch filter that zeroes out spikes on the x axis
filter3 = ones(M, N);

midi = (M-1)/2;
midj = (N-1)/2;

% center coordinates of 4 sparks
% found with trial and error method
spark1 = 575;
spark2 = N - spark1;
spark3 = spark1 - (midj - spark1);
spark4 = spark2 + (spark2 - midj);

% set filter to 0 in the 10x10 proximity of sparks
filter3((midi-10):(midi+10), (spark1-10):(spark1+10)) = 0;
filter3((midi-10):(midi+10), (spark2-10):(spark2+10)) = 0;
filter3((midi-10):(midi+10), (spark3-10):(spark3+10)) = 0;
filter3((midi-10):(midi+10), (spark4-10):(spark4+10)) = 0;

% array multiplication in freq. domain
b3_of = b3_fs .* filter3;

b3_output = ifft2(ifftshift(b3_of));

imwrite(uint8(real(b3_output)), 'B3_output.png');

