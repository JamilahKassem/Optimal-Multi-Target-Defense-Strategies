clear;clc;close all;

m=13;
cm=1/4;
% cm=1/40;

Values=2:15;
Cost_base=zeros(size(Values,1));
Cost_kassem=zeros(size(Values,1));
Cost_new=zeros(size(Values,1));
font_size = 22;
font_size_2 = 20;

C=1;
for n=Values
    Cost_base(C) = base_model( cm,n,m );
    [~,Cost_kassem(C)]  = kassem_model( cm,n,m );
    [~,~,Cost_new(C)]  = new_model( cm,n,m );
    C=C+1;
end
h=figure;
plot(Values,Cost_base,'--','color','red');
hold on;
plot(Values,Cost_new,'color','blue');
plot(Values,Cost_kassem,":",'color','black');

Px=4;Py=3;mx=0;my=0;
hold off;
xlabel('Number of Nodes n','FontSize',font_size);
ylabel('Defense Cost','FontSize',font_size);
set(0, 'DefaultAxesFontSize', font_size_2);
grid on;
xlim([2 15]);
xticks([2, 5, 10, 15]);
set(h,'papersize',[Px Py]);
set(h, 'PaperPosition', [mx my Px Py]);
% lgd = legend('Base model','Proposed model','unoptimized model','Position',[0.46 0.65 0.1 0.2],'FontSize',font_size);
% set(lgd,'Box','off');
% lgd.Color = 'none';
% lgd.EdgeColor = 'none';
% legend('Baseline model','Proposed model','Position',[0.32 0.7 0.1 0.2],'FontSize',font_size);
ylim([0 inf]);
print(h,['compare_n_m_',num2str(m),'_cm_',num2str(cm),'.pdf'],'-dpdf');