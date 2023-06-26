from io import StringIO

import numpy as np
import pydotplus as pydotplus
from sklearn.model_selection import train_test_split, GridSearchCV

from .models import Iris, OrderSum, PositionInfo, Aprioridb
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz

# ========= 关联规则算法 ========= #
class Apriori:
    def __init__(self, min_support, min_confidence):
        self.database = Aprioridb
        self.min_support = min_support
        self.min_confidence = min_confidence

    # 从数据库获取数据集并转化为dataframe格式
    def get_data(self):
        queryset = self.database.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        dataset = dataset.drop(['id'], axis=1)
        return dataset

    # 获取一阶候选项集
    def get_first_candidate(self):
        dataset = self.get_data()
        candidates = []
        for i in range(len(dataset.index)):  # 遍历每一行
            for j in range(len(dataset.columns)):    # 遍历每一行的每一项
                item = str(dataset.iloc[i, j])   # 获取每一项
                if item != 'None':  # 如果该项不为 NaN
                    if item not in candidates:  # 如果该项不在候选项集中
                        candidates.append(item)  # 将每一项加入候选项集
        # print(candidates)
        return candidates

    # 计算置信度矩阵
    def get_confidence_matrix(self):
        dataset = self.get_data()
        candidates = self.get_first_candidate()
        # 初始化计数矩阵
        count_matrix = pd.DataFrame(np.zeros((len(candidates), len(candidates))), index=candidates, columns=candidates)
        # 得到事务集之间的支持度
        for transaction in dataset.values:  # 遍历每一行
            for item in transaction:    # 遍历每一行的每一项
                if str(item) != 'None':  # 如果该项不为 NaN
                    for other_item in transaction:
                        if str(other_item) != 'None':
                            count_matrix.at[item, other_item] += 1
        # 得到每项事务的支持度
        item_counts = dataset.apply(pd.value_counts).fillna(0).sum(axis=1).reindex(['面包', '可乐', '麦片', '牛奶', '鸡蛋'])
        # 置信度 = 事务集之间的支持度 / 每项事务的支持度
        confidence_matrix = count_matrix.div(item_counts, axis=0)
        # print(confidence_matrix)
        return confidence_matrix


    # 将置信度矩阵转化为可用于Echarts热力图展示的数据格式
    def reformat(self):
        original_matrix = self.get_confidence_matrix()
        reformatted_matrix = []     # 初始化矩阵
        for i in range(len(original_matrix.index)):
            for j in range(len(original_matrix.columns)):
                reformatted_matrix.append([i, j, round(original_matrix.iloc[i, j], 2)])
        # print(reformatted_matrix)
        return reformatted_matrix

    # 返回结果
    def result(self):
        return self.reformat()


# ========= 聚类算法 ========= #
class Clustering:
    # 初始化
    def __init__(self, data):
        self.dataset = self.get_data()

    # 从数据库获取数据集
    def get_data(self):
        queryset = Iris.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        dataset = dataset.drop(['id', 'Species'], axis=1)
        return dataset

    # pca降维
    def pca(self, dataset):
        dataset = self.dataset
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(dataset)

    # K-Means聚类
    def kmeans(self):
        pass

    # 返回结果
    def result(self):
        pass


# ========= 分类算法（决策树） ========= #
class Classifier:
    # 类初始化
    def __init__(self, tree_height, child_node_num):
        self.database = Iris
        self.tree_height = tree_height
        self.child_node_num = child_node_num

    # 从数据库获取数据集并转化为dataframe格式
    def get_data(self):
        queryset = self.database.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        dataset = dataset.drop(['id', 'Species'], axis=1)
        return dataset

    # 数据据集划分
    def divide_dataset(self, dataset):
        X = dataset.loc[:, 'Sepal.Length':'Petal.Width']  # 提取数据集中的特征
        y = dataset['Species']  # 提取数据集中的标签
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2021)  # 划分训练集和测试集
        return X_train, X_test, y_train, y_test

    # 使用entropy系数作为划分标准训练决策树
    def train_tree(self, dataset):
        X_train, X_test, y_train, y_test = self.divide_dataset(dataset)  # 划分训练集和测试集
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=self.tree_height,
                                     min_samples_leaf=self.child_node_num)
        tree_model = clf.fit(X_train, y_train)
        return tree_model

    # 绘制决策树图并保存到本地
    def draw_tree(self, tree_model):
        dot_data = StringIO()   # 创建一个内存空间
        export_graphviz(tree_model, out_file=dot_data,      # 绘制决策树图
                        filled=True, rounded=True,
                        special_characters=True, feature_names=self.get_data().columns)
        graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  # 从内存空间中获取图
        graph.write_png('../decision_tree.png')    # 保存图

    # 返回结果
    def result(self):
        dataset = self.get_data()
        tree_model = self.train_tree(dataset)
        return tree_model

    # 返回决策树图
    def get_png(self):
        self.draw_tree(self.train_tree(self.get_data()))
        return 'decision_tree.png'
