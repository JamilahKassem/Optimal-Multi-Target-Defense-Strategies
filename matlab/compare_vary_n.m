clear;clc;close all;

m=13;
cm=1/4;
% cm=1/40;

Values=2:15;
Cost_base=zeros(size(Values,1));
Cost_kassem=zeros(size(Values,1));
Cost_new=zeros(size(Values,1));

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
plot(Values,Cost_kassem,'color','black');

hold off;
xlabel('Number of Nodes n');
ylabel('Defense Cost');
set(h,'papersize',[5 4]);
set(h, 'PaperPosition', [-0.5 0 5 4]);
legend('Base model','Proposed model','Kassem model','Position',[0.37 0.7 0.1 0.2]);
fontsize(16,"points");
ylim([0 inf]);
print(h,['compare_n_m_',num2str(m),'_cm_',num2str(cm),'.svg'],'-dsvg');