from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
font_zh = FontProperties(
    fname="/home/zgb/ojy/simhei.ttf")  # 导入中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def func(x, a1, a2, a3, a4):
    return a1*np.sin(a2*(x+a3))+a4  # 自定义要拟合的函数


data = np.array(pd.read_csv("/home/zgb/ojy/SCUPT/data.csv"))  # 从csv文件获取数据
x0 = np.array(data[:, 0])
y0 = np.array(data[:, 1])
r = abs(y0 / 3) + 4
x = np.linspace(0, 3, 300)

popt, pcov = curve_fit(func, x0, y0)
a1 = popt[0]
a2 = popt[1]
a3 = popt[2]
a4 = popt[3]
print(a1, a2, a3, a4)
y = func(x, a1, a2, a3, a4)
# 进行拟合，获得四个系数，并构建函数

plt.figure(figsize=(8, 4))
plt.scatter(x0, y0, r, marker='o',
            color='r',
            label="实验结果")  # 绘制散点图
plt.plot(x, y, 'b',
         linewidth=1,
         label="拟合曲线")

plt.xlabel("T(S)")
plt.ylabel("X(mm)")
plt.legend(prop=font_zh)
plt.title("摩擦振子实验结果及正弦拟合", fontproperties=font_zh, fontsize=16)
plt.savefig(__file__+'.svg')
