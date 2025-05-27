function [Nm] = NumberofMoves(m,n)
    if m<2 || n < 2
        Nm = m * n;
    else
        if m>n
            Nm = n;
            Nm = Nm + NumberofMoves(m-n,n);
        else
            Nm = m;
            Nm = Nm + NumberofMoves(m,n-m);
        end
    end
end

