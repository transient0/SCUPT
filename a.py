
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

data = np.array(pd.read_csv("D:\WORK\GitHub\SCUPT\\a.csv"))
t = np.array(data[:, 0])
x1 = np.array(data[:, 1])+40
x2 = np.array(data[:, 2])-40


plt.figure(figsize=(12, 4))

plt.plot(t, x1, '-',
         linewidth=1,
         label="前期")
plt.plot(t, x2, '-',
         linewidth=1,
         label="后期")

plt.xlabel("$t$(s)")
plt.ylabel("$x$(mm)")
plt.legend()
plt.title("摩擦振子实验前期与后期对比", fontsize=20)
plt.show()
