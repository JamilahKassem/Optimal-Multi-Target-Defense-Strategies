function [matrix] = form_matrix(m,n)
    if m==0 || n==0
        fprintf("error cannot create matrix with size 0\n");
        matrix=ones(m,n);
    else
        matrix=zeros(m,n);
        if m==1 || n ==1
            matrix=ones(m,n);
        else
            min = m;
            if m>n
                min = n;
                matrix(n+1:m,1:n) = form_matrix(m-n,n);
            else
                matrix(1:m,m+1:n) = form_matrix(m,n-m);
            end
            for i=1:min
               matrix(i,i)=min;
            end
        end
    end
end

