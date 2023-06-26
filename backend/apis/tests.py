from django.test import TestCase
import pandas as pd
import numpy as np

# Create your tests here.
# ========= 关联规则算法 ========= #
class Apriori:
    def __init__(self, min_support, min_confidence):
        # self.database = Aprioridb
        self.dataset = pd.read_csv(r'D:\Projects\Data-Mining-and-Analysis\backend\data\Dataset.csv', header=0)
        self.dataset = self.dataset.drop(['id'], axis=1)
        self.min_support = min_support
        self.min_confidence = min_confidence
        print(self.dataset)

    # 从数据库获取数据集并转化为dataframe格式
    # def get_data(self):
    #     queryset = self.database.objects.all()
    #     dataset = pd.DataFrame(list(queryset.values()))
    #     dataset = dataset.drop(['id'], axis=1)
    #     return dataset

    # 获取一阶候选项集
    def get_first_candidate(self):
        dataset = self.dataset
        candidates = []
        for i in range(len(dataset.index)):  # 遍历每一行
            for j in range(len(dataset.columns)):    # 遍历每一行的每一项
                item = str(dataset.iloc[i, j])   # 获取每一项
                if item != 'nan':  # 如果该项不为 NaN
                    if item not in candidates:  # 如果该项不在候选项集中
                        candidates.append(item)  # 将每一项加入候选项集
        print(candidates)
        return candidates

    # 计算置信度矩阵
    def get_confidence_matrix(self):
        dataset = self.dataset
        candidates = self.get_first_candidate()
        # 初始化计数矩阵
        count_matrix = pd.DataFrame(np.zeros((len(candidates), len(candidates))), index=candidates, columns=candidates)
        # 得到事务集之间的支持度
        for transaction in dataset.values:  # 遍历每一行
            for item in transaction:    # 遍历每一行的每一项
                if str(item) != 'nan':  # 如果该项不为 NaN
                    for other_item in transaction:
                        if str(other_item) != 'nan':
                            count_matrix.at[item, other_item] += 1
        # 得到每项事务的支持度
        item_counts = dataset.apply(pd.value_counts).fillna(0).sum(axis=1).reindex(['面包', '可乐', '麦片', '牛奶', '鸡蛋'])
        # 置信度 = 事务集之间的支持度 / 每项事务的支持度
        confidence_matrix = count_matrix.div(item_counts, axis=0)
        print(confidence_matrix)
        return confidence_matrix

    # 将置信度矩阵转化为可用于Echarts热力图展示的数据格式
    def reformat(self):
        original_matrix = self.get_confidence_matrix()
        reformatted_matrix = []     # 初始化矩阵
        for i in range(len(original_matrix.index)):
            for j in range(len(original_matrix.columns)):
                reformatted_matrix.append([i, j, round(original_matrix.iloc[i, j], 2)])
        print(reformatted_matrix)
        return reformatted_matrix

    # 返回结果
    def result(self):
        self.reformat()


if __name__ == '__main__':
    apriori = Apriori(0.1, 0.1)
    apriori.result()


