data = csvread('data.csv', 1, 0);
hold on

x0 = data(:, 1);
y0 = data(:, 2);
x = 0:0.01:3;

func = @(a, x)a(1) * sin(a(2) * (x + a(3))) + a(4);
p = lsqcurvefit(func, [-30, 5, 0, 0], x0, y0)
y = func(p, x);

scatter(x0, y0, 16, 'o', 'filled', 'MarkerFaceColor', 'r')
plot(x, y, '-', ...% 实线型
'Color', 'b', ...% 颜色
'LineWidth', 1)% 线宽
