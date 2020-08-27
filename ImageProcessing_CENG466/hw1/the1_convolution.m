%Zumrud Shukurlu 2174761 & Yekta Demirci 2093607
function [result] = the1_convolution(input,kernel)
%According to the size of the kernel two different approach is followed
%For the 2x2 sizes, input is reflected on the rightest and lowest indexes
%Also convolution result is put to the left top point according to kernel
%For the 3x3 sizes result is putted into the middle according to kernel
%Also input is reflected at all edges to not miss any point during
%convolution
input = cast(input,'double');

[xKernel,yKernel] = size(kernel);
[xInput,yInput] = size(input);
result = zeros(xInput, yInput);
    if xKernel == 2
        
        input = [input input(:,yInput)];
        input = [input ; input(xInput,:)];

        for column1 =  1:yInput
            for row1 =  1:xInput
                
                carpim = input(row1:row1+(xKernel-1),column1:column1+(yKernel-1)).*kernel;            
                result(row1,column1)= sum(carpim ,'all');
                
            end
        end
        
    else
        input = [input(:,1) input];
        input = [input input(:,yInput)];
        input = [input(1,:) ; input];
        input = [input ; input(xInput,:)];
        
        for column2 =  1:yInput
            for row2 =  1:xInput
                
                carpim2= input(row2:row2+(xKernel-1),column2:column2+(yKernel-1)).*kernel;
                result(row2,column2) = sum(carpim2 ,'all');
                
            end
        end
        
    end

end