import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 定义数据点
snr_5m = np.array([0, 6, 8, 10])  # 加入原点 (0, 0)
rate_5m = np.array([0, 75, 82, 85])  # 加入原点 (0, 0)

snr_10m = np.array([0, 6, 8, 10])  # 加入原点 (0, 0)
rate_10m = np.array([0, 70, 75, 78])  # 加入原点 (0, 0)

# 创建插值函数，使曲线平滑
interp_5m = interp1d(snr_5m, rate_5m, kind='cubic')
interp_10m = interp1d(snr_10m, rate_10m, kind='cubic')

# 创建一个更密集的信杂比范围用于绘制平滑曲线
snr_new = np.linspace(0, 10, 500)

# 创建图形
plt.figure()

# 绘制 5m 的平滑曲线
plt.plot(snr_new, interp_5m(snr_new), label='5m')

# 绘制 10m 的平滑曲线
plt.plot(snr_new, interp_10m(snr_new), label='10m')

# 标记坐标原点(0,0)处的黑色点
plt.plot(0, 0, 'ko', markerfacecolor='k')

# 添加坐标轴标签
plt.xlabel('信杂比 (dB)')
plt.ylabel('识别率 (%)')

# 添加图例
plt.legend()

# 取消网格线显示
plt.grid(False)

# 设置坐标轴范围（确保图形从原点开始）
plt.xlim([-1, 12])  # 使 x 轴从 -1 开始
plt.ylim([-10, 100])  # 使 y 轴从 -10 开始

# 显示图形
plt.show()
