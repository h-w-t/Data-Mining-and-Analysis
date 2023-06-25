from io import StringIO

import pydotplus as pydotplus
from sklearn.model_selection import train_test_split, GridSearchCV

from .models import Iris, OrderSum, PositionInfo
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz


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
