from .models import Iris, OrderSum, PositionInfo
import pandas as pd
from sklearn.decomposition import PCA

'''聚类算法'''
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
