import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from matplotlib.font_manager import FontProperties
font_zh = FontProperties(
    fname="/home/zgb/ojy/simhei.ttf")  # 导入中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = np.array([
    [0.000, 107.702],
    [0.067, 114.925],
    [0.083, 120.895],
    [0.100, 123.702],
    [0.117, 124.802],
    [0.133, 121.033],
    [0.150, 114.806],
    [0.167, 107.162],
    [0.184, 99.188],
    [0.200, 91.974],
    [0.217, 87.502],
    [0.234, 86.721],
    [0.250, 89.124],
    [0.267, 95.322],
    [0.284, 102.978],
    [0.300, 110.784],
    [0.317, 117.688],
    [0.334, 122.489],
    [0.350, 125.049],
    [0.367, 122.432],
    [0.384, 118.139],
    [0.400, 111.824],
    [0.417, 103.938],
    [0.434, 95.428],
    [0.450, 89.431],
    [0.467, 86.695],
    [0.484, 86.820],
    [0.501, 91.506],
    [0.517, 98.348],
    [0.534, 106.164],
    [0.551, 113.841],
    [0.567, 119.812],
    [0.584, 123.752],
    [0.601, 123.563],
    [0.617, 120.862],
    [0.634, 115.670],
    [0.651, 108.619],
    [0.667, 100.322],
    [0.684, 92.441],
    [0.701, 88.032],
    [0.717, 86.529],
    [0.734, 88.550],
    [0.751, 94.271],
    [0.767, 101.576],
    [0.784, 109.477],
    [0.801, 116.915],
    [0.817, 121.809],
    [0.834, 123.872],
    [0.851, 123.762],
    [0.868, 119.068],
    [0.884, 112.879],
    [0.901, 105.131],
    [0.918, 96.428],
    [0.934, 90.406],
    [0.951, 86.905],
    [0.968, 86.210],
    [0.984, 90.744],
    [1.001, 96.988],
    [1.018, 104.966],
    [1.034, 112.594],
    [1.051, 119.001],
    [1.068, 123.777],
    [1.084, 124.140],
    [1.101, 121.572],
    [1.118, 116.495],
    [1.134, 109.555],
    [1.151, 100.814],
    [1.168, 93.400],
    [1.185, 88.437],
    [1.201, 85.964],
    [1.218, 87.732],
    [1.235, 93.076],
    [1.251, 100.375],
    [1.268, 108.217],
    [1.285, 115.658],
    [1.301, 121.098],
    [1.318, 124.578],
    [1.335, 124.460],
    [1.351, 119.828],
    [1.368, 114.029],
    [1.385, 106.187],
    [1.401, 98.350],
    [1.418, 91.179],
    [1.435, 86.154],
    [1.451, 86.256],
    [1.468, 89.616],
    [1.485, 95.893],
    [1.502, 103.549],
    [1.518, 111.586],
    [1.535, 118.376],
    [1.552, 122.653],
    [1.568, 124.917],
    [1.585, 123.197],
    [1.602, 117.538],
    [1.618, 110.985],
    [1.635, 102.964],
    [1.652, 94.606],
    [1.668, 89.003],
    [1.685, 86.416],
    [1.702, 87.331]
])


def func(x, a, b, c, d):
    return a*np.sinc(b*(x+c))+d


x0 = np.array(data[:, 0])
y0 = np.array(data[:, 1])
x = np.linspace(0, 1.8, 180)

popt, pcov = curve_fit(func, x0, y0)
a = popt[0]
b = popt[1]
c = popt[2]
d = popt[3]
y = func(x, a, b, c, d)

plt.scatter(x0, y0, marker='o', c='r')
plt.plot(x, y, 'b')
plt.show()