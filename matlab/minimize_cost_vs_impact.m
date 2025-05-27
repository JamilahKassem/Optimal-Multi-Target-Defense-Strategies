clear;
close all;
% define number of nodes and networks
m=4;
n=3;

m_mod_n = mod(m,n);
Nm = ceil(m/n) * m_mod_n * (1 - 1 / (n - m_mod_n)) * (ceil((n-m_mod_n)/(ceil(m/n)*m_mod_n))+1);
Nm = Nm + ceil((n-m_mod_n)/(ceil(m/n)*m_mod_n*(1-1/(n-m_mod_n))));
Model_coefficient = Nm * m_mod_n * ceil(m/n)*(1-m/(n*ceil(m/n)))^2;
Math_Model_coefficient = 4*Nm*m_mod_n*ceil(m/n);

start = 1/ (2*Nm*m_mod_n*(ceil(m/n)-m/n));

cms=0.1:0.01:2;
% initiate matrices for costs
skip = floor(start/0.01)-9;
Math_Model=zeros(size(cms,2)-skip,1);
Model=zeros(size(cms,2),1);

C=1;%counter coefficient
for cm=cms
    if(cm>start)
        Math_Model(C-skip)=m/n + 1 - m/(n*ceil(m/n)) - 1 / (cm * Math_Model_coefficient);
    end
    Model(C)=m/n+cm*Model_coefficient;
    C=C+1;
end
h=figure;
plot(cms,Model);
hold on;
plot(cms(:,skip+1:end),Math_Model);
hold off;
xlabel('Migration cost');
ylabel('Total defense cost');
ylim([0 inf])
legend('Minimized impact','Minimized cost','Position',[0.6 0.2 0.1 0.2]);
fontsize(16,"points");
set(h,'papersize',[5 4]);
set(h, 'PaperPosition', [-0.5 0 5 4]);
fontsize(16,"points");
print(h,'cost_with_defense_variation','-dpdf');