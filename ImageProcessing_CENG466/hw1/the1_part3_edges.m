%Zumrud Shukurlu 2174761 & Yekta Demirci 2093607
%Euclidian distance of X and Y matrixes are taken per each pixel
for no = [1,2,3]
    for type = ['R','S']
        A = imread('C'+string(no)+'_'+type+'x.png');
        B = imread('C'+string(no)+'_'+type+'y.png');

        A = cast(A,'double');
        B = cast(B,'double');

        [x,y] = size(A);
        C = zeros(x, y);


        for row = 1:x

            for column = 1:y

               C(row,column) = sqrt( (A(row,column).^2) + (B(row,column).^2) );

            end
        end
        C = cast(C,'uint8');
        imwrite(C,'C'+string(no)+'_'+type+'_edges.png');
    end
end

clear all