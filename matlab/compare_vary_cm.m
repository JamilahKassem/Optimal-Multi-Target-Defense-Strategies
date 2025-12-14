clear;clc;close all;

m=13;
n=5;

Values=0.1:0.01:1;
Cost_base=zeros(size(Values,1));
Cost_kassem=zeros(size(Values,1));
Cost_new=zeros(size(Values,1));
font_size = 18;
font_size_2 = 16;

C=1;
for cm=Values
    Cost_base(C) = base_model( cm,n,m );
    [~,Cost_kassem(C)]  = kassem_model( cm,n,m );
    [~,~,Cost_new(C)]  = new_model( cm,n,m );
    C=C+1;
end
h=figure;
plot(Values,Cost_base,'--','color','red');
hold on;
plot(Values,Cost_new,'color','blue');
plot(Values,Cost_kassem,':','color','black');

Px=4;Py=3;mx=0;my=0;
hold off;
xlabel('Migration Cost cm','FontSize',font_size);
ylabel('Defense Cost','FontSize',font_size);
set(0, 'DefaultAxesFontSize', font_size_2);
xlim([0.1 1]);
xticks([0.1, 0.2, 0.4, 0.6, 0.8, 1]);
grid on;
set(h,'papersize',[Px Py]);
set(h, 'PaperPosition', [mx my Px Py]);
% lgd = legend('Base model','Proposed model','unoptimized model','Position',[0.46 0.65 0.1 0.2],'FontSize',font_size);
% set(lgd,'Box','off');
% lgd.Color = 'none';
% lgd.EdgeColor = 'none';
% legend('Baseline model','Proposed model','Position',[0.32 0.7 0.1 0.2],'FontSize',font_size);
ylim([0 inf]);
print(h,['compare_cm_m_',num2str(m),'_n_',num2str(n),'.pdf'],'-dpdf');