data = csvread('data.csv', 1, 0);
hold on

x0 = data(:, 1);
y0 = data(:, 2);
r = abs(y0 ./ 3) +4;
x = 0:0.01:3;

func = @(a, x)a(1) * sin(a(2) * (x + a(3))) + a(4);
p = lsqcurvefit(func, [-30, 5, 0, 0], x0, y0)
y = func(p, x);

scatter(x0, y0, r, 'o', 'filled', 'MarkerFaceColor', 'r')%绘制散点图
plot(x, y, '-', ...% 实线型
'Color', 'b', ...% 颜色
'LineWidth', 1)% 线宽

xlabel('T(S)')
ylabel('X(mm)')
legend('实验结果', '拟合曲线')
title('摩擦振子实验结果及正弦拟合')
