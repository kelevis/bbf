import matplotlib.pyplot as plt
import numpy as np

# 数据
distance_5m = [10, 6, 8]
snr_5m = [85, 75, 82]
distance_10m = [10, 6, 8]
snr_10m = [78, 70, 75]

# 创建图形
plt.figure(figsize=(8, 6))

# 绘制两条曲线
plt.plot(snr_5m, distance_5m, marker='o', label='5m')
plt.plot(snr_10m, distance_10m, marker='x', label='10m')

# 添加标题、坐标轴标签和图例
plt.title('军民识别率与信杂比关系')
plt.xlabel('信杂比')
plt.ylabel('军民识别率')
plt.legend()

# 显示网格
plt.grid(True)

# 显示图形
plt.show()