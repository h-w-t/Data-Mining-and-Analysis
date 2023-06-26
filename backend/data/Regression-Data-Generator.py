# 生成用于回归的数据集
# 生成的数据集为csv格式，包含两列，第一列为x，第二列为y

import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

n_samples = 500     # 样本数
n_outliers = 100    # 噪声点数

# 生成随机数据
X, y = datasets.make_regression(n_samples=n_samples, n_features=1,
                                n_informative=1, noise=10,
                                coef=False, random_state=42)

# 添加噪声数据
np.random.seed(42)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)

# 保留 4 位小数
X = np.round(X, 4)
y = np.round(y, 4)

# 保存数据
data = np.hstack((X, y.reshape(-1, 1)))     # 水平拼接
np.savetxt('Regression_data.csv', data, delimiter=',', fmt='%.4f')  # 保存为csv格式
