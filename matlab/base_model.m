function [ C ] = base_model( cm,n,m )
    C = m/n + cm * m * n * (1 - 1/n)^2;
end

