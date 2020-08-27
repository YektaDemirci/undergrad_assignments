% Zumrud Shukurlu 2174761 & Yekta Demirci 2093607


b1 = imread('B1.png');
b2 = imread('B2.png');
b1_ref = imread('B1_ref.png');
b2_ref = imread('B2_ref.png');

% --- HISTOGRAM EQUALIZATION for B2.png ---

rows = size(b2, 1);
cols = size(b2, 2);

b2_output = zeros(rows, cols, 'uint8');
MN = rows*cols;
L = 256;

% array for frequency of pixels with intensity i
freq = zeros(L, 1);

% cumulative distribution function
% s_k = T(r_k) = (L - 1) * sum_{j=0}^k p_r(r_j)
cdf = zeros(L, 1);
cum = zeros(L, 1);
% matching function
s = zeros(L, 1);

for i = 1:rows
    for j = 1:cols
        r_k = b2(i, j);
        % freq(r_k + 1) because intensity can be 0, but no 0 index in
        % matlab
        % increment
        freq(r_k + 1) = freq(r_k + 1) + 1;  
    end
end

% sum of frequencies
sum = 0;

for i=1:L
    sum = sum + freq(i);
    cum(i) = sum;
    cdf(i) = cum(i)/MN;
    s(i) = round(cdf(i)*(L-1));
end

for i = 1:rows
    for j = 1:cols
        b2_output(i, j) = s(b2(i, j) + 1);
    end
end

hist = histogram(b2_output);
imwrite(b2_output, 'B2_histeq_output.png');
saveas(hist, 'B2_histeq.png');

% --- HISTOGRAM MATCHING for B2.png ---

b2_histmatch = zeros(rows, cols, 'uint8');
freq_ref = zeros(L, 1);
cdf_ref = zeros(L, 1);
cum_ref = zeros(L, 1);
rows_ref = size(b2_ref, 1);
cols_ref = size(b2_ref, 2);
MN_ref = rows_ref * cols_ref;
% mapping from original image intensities to reference image intensities
map = zeros(L, 1, 'uint8');

for i = 1:rows_ref
    for j = 1:cols_ref
        r_k = b2_ref(i, j);
        freq_ref(r_k + 1) = freq_ref(r_k + 1) + 1;     
    end
end

sum = 0;

for i=1:L
    sum = sum + freq_ref(i);
    cum_ref(i) = sum;
    cdf_ref(i) = cum_ref(i)/MN_ref;
end

for i = 1:L
    [~, temp] = min(abs(cdf(i) - cdf_ref));
    map(i) = temp - 1;
end

b2_histmatch = map(b2 + 1);

imwrite(b2_histmatch, 'B2_histmatch_output.png');
hist = histogram(b2_histmatch);
saveas(hist, 'B2_histmatch.png');


% --- HISTOGRAM EQUALIZATION for B1.png ---

rows = size(b1, 1);
cols = size(b1, 2);
b1_output = zeros(rows, cols, 3, 'uint8');
MN = rows*cols;
L = 256;

freq = zeros(L, 3);
% probability density function 
% p_r(r_k) = n_k/(M*N)
% cumulative distribution function
% s_k = T(r_k) = (L - 1) * sum_{j=0}^k p_r(r_j) 
% cdf is the sum part
cdf = zeros(L, 3); 
cum = zeros(L, 3);
s = zeros(L, 3);

for i = 1:rows
    for j = 1:cols
        for k = 1:3
            r_k = b1(i, j, k);
            % freq(r_k + 1) because intensity can be 0, but no 0 index in
            % matlab
            % increment
            freq(r_k + 1, k) = freq(r_k + 1, k) + 1; 
        end
    end
end

% sum of frequencies

for j = 1:3
    sum = 0;
    for i=1:L
        sum = sum + freq(i, j);
        cum(i, j) = sum;
        cdf(i, j) = cum(i, j)/MN;
        s(i, j) = round(cdf(i, j)*(L-1));
    end
end

for i = 1:rows
    for j = 1:cols
        for k = 1:3
        b1_output(i, j, k) = s(b1(i, j, k) + 1, k);
        end
    end
end

hist = histogram(b1_output);
imwrite(b1_output, 'B1_histeq_output.png');
saveas(hist, 'B1_histeq.png');

% --- HISTOGRAM MATCHING for B1.png ---

b1_histmatch = zeros(rows, cols, 3, 'uint8');
freq_ref = zeros(L, 3);
cdf_ref = zeros(L, 3);
cum_ref = zeros(L, 3);
rows_ref = size(b1_ref, 1);
cols_ref = size(b1_ref, 2);
MN_ref = rows_ref * cols_ref;
% mapping from original image intensities to reference image intensities
map = zeros(L, 3, 'uint8');

for i = 1:rows_ref
    for j = 1:cols_ref
        for k = 1:3
            r_k = b1_ref(i, j, k);
            % freq(r_k + 1) because intensity can be 0, but no 0 index in
            % matlab
            % increment
            freq_ref(r_k + 1, k) = freq_ref(r_k + 1, k) + 1;  
        end
    end
end

% sum of frequencies
%sum = 0;

for j = 1:3
    sum = 0;
    for i=1:L
        sum = sum + freq_ref(i, j);
        cum_ref(i, j) = sum;
        cdf_ref(i, j) = cum_ref(i, j)/MN_ref;
    end
end

% subtract each element of cdf of original image from cdf of ref image and
% get the minimum from the difference array
for i = 1:L
    for j = 1:3
    [~, temp] = min(abs(cdf(i, j) - cdf_ref(:, j)));
    map(i, j) = temp - 1;
    end
end

b1_histmatch = map(b1 + 1);

imwrite(b1_histmatch, 'B1_histmatch_output.png');
hist = histogram(b1_histmatch);
saveas(hist, 'B1_histmatch.png');


