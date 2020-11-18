data = [
    0.50 0.513 0.05 0.023
    1.00 0.561 0.05 0.018
    1.50 0.499 0.05 0.026
    2.00 0.369 0.05 0.019
    2.50 0.218 0.05 0.025
    ];

hold on

x = data(:, 1);
y = data(:, 2);
xEr = data(:, 3);
yEr = data(:, 4);
x0 = 0:0.01:3;

y0 = sin(x0) ./ (sqrt(x0) + 0.5 .* x0); % 定义函数

plot(x0, y0, '-', ...
    'Color', [0.90 0 0.07], ...
    'LineWidth', 1)
errorbar(x, y, yEr, yEr, xEr, xEr, '.', ...
    'Color', [0.27 0.45 0.77], ...
    'LineWidth', 1, ...
    'CapSize', 8); % 误差棒端长度
% 误差图（X，Y，Y-，Y+，X-，X+，各种选项，对应值）

axis([0 3 0 0.6])
xlabel('X(mm)')
ylabel('Y(mm)')
legend('理论曲线', '实验结果')
title('Y与X关系实验结果及理论曲线')
