from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
font_zh = FontProperties(
    fname="/home/zgb/ojy/simhei.ttf")  # 导入中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def func(x, a, b, c, d):
    return a*np.sin(b*(x+c))+d  # 自定义要拟合的函数


data = np.array(pd.read_csv("/home/zgb/ojy/SCUPT/data.csv"))  # 从csv文件获取数据
x0 = np.array(data[:, 0])
y0 = np.array(data[:, 1])
x = np.linspace(0, 3, 300)

popt, pcov = curve_fit(func, x0, y0)
a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]
y = func(x, a, b, c, d)
# 进行拟合，获得四个系数，并构建函数

plt.figure(figsize=(8, 4))
plt.scatter(x0, y0, 16, marker='o',
            color='r',
            label="实验结果")  # 绘制散点图
plt.plot(x, y, 'b',
         linewidth=1,
         label="拟合曲线")

plt.legend(prop=font_zh)
plt.title("摩擦振子实验结果及正弦拟合", fontproperties=font_zh, fontsize=16)
plt.savefig(__file__+'.svg')
