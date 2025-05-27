function [Nm,C] = kassem_model( cm,n,m )
    m_mod_n = mod(m,n);
    Nm = (ceil(m/n) * m_mod_n) * (n - m_mod_n + 1);
    delta = 1 - m/(n * ceil(m/n)) - 1/(2*cm);
    if( delta>0 && delta <= (1 -  m/(n*ceil(m/n)) ))
        C = m/n + Nm * m_mod_n * ceil(m/n) * (1 - m/(n * ceil(m/n)) - 1/(4*cm));
    else
        C = m/n + Nm * cm * m_mod_n * ceil(m/n) * (1 - m/(n * ceil(m/n)))^2;
    end
end