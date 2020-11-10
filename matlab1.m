data = [
    34.8	0.5985	0.6214
    39.9	0.5872	0.6107
    45.0	0.5765	0.6004
    50.0	0.5658	0.5895
    54.9	0.5555	0.5800
    59.9	0.5453	0.5696
    64.9	0.5326	0.5595
    ]; % 数据可以直接从Excel粘贴

hold on% 添加新绘图时保留当前绘图

x = data(:, 1); % 提取列数据
y1 = data(:, 2);
y2 = data(:, 3);
t = 30:1:70; % 线性列表（开始：间隔：结束）

f1 = polyfit(x, y1, 1); % 多项式拟合（X，Y，次数）返回系数
p1 = polyval(f1, t); % 多项式计算（F，t）返回F在t处的值
f2 = polyfit(x, y2, 1);
p2 = polyval(f2, t);

plot(t, p1, '-', ...% 实线型
'Color', [0.93 0.49 0.19], ...% 颜色
'LineWidth', 1)% 线宽
plot(x, y1, 'o', ...% 圆形
'MarkerFaceColor', [0.44 0.68 0.28], ...% 标记填充颜色
'MarkerEdgeColor', 'w', ...% 标记边缘颜色
'MarkerSize', 6)% 标记大小
plot(t, p2, '-', ...
    'Color', [0.90 0 0.07], ...
    'LineWidth', 1)
plot(x, y2, 'o', ...
    'MarkerFaceColor', [0.27 0.45 0.77], ...
    'MarkerEdgeColor', 'w', ...
    'MarkerSize', 6)
% 绘图（X，Y，线型点型，各种选项，对应值）

axis([30 70 0.52 0.64])
xlabel('{T(^\circ C)}')% X轴标签
ylabel('{U_F(V)}')% Y轴标签
legend('{I_F=100\muA}线性拟合', '{I_F=100\muA}实验结果', '{I_F=200\muA}线性拟合', '{I_F=200\muA}实验结果')% 添加图例
title('{U_F}与{T}关系实验结果及线性拟合')% 添加标题
