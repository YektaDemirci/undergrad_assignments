function [coefs,top,top2,coefs2] = filtre(N,P,a,var)
    for i = (1:N)

    Rdx(i)=(1/(1-(a)^2))*a^abs(i-1);
    Rdx2(i)=(1/(1-(a)^2))*a^abs(i-1+2);


    end
    
    Rx=Rdx;
    
    Rx(1)=Rx(1)+var^2;

    for i = (1:P)

        for j = (1:P)

            bigR(i,j) = Rx(abs(i-j)+1);

        end

    end

    coefs= inv(bigR)*transpose(Rdx(1:P));
    coefs2= inv(bigR)*transpose(Rdx2(1:P));

    top=Rdx(1);
    top2=0
    
    for i = (1:P)
        top2=top2+(coefs(i)*Rdx(i));
    end
    
end
    