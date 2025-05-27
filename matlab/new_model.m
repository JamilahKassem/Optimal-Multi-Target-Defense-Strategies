function [S,Nm,C] = new_model( cm,n,m )
    m_mod_n = mod(m,n);
    if(m_mod_n==0)
        Nm = 0;
    else
        Nm = NumberofMoves(m_mod_n*ceil(m/n),n-m_mod_n) + m_mod_n*ceil(m/n);
    end
    if cm > 1/ (2*Nm*m_mod_n*(ceil(m/n)-m/n))
        coefficient = 4*Nm*m_mod_n*ceil(m/n);
        C=m/n + 1 - m/(n*ceil(m/n)) - 1 / (cm * coefficient);
        S=1;
    else
        coefficient = Nm * m_mod_n * ceil(m/n)*(1-m/(n*ceil(m/n)))^2;
        C=m/n+cm*coefficient;
        S=2;
    end
end