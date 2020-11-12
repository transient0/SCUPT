import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
font_zh = FontProperties(
    fname="/home/zgb/ojy/simhei.ttf")  # 导入中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = np.array([
    [34.8, 0.5985, 0.6214],
    [39.9, 0.5872, 0.6107],
    [45.0, 0.5765, 0.6004],
    [50.0, 0.5658, 0.5895],
    [54.9, 0.5555, 0.5800],
    [59.9, 0.5453, 0.5696],
    [64.9, 0.5326, 0.5595]
])  # 数据从Excel粘贴以后需要添加逗号和括号

x = np.array(data[:, 0])  # 提取列数据
y1 = np.array(data[:, 1])
y2 = np.array(data[:, 2])
t = np.linspace(30, 70, 40)  # 线性列表（开始，结束，分段数）

f1 = np.polyfit(x, y1, 1)  # 多项式拟合（X，Y，次数）返回系数
p1 = np.poly1d(f1)  # 构成多项式（F）返回一个多项式函数
f2 = np.polyfit(x, y2, 1)
p2 = np.poly1d(f2)

plt.plot(t, p1(t), '-',                   # 直线型
         color=(0.93, 0.49, 0.19),        # 颜色
         linewidth=1,                     # 线宽
         label="$I_F=100 \mu A$ 线性拟合")
plt.plot(x, y1, 'o',                      # 圆形
         color=(0.44, 0.68, 0.28),
         markersize=4,                    # 标记大小
         label="$I_F=100 \mu A$ 实验结果")
plt.plot(t, p2(t), '-',
         color=(0.90, 0, 0.07),
         linewidth=1,
         label="$I_F=200 \mu A$ 线性拟合")
plt.plot(x, y2, 'o',
         color=(0.27, 0.45, 0.77),
         markersize=4,
         label="$I_F=200 \mu A$ 实验结果")
# 绘图（X，Y，线型点型，各种选项=对应值）

plt.axis([30, 70, 0.52, 0.64])
plt.xlabel("$T(^\circ C)$")  # X轴标签
plt.ylabel("$U_F(V)$")  # Y轴标签
plt.legend(prop=font_zh)  # 添加图例，并设置中文字体
plt.title("$U_F$与$T$关系实验结果及线性拟合",
          fontproperties=font_zh,
          fontsize=16)  # 添加标题，并设置中文字体
plt.savefig(__file__+'.svg')  # 保存图片
