import base64
from io import StringIO, BytesIO

import numpy as np
import pydotplus as pydotplus
from sklearn import tree
from sklearn.cluster import DBSCAN
from sklearn.model_selection import train_test_split, GridSearchCV

from .models import Iris, OrderSum, PositionInfo, Aprioridb, MoonsDataSet, RegressionData, BlobsDataSet
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz


# ========= 关联规则算法 ========= #
class Apriori:
    def __init__(self, min_support, min_confidence):
        self.database = Aprioridb
        self.dataset = self.get_data()
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.first_candidates = self.get_first_candidate()

    # 从数据库获取数据集并转化为dataframe格式
    def get_data(self):
        queryset = self.database.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        dataset = dataset.drop(['id'], axis=1)
        return dataset

    # 获取一阶候选项集
    def get_first_candidate(self):
        dataset = self.dataset
        candidates = []
        for i in range(len(dataset.index)):  # 遍历每一行
            for j in range(len(dataset.columns)):  # 遍历每一行的每一项
                item = str(dataset.iloc[i, j])  # 获取每一项
                if item != 'None':  # 如果该项不为 NaN
                    if item not in candidates:  # 如果该项不在候选项集中
                        candidates.append(item)  # 将每一项加入候选项集
        # print(candidates)
        return candidates



    # 求单项支持度
    def calculate_support_1(self, item):
        dataset = self.dataset
        support = 0
        for i in range(0, len(dataset.index)):
            item_sets = dataset.loc[i].values.tolist()
            if item[0] in item_sets:
                support += 1
        support = support / len(dataset.index)
        return support
    # def calculate_support(self, item):
    #     dataset = self.dataset
    #     support = dataset.astype(bool).sum(axis=0)[item] / len(dataset.index)
    #     return support

    # 计算二阶单项支持度
    def calculate_support_2(self, item):
        dataset = self.dataset
        support = 0
        for i in range(0, len(dataset.index)):
            item_sets = dataset.loc[i].values.tolist()
            if item[0] in item_sets and item[1] in item_sets:
                support += 1
        support = support / len(dataset.index)
        return support

    # 得到一阶频繁项集
    def get_first_frequent(self):
        first_candidates = self.get_first_candidate()
        frequent_items = [item for item in first_candidates if self.calculate_support(item) >= self.min_support]
        return frequent_items

    # 生成二阶候选项集合
    def generate_second_candidates(self, first_candidates):
        second_candidates = []
        for i in range(len(first_candidates)):
            for j in range(i + 1, len(first_candidates)):
                second_candidates.append([first_candidates[i], first_candidates[j]])
        return second_candidates

    # 计算二阶候选项集合支持度
    def calculate_support_list_second(self, candidates):
        dataset = self.dataset
        support_list = []
        for candidate in candidates:
            support = self.calculate_support_2(candidate)
            support_list.append(support)
        return support_list

    # 得到二阶频繁项集
    def get_second_frequent(self):
        first_candidates = self.get_first_candidate()
        second_candidates = self.generate_second_candidates(first_candidates)
        support_list = self.calculate_support_list_second(second_candidates)
        frequent_items = [item for item, support in zip(second_candidates, support_list) if support >= float(self.min_support)]
        return frequent_items

    # 计算二阶频繁项集的置信度
    def calculate_confidence(self, itemset, subset):
        dataset = self.dataset
        itemset_support = self.calculate_support_2(itemset)
        subset_support = self.calculate_support_1(subset)
        confidence = itemset_support / subset_support
        return confidence

    # 生成置信度矩阵，未构成关联规则的项集置信度为0，未达到最小置信度的关联规则置信度为0，对角线为1
    def generate_confidence_matrix(self, frequent_items):
        first_candidates = self.first_candidates
        confidence_matrix = pd.DataFrame(np.zeros((len(first_candidates), len(first_candidates))), index=first_candidates, columns=first_candidates)
        for frequent_itemsets in frequent_items:
            for candidate in first_candidates:
                if candidate in frequent_itemsets:
                    cof = self.calculate_confidence(frequent_itemsets, [candidate])
                else:
                    cof = 0
                confidence_matrix.loc[candidate, frequent_itemsets[0]] = cof
        for i in range(len(first_candidates)):
            confidence_matrix.iloc[i, i] = 1
        # print(confidence_matrix)
        return confidence_matrix

    # 将置信度矩阵转化为可用于Echarts热力图展示的数据格式
    def reformat(self):
        original_matrix = self.generate_confidence_matrix(self.get_second_frequent())
        reformatted_matrix = []  # 初始化矩阵
        for i in range(len(original_matrix.index)):
            for j in range(len(original_matrix.columns)):
                if original_matrix.iloc[i, j] >= self.min_confidence:
                    reformatted_matrix.append([i, j, round(original_matrix.iloc[i, j], 5)])
                else:
                    reformatted_matrix.append([i, j, 0])
        # print(reformatted_matrix)
        return reformatted_matrix

    # 返回结果
    def result(self):
        return self.reformat()


# ========= 聚类算法 ========= #
class Clustering:
    # 初始化
    def __init__(self):
        self.database = BlobsDataSet
        self.blobs_dataset = self.get_blobs_data()


    # 从数据库获取数据集
    def get_blobs_data(self):
        queryset = self.database.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        return dataset



    # 将初始数据集转化为可用于Echarts散点图展示的数据格式
    def original_blobs_data_for_echarts(self):
        dataset = self.get_blobs_data()
        dataset = dataset.drop(['label'], axis=1)
        reformatted_dataset = []
        for i in range(len(dataset.index)):
            reformatted_dataset.append([dataset.iloc[i, 1], dataset.iloc[i, 2]])
        return reformatted_dataset


class DBSCAN_Clustering:
    # 初始化
    def __init__(self, eps=None, min_samples=None):
        self.database = MoonsDataSet
        self.dataset = self.get_moons_data()
        self.eps = eps
        self.min_samples = min_samples

    # 获取初始数据
    def get_moons_data(self):
        queryset = self.database.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        return dataset

    # 将初始数据集转化为可用于Echarts散点图展示的数据格式
    def original_moons_data_for_echarts(self):
        dataset = self.get_moons_data()
        dataset = dataset.drop(['label'], axis=1)
        reformatted_dataset = []
        for i in range(len(dataset.index)):
            reformatted_dataset.append([dataset.iloc[i, 1], dataset.iloc[i, 2]])
        return reformatted_dataset

    # 使用DBSCAN聚类
    def cluster(self):
        dataset = self.dataset
        dataset = dataset.drop(['id'], axis=1)
        dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)
        dbscan.fit(dataset.drop(['label'], axis=1))
        labels = dbscan.labels_
        dataset['label'] = labels
        return dataset

    # 将聚类结果转化为可用于Echarts散点图展示的数据格式
    def DBCSCAN_clustered_result_for_echarts(self):
        dataset = self.cluster()
        reformatted_dataset = []
        for i in range(len(dataset.index)):
            reformatted_dataset.append([dataset.iloc[i, 0], dataset.iloc[i, 1], dataset.iloc[i, 2]])
        return reformatted_dataset



# ========= 分类算法（决策树） ========= #
class Classifier:
    # 类初始化
    def __init__(self, tree_height, child_node_num):
        self.database = Iris
        self.dataset = self.get_data()
        self.tree_height = tree_height
        self.child_node_num = child_node_num

    # 从数据库获取数据集并转化为dataframe格式
    def get_data(self):
        queryset = self.database.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        dataset = dataset.drop(['id'], axis=1)
        return dataset

    # 数据据集划分
    def divide_dataset(self, dataset):
        X = dataset.loc[:, 'SpeL':'PetW']  # 提取数据集中的特征
        y = dataset['Species']  # 提取数据集中的标签
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2021)  # 划分训练集和测试集
        return X_train, X_test, y_train, y_test

    # 使用entropy系数作为划分标准训练决策树模型
    def train_tree(self, dataset):
        X_train, X_test, y_train, y_test = self.divide_dataset(dataset)
        clf = DecisionTreeClassifier(criterion='entropy', max_depth=self.tree_height, min_samples_split=self.child_node_num)
        clf.fit(X_train, y_train)
        return clf

    # 绘制决策树图
    def get_tree_image(self, tree_model):
        dot_data = tree.export_graphviz(tree_model, out_file=None, feature_names=['PetL', 'PetW', 'SepL', 'SepW'], class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], filled=True, rounded=True, special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        # graph.write_png(r'D:\Projects\Data-Mining-and-Analysis\backend\media\images\decision_tree.png')
        image = graph.create_png()
        return image

    # 将图片转码为Base64格式
    def get_tree_image_base64(self):
        image = self.get_tree_image(self.train_tree(self.dataset))
        buffered = BytesIO(image)
        encoded_image = base64.b64encode(buffered.getvalue()).decode()
        return "data:image/png;base64," + encoded_image


# ========= 回归算法 ========= #
class Regression:
    def __init__(self):
        self.database = RegressionData

    def get_data(self):
        queryset = self.database.objects.all()
        dataset = pd.DataFrame(list(queryset.values()))
        return dataset

    def original_regression_data_for_echarts(self):
        dataset = self.get_data()
        reformatted_dataset = []
        for i in range(len(dataset.index)):
            reformatted_dataset.append([dataset.iloc[i, 1], dataset.iloc[i, 2]])
        return reformatted_dataset
