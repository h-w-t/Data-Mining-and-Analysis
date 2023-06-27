import numpy as np
from sklearn import datasets

# 生成聚类使用的初始数据集
# 生成3个簇，每个簇500个样本（簇状数据集）
X_blobs, y_blobs = datasets.make_blobs(n_samples=1500, centers=3, random_state=8)
# 生成2个簇，每个簇500个样本（月牙型数据集）
X_moons, y_moons = datasets.make_moons(n_samples=1000, noise=0.05, random_state=8)

# 规范数据格式，保留2位小数
X_blobs = np.around(X_blobs, 2)
X_moons = np.around(X_moons, 2)
y_blobs = y_blobs.astype(int)
y_moons = y_moons.astype(int)

# 合并数据并设置格式
blobs = np.column_stack((X_blobs, y_blobs))
moons = np.column_stack((X_moons, y_moons))

# 保存为 CSV 文件
np.savetxt('blobs.csv', blobs, delimiter=',', fmt=['%.2f', '%.2f', '%d'], header='x,y,label', comments='', encoding='utf-8')
np.savetxt('moons.csv', moons, delimiter=',', fmt=['%.2f', '%.2f', '%d'], header='x,y,label', comments='', encoding='utf-8')
